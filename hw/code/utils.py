import datetime


def get_today():
    return datetime.datetime.today().strftime("%Y-%m-%d")


def long_text(len):
    str = ''
    for i in range(len):
        str += '1'
    return str
