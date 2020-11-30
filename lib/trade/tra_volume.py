import sys
import os
import datetime as dt
from pytz import timezone
from enum import Enum

base_dir = os.path.dirname(__file__) or '.'

exchange_dir = os.path.join(base_dir, '..\exchange')
sys.path.insert(1, exchange_dir)
from exc_exchange import *

class EVolume(Enum):
    LOW = 0
    HIGH = 1

exchange = Exchange()

class Volume:
    symbol: str
    interval: EInterval
    startTime: dt
    endTime: dt
    limit: int
    triggerFrequency: int
    volumeTriggerTolerance: float

    # Constructor
    def __init__(self, symbol, interval, startTime = None, endTime = None, limit = 500, 
        triggerFrequency = 1, volumeTriggerTolerance = 4000.0
    ):
        self.symbol = symbol
        self.interval = interval
        self.startTime = startTime
        self.endTime = endTime
        self.limit = limit
        self.triggerFrequency = triggerFrequency
        self.volumeTriggerTolerance = volumeTriggerTolerance

    def __FindVolumeTimeHigh(self, timezoneStr):
        klineList = []
        klineList = exchange.getCandleData(self.symbol, self.interval, limit=self.limit)#, startTime, endTime, limit)
        triggerList = []
        for hour in range(23):
            count = 0
            triggerList.append(count)
            for candle in klineList:
                utcOpenTime = dt.datetime.utcfromtimestamp(candle.openTime / 1000)
                utcCloseTime = dt.datetime.utcfromtimestamp(candle.closeTime / 1000)
                if (float(candle.volume) >= self.volumeTriggerTolerance):
                    if (utcOpenTime.hour == hour):
                        triggerList[hour] = triggerList[hour] + 1
                        if (triggerList[hour] >= self.triggerFrequency):
                            print(timezoneStr + ": " + str(utcOpenTime.astimezone(timezone(timezoneStr)).time()))
                            triggerList[hour] = -100

    def __FindVolumeTimeLow(self, timezoneStr):
        klineList = []
        klineList = exchange.getCandleData(self.symbol, self.interval, limit=self.limit)#, startTime, endTime, limit)
        triggerList = []
        for hour in range(23):
            count = 0
            triggerList.append(count)
            for candle in klineList:
                utcOpenTime = dt.datetime.utcfromtimestamp(candle.openTime / 1000)
                utcCloseTime = dt.datetime.utcfromtimestamp(candle.closeTime / 1000)
                if (float(candle.volume) <= self.volumeTriggerTolerance):
                    if (utcOpenTime.hour == hour):
                        triggerList[hour] = triggerList[hour] + 1
                        if (triggerList[hour] >= self.triggerFrequency):
                            print(timezoneStr + ": " + str(utcOpenTime.astimezone(timezone(timezoneStr)).time()))
                            triggerList[hour] = -100


    # This method is used in order to determine timeframes in which a particular currency is least/most volatile
    # self          [In] - The instance of the class.
    # timezoneStr   [In] - The timezone of time to capture.
    # volume        [In] - The volume that determines whether the times that should be searched is when volume is HIGH/LOW.
    def FindVolumeTime(self, timezoneStr: str = "UTC", volume: EVolume = EVolume.HIGH):
        if (volume == EVolume.HIGH):
            self.__FindVolumeTimeHigh(timezoneStr)
        else:
            self.__FindVolumeTimeLow(timezoneStr)

