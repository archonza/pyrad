import sys
import os

base_dir = os.path.dirname(__file__) or '.'

# Import lib exchange functionality
exchange_dir = os.path.join(base_dir, '..\lib\exchange')
sys.path.insert(1, exchange_dir)
from exc_exchange import *
from exc_request import *
from exc_converter import *

def simulateSystemBehavior():
    request = Request()
    converter = Converter()
    print(converter.convertPingRawToReal(request.getPingRaw()))
    print(converter.convertServerTimeRawToReal(request.getServerTimeRaw()))
    symbolPriceTickerReal = converter.convertSymbolPriceTickerRawToReal(request.getSymbolPriceTickerRaw("LTCBTC"))
    print(symbolPriceTickerReal.symbol)
    print(symbolPriceTickerReal.price)
    currentAveragePriceReal = converter.convertCurrentAveragePriceRawToReal(request.getCurrentAveragePriceRaw("LTCBTC"))
    print(currentAveragePriceReal.mins)
    print(currentAveragePriceReal.price)

    klineList = []
    klineList = converter.convertKLineDataRawToReal(request.getCandleDataRaw("BTCUSDT", EInterval.ONE_HR))
    for candle in klineList:
        print("==============================")
        print("openTime: " + str(candle.openTime))
        print("open: " + str(candle.open))
        print("high: " + str(candle.high))
        print("low: " + str(candle.low))
        print("close: " + str(candle.close))
        print("volume: " + str(candle.volume))
        print("closeTime: " + str(candle.closeTime))
        print("quoteAssetVolume: " + str(candle.quoteAssetVolume))
        print("numberOfTrades: " + str(candle.numberOfTrades))
        print("takerBuyBaseAssetVolume: " + str(candle.takerBuyBaseAssetVolume))
        print("takerBuyQuoteAssetVolume: " + str(candle.takerBuyQuoteAssetVolume))
        print("ignore: " + str(candle.ignore))

simulateSystemBehavior()