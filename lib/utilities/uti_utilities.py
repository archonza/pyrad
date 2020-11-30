import datetime as dt
from pytz import timezone

class Utilities:
    
    def getUTCDateTimeStr(self, timeStampMs: int) -> str:
        return str(dt.datetime.utcfromtimestamp(timeStampMs / 1000))

    def getUTCDateTimeObject(self, timeStampMs: int) -> dt.datetime:
        return str(dt.datetime.utcfromtimestamp(timeStampMs / 1000))

    def getUTCTimeStr(self, timeStampMs: int) -> str:
        dateTime = dt.datetime.utcfromtimestamp(timeStampMs / 1000)
        time = str(dateTime.hour) + ":" + str(dateTime.minute) + ":" + str(dateTime.second)
        return time

    def getUTCDateStr(self, timeStampMs: int) -> str:
        dateTime = dt.datetime.utcfromtimestamp(timeStampMs / 1000)
        date = str(dateTime.year) + ":" + str(dateTime.month) + ":" + str(dateTime.day)
        return date