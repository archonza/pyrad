from enum import Enum

class EPattern(Enum):
    UNDEFINED = 0
    DOJI_GRAVESTONE = 1
    DOJI_TRADITIONAL = 2
    DOJI_DRAGONFLY = 3
    DOJI_LONGLEGGED = 4
    HAMMER = 5
    HANGING_MAN = 6
    SHOOTING_STAR = 7
    CHECKMATE = 8
    EVENING_STAR = 9
    MORNING_STAR = 10
    BULLISH_ENGULFING = 11
    BEARING_ENGULFING = 12
    BULLISH_HARAMI = 13
    BEARISH_HARAMI = 14
    KICKER = 15
    PIERCING_LINE = 16
    DARK_CLOUD_COVER = 17
    THREE_WHITE_SOLDIERS = 18
    THREE_BLACK_CROWS = 19
    TWEEZER_BOTTOMS = 20
    TWEEZER_TOPS = 21
    BULLISH = 22
    BEARISH = 23
    DOJI = 24

sumOfClosePrices = 0.0
period = 0

class Pattern:
    # Constructor
    def __init__(self, highPrice: float, lowPrice: float, openPrice: float, closePrice: float, genTol: float, tradTol: float, longTol: float, trend):
        self.highPrice = highPrice
        self.lowPrice = lowPrice
        self.openPrice = openPrice
        self.closePrice = closePrice
        self.trend = trend
        self.genTol = genTol
        self.tradTol = tradTol
        self.longTol = longTol
        self.addSimpleMovingAverage()

    def getPattern(self) -> EPattern:
        pattern = EPattern.UNDEFINED
        if (self.isDojiGravestone()):
            pattern = EPattern.DOJI_GRAVESTONE
        elif (self.isDojiTraditional()):
            pattern = EPattern.DOJI_TRADITIONAL
        elif (self.isDojiDragonfly()):
            pattern = EPattern.DOJI_DRAGONFLY
        elif (self.isDojiLonglegged()):
            pattern = EPattern.DOJI_LONGLEGGED
        elif (self.isHammer()):
            pattern = EPattern.HAMMER
        elif (self.isBullish()):
            pattern = EPattern.BULLISH
        elif (self.isBearish()):
            pattern = EPattern.BEARISH
        elif (self.isDoji()):
            pattern = EPattern.DOJI
        return pattern

    def isBullish(self) -> bool:
        if (self.closePrice > self.openPrice):
            return True
        else:
            return False

    def isBearish(self) -> bool:
        if (self.closePrice < self.openPrice):
            return True
        else:
            return False

    def isDoji(self) -> bool:
        if (self.closePrice == self.openPrice):
            return True
        else:
            return False

    def isDojiGravestone(self) -> bool:
        if (self.isLowPriceEqualToOpenPrice() and
            (self.isHighPriceGreaterThanOpenPrice() and
             self.isClosePriceEqualToOpenPrice())):
            return True
        else:
            return False

    def isDojiTraditional(self) -> bool:
        if (self.isClosePriceEqualToOpenPrice() and
            self.isLowPriceLessThanClosePrice() and
            self.isHighPriceGreaterThanClosePrice() and
            self.isClosePriceMinusLowPriceEqualToHighPriceMinusClosePrice() and
            not self.isLeggsLong()):
            return True
        else:
            return False

    def isDojiDragonfly(self) -> bool:
        if (self.isLowPriceLessThanOpenPrice() and
            self.isHighPriceEqualToOpenPrice() and
            self.isClosePriceEqualToOpenPrice()):
            return True
        else:
            return False

    def isDojiLonglegged(self) -> bool:
        if (self.isClosePriceEqualToOpenPrice() and
           self.isLowPriceLessThanClosePrice() and
           self.isHighPriceGreaterThanClosePrice() and
           self.isClosePriceMinusLowPriceEqualToHighPriceMinusClosePrice() and
           self.isLeggsLong()):
            return True
        else:
            return False

    def isHammer(self) -> bool:
        if(self.isHighPriceGreaterThanOpenPrice() and
           self.isClosePriceLessThanOpenPrice() and
           self.isLowPriceLessThanOpenPrice() and
           self.isLowPriceLessThanClosePrice() and
           (self.trend == "bearish") and
           #(self.highPrice >= self.previousOpenPrice) and 
           (self.lowPrice >= 3* (self.openPrice - self.closePrice))):
            return True
        else:
            return False

    def isHangingMan(self) -> bool:
        return True

    def isShootingStar(self) -> bool:
        return True

    def isCheckmate(self) -> bool:
        return True

    def isEveningStar(self) -> bool:
        return True

    def isMorningStar(self) -> bool:
        return True

    def isBullishEngulfing(self) -> bool:
        return True

    def isBearishEngulfing(self) -> bool:
        return True

    def isBullishHarami(self) -> bool:
        return True

    def isBearishHarami(self) -> bool:
        return True

    def isKicker(self) -> bool:
        return True

    def isPiercingLine(self) -> bool:
        return True

    def isDarkCloudCover(self) -> bool:
        return True

    def isThreeWhiteSoldiers(self) -> bool:
        return True

    def isThreeBlackCrows(self) -> bool:
        return True

    def isTweezerBottoms(self) -> bool:
        return True

    def isTweezerTops(self) -> bool:
        return True

    def isLeggsLong(self) -> bool:
        if (((self.closePrice - self.lowPrice) >= self.longTol) and 
            ((self.highPrice - self.closePrice) >= self.longTol)):
            return True
        else:
            return False

    def isLowPriceEqualToOpenPrice(self) -> bool:
        if ((self.lowPrice >= (self.openPrice - self.genTol)) and 
            (self.lowPrice <= (self.openPrice + self.genTol))):
            return True
        else:
            return False

    def isHighPriceEqualToOpenPrice(self) -> bool:
        if ((self.highPrice >= (self.openPrice - self.genTol)) and 
            (self.highPrice <= (self.openPrice + self.genTol))):
            return True
        else:
            return False

    def isClosePriceEqualToOpenPrice(self) -> bool:
        if ((self.closePrice >= (self.openPrice - self.genTol)) and 
            (self.closePrice <= (self.openPrice + self.genTol))):
            return True
        else:
            return False

    def isClosePriceMinusLowPriceEqualToHighPriceMinusClosePrice(self) -> bool:
        if (((self.closePrice - self.lowPrice) >= (self.highPrice - self.closePrice - self.genTol)) and
            ((self.closePrice - self.lowPrice) <= (self.highPrice - self.closePrice + self.genTol))):
            return True
        else:
            return False

    def isHighPriceGreaterThanOpenPrice(self) -> bool:
        if (self.highPrice > (self.openPrice - self.genTol)):
            return True
        else:
            return False

    def isHighPriceGreaterThanClosePrice(self) -> bool:
        if (self.highPrice > (self.closePrice - self.genTol)):
            return True
        else:
            return False

    def isLowPriceLessThanClosePrice(self) -> bool:
        if (self.lowPrice < (self.closePrice + self.genTol)):
            return True
        else:
            return False

    def isLowPriceLessThanOpenPrice(self) -> bool:
        if (self.lowPrice < (self.openPrice + self.genTol)):
            return True
        else:
            return False

    def isClosePriceLessThanOpenPrice(self) -> bool:
        if (self.closePrice < (self.openPrice + self.genTol)):
            return True
        else:
            return False

    def isTrendBulish(self) -> bool:
        return True

    def isTrendBearish(self) -> bool:
        return True

    def isTrendFlat(self) -> bool:
        return True

    def getSupportPrice(self) -> float:
        return 0.0

    def getResistancePrice(self) -> float:
        return 0.0

    def addSimpleMovingAverage(self) -> float:
        global period
        global sumOfClosePrices
        period = period + 1
        sumOfClosePrices = sumOfClosePrices + self.closePrice

    def getSimpleMovingAverage(self) -> float:
        global period
        global sumOfClosePrices
        return (sumOfClosePrices / float(period))

    def resetSimpleMovingAverage(self):
        global period
        global sumOfClosePrices
        sumOfClosePrices = 0.0
        period = 0


    #def isClosePriceMinusLowPriceLessThanClosePrice():
    #    if ((self.closePrice - self.lowPrice) < self.closePrice)
