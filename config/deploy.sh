#!/bin/sh

set -e

Template () {
	SOURCE="${1}"
	TARGET="${2}"

	# Could be a symlink
	sudo rm -f ${TARGET}

	sed \
		-e "s@__BASE_DIR__@${BASE_DIR}@g" \
		"${SOURCE}" \
		| sudo tee "${TARGET}"
}

Wait_for () {
	PIDFILE="${1}"
	TIMEOUT="${2}"

	for X in $(seq ${TIMEOUT})
	do
		if kill -0 "$(cat "${PIDFILE}" 2>/dev/null)" 2>/dev/null
		then
			return 0
		fi

		echo "I: Process in ${PIDFILE} doesn't exist yet (${X}/${TIMEOUT})"

		sleep 1
	done

	return 1
}

if [ "$(id -u)" = 0 ]
then
	echo "${0}: should not be run as root"
	exit 1
fi

BASE_DIR="$(dirname $(readlink -f "$(dirname ${0})"))"
CELERY_WORKER_PIDFILE="${BASE_DIR}/celery-worker.pid"

if [ ! -d "${BASE_DIR}" ]
then
	echo "${0}: target '${BASE_DIR}' does not exist"
	exit 1
fi

cd "${BASE_DIR}"

sudo apt-get install --yes \
	python-virtualenv \
	nginx \
	gunicorn \
	postgresql-9.3 \
	redis-server \
	libpq-dev \
	python-dev


# Stop services so we don't get race conditions
start-stop-daemon \
	--stop \
	--retry forever/TERM/1 \
	--quiet \
	--oknodo \
	--pidfile "${CELERY_WORKER_PIDFILE}"
rm -f "${CELERY_WORKER_PIDFILE}"
sudo /etc/init.d/gunicorn stop
sudo /etc/init.d/nginx stop

# Virtualenv
if [ ! -d "${BASE_DIR}/env" ]
then
	virtualenv env
fi
. env/bin/activate

pip install -r requirements.txt
pip install gunicorn psycopg2

# Configure gunicorn. We want to use the initscripts from the Debian package,
# but the Python interpreter from our virtualenv, so we take over
# /usr/bin/gunicorn.
sudo dpkg-divert --local --divert /usr/bin/gunicorn.dpkg-divert --rename /usr/bin/gunicorn
sudo ln -sf ${BASE_DIR}/env/bin/gunicorn /usr/bin/gunicorn
Template config/gunicorn /etc/gunicorn.d/takeyourmeds

# Configure nginx
sudo rm -f /etc/nginx/sites-enabled/default
Template config/nginx /etc/nginx/sites-enabled/takeyourmeds

# Migrations, etc.
sudo -u postgres createuser takeyourmeds -SDR || true
sudo -u postgres createdb -E UTF-8 -O takeyourmeds takeyourmeds || true
python manage.py migrate --verbosity=2

# Start queue and block until it appears
python manage.py celery worker --pidfile="${CELERY_WORKER_PIDFILE}" --detach
Wait_for "${CELERY_WORKER_PIDFILE}" 30

sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/nginx restart
