from datetime import datetime, timedelta, date
from . import settings as s


def get_date_range():
    rolling_date = convert_to_date(s.mtm_vars['start_date'])
    end_date = convert_to_date(s.mtm_vars['end_date'])

    if end_date < rolling_date:
        raise ValueError("Start date and end date may be swaped !")

    date_range = []
    while rolling_date <= end_date:
        date_range.append(str(rolling_date))
        rolling_date += timedelta(1)

    return date_range


def convert_to_date(date_var):
    if isinstance(date_var, str):
        return datetime.strptime(date_var, '%Y-%m-%d').date()
    elif isinstance(date_var, date):
        return date_var
    else:
        raise TypeError("Date format is wrong")
