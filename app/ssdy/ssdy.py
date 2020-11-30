# Imports standard python functionality
import sys
import os
from enum import Enum
#print(sys.path)
base_dir = os.path.dirname(__file__) or '.'
# Import lib common functionality
common_dir = os.path.join(base_dir, '..\..\lib\common')
sys.path.insert(1, common_dir)
#print(sys.path)
from com_common import *

# Import lib exchange functionality
exchange_dir = os.path.join(base_dir, '..\..\lib\exchange')
sys.path.insert(1, exchange_dir)
from exc_exchange import *
from exc_types import *

# Import lib trade functionality
trade_dir = os.path.join(base_dir, '..\..\lib\\trade')
sys.path.insert(1, trade_dir)
from tra_pattern import *
from tra_pivot_point import *
from tra_resistance import *
from tra_support import *
from tra_trade import *
from tra_volume import *

# Import lib utilities functionality
utilities_dir = os.path.join(base_dir, '..\..\lib\\utilities')
print(utilities_dir)
sys.path.insert(1, utilities_dir)
from uti_utilities import *

# Define constants
BTCUSDT_HOUR_TOLERANCE = 10.0
BTCUSDT_HOUR_DOJI_TRADITIONAL_TOLERANCE = 20.0
BTCUSDT_HOUR_DOJI_LONG_LEGGED_TOLERANCE = 40.0

# Instantiate classes
exchange = Exchange()

# Public Function definitions
def analyseCandlestickData():
    print("TODO")

def PrintTimesWhenVolumeIsLow():
    tradeVolue = Volume("BTCUSDT", EInterval.ONE_HR, limit=1000, triggerFrequency=8, 
    volumeTriggerTolerance=1500)
    tradeVolue.FindVolumeTime("UTC", EVolume.LOW)
    tradeVolue.FindVolumeTime("Africa/Johannesburg",EVolume.LOW)

def PrintCandlePatternNames():
    klineList = []
    klineList = exchange.getCandleData("BTCUSDT", EInterval.ONE_HR, limit=240)
    for candle in klineList:
        candlePattern = Pattern(candle.high, candle.low, candle.open, candle.close, BTCUSDT_HOUR_TOLERANCE, BTCUSDT_HOUR_DOJI_TRADITIONAL_TOLERANCE, BTCUSDT_HOUR_DOJI_LONG_LEGGED_TOLERANCE, "BULLISH")
        print()
        print("==[Start]===============================")
        print("OpenTime: " + str(candle.openTime))
        print("High: " + str(candle.high))
        print("Low: " + str(candle.low))
        print("Open: " + str(candle.open))
        print("Close: " + str(candle.close))
        print(candlePattern.getPattern())
        print("SimpleMovingAverage: " + str(candlePattern.getSimpleMovingAverage()))
        print("==[End]=================================")
        print()

    candlePattern.resetSimpleMovingAverage()

def PrintDataPoints():
    utilities = Utilities()
    klineList = []
    klineList = exchange.getCandleData("BTCUSDT", EInterval.ONE_HR, limit=240)
    trade = Trade()
    pivotPoint = PivotPoint()
    support = Support()
    resistance = Resistance()

    #previousDayClose = getCandleDataRaw()
    previousDayClose = trade.getPreviousDayClose("2020:11:29", klineList)
    if (previousDayClose is None):
        print("previousDayClose not defined")
    else:
        print("open: " + str(previousDayClose.open))
        print("low: " + str(previousDayClose.low))
        print("high: " + str(previousDayClose.high))
        print("close: " + str(previousDayClose.close))
        pivotPoint.calculatePivotPoint(previousDayClose.high, previousDayClose.low, previousDayClose.close)
        print("PivotPoint: " + str(pivotPoint.getValue()))
        support.calculateSupportLevels(pivotPoint.getValue(), previousDayClose.high, previousDayClose.low, previousDayClose.close)
        print("Support Level S1: " + str(support.getSupportLevel(ESupportLevels.S1)))
        print("Support Level S2: " + str(support.getSupportLevel(ESupportLevels.S2)))
        print("Support Level S3: " + str(support.getSupportLevel(ESupportLevels.S3)))
        resistance.calculateResistanceLevels(pivotPoint.getValue(), previousDayClose.high, previousDayClose.low, previousDayClose.close)
        print("Resistance Level R1: " + str(resistance.getResistanceLevel(pivotPoint.getValue(), EResistanceLevels.R1)))
        print("Resistance Level R2: " + str(resistance.getResistanceLevel(pivotPoint.getValue(), EResistanceLevels.R2)))
        print("Resistance Level R3: " + str(resistance.getResistanceLevel(pivotPoint.getValue(), EResistanceLevels.R3)))
    # Count how many time a pivot point was hit in a trading session

# Application Start
#executeTests()
#simulateSystemBehavior()
#sys.stdout = open('./out/output.txt','wt')
#PrintCandlePatternNames()
PrintDataPoints()

