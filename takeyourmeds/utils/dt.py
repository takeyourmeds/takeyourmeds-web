import pytz
import datetime

def local_time(timezone='Europe/London'):
    now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

    return now.astimezone(pytz.timezone(timezone))
