from datetime import datetime


def datestr2date(datestr):
    date, time = datestr.split('_')
    date = date.split('-')
    time = time.split('-')
    year, month, day, hour, minute, second = [int(f) for f in date + time]
    return datetime(year,month,day,hour,minute,second)


def now():
    d = datetime.now()
    return f"{d.year}-{str(d.month).zfill(2)}-{str(d.day).zfill(2)}_{str(d.hour).zfill(2)}-{str(d.minute).zfill(2)}-{str(d.second).zfill(2)}"