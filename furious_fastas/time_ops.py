from datetime import datetime


def datestr2date(datestr):
    date, time = datestr.split('_')
    date = date.split('-')
    time = time.split('-')
    year, month, day, hour, minute, second = [int(f) for f in date + time]
    return datetime(year,month,day,hour,minute,second)


def now():
    d = datetime.now()
    return "{}-{}-{}_{}-{}-{}".format(d.year,d.month,d.day,d.hour,d.minute,d.second)