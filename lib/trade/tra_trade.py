# Imports standard python functionality
import sys
import os
from enum import Enum
import datetime as dt
from typing import List
import array

base_dir = os.path.dirname(__file__) or '.'

# Import lib exchange functionality
exchange_dir = os.path.join(base_dir, '..\exchange')
sys.path.insert(1, exchange_dir)
from exc_types import *

# Import lib utilities functionality
utilities_dir = os.path.join(base_dir, '..\\utilities')
sys.path.insert(1, utilities_dir)
from uti_utilities import *

class Trade:

    #def __init__(self):
        #self.prevOpenPrice = prevOpenPrice
        #self.prevHighPrice = prevHighPrice
        #self.prevLowPrice = prevLowPrice
        #self.prevClosePrice = prevClosePrice
        #self.calculateSupportLevels()
        #self.calculateResistanceLevels()

    def getPreviousDayClose(self, previousDayDate: str, klineList: List[CandleData]) -> CandleData:
        utilities = Utilities()
        for candle in klineList:
            if (utilities.getUTCDateStr(candle.closeTime) == previousDayDate):
                if (utilities.getUTCTimeStr(candle.closeTime) == "23:59:59"):
                    return candle

    # This function return's how many time a specific level was breached in a session
    def getDataPointHitCount(self, session, level):
        for candle in session:
            print("")
            
