import datetime


def get_today():
    return datetime.datetime.today().strftime("%Y-%m-%d")


def get_today_campaign_name():
    return f'Кампания {get_today()}'


def long_text(len):
    str = ''
    for i in range(len):
        str += '1'
    return str
