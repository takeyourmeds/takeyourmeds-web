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


if [ "$(id -u)" = 0 ]
then
	echo "${0}: should not be run as root"
	exit 1
fi

BASE_DIR="$(dirname $(readlink -f "$(dirname ${0})"))"

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
	libpq-dev \
	python-dev

# Stop services so we don't get race conditions
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

sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/nginx restart
