def to_date(dateTime: str):
    if dateTime is None:
        return None
    else:
        return dateTime[0:10]


def to_time(dateTime: str):
    if dateTime is None:
        return None
    else:
        return dateTime[11:19]
