from exc_request import *
from exc_converter import *
from exc_types import *

class Exchange:
    request = None
    converter = None

    def __init__(self):
        self.request = Request()
        self.converter = Converter()

    def getPing(self) -> Ping:
        return self.converter.convertPingRawToReal(self.request.getPingRaw())

    def getServerTime(self) -> ServerTime:
        return self.converter.convertServerTimeRawToReal(self.request.getServerTimeRaw())

    def getSymbolPriceTicker(self, symbol: str) -> SymbolPriceTicker:
        return self.converter.convertSymbolPriceTickerRawToReal(self.request.getSymbolPriceTickerRaw(symbol))

    def getCurrentAveragePrice(self, symbol: str) -> CurrentAveragePrice:
        return self.converter.convertCurrentAveragePriceRawToReal(self.request.getCurrentAveragePriceRaw(symbol))

    def getCandleData(self, symbol: str, interval: EInterval, startTime: int = -1, endTime: int = -1, limit: int = -1) -> CandleData:
        return self.converter.convertKLineDataRawToReal(self.request.getCandleDataRaw(symbol, interval, startTime, endTime, limit))
    