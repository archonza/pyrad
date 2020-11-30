# Imports
from typing import List
from exc_request import *
from exc_types import *

class Converter:
    def convertPingRawToReal(self, raw: dict) -> str:
        return json.dumps(raw)

    def convertServerTimeRawToReal(self, raw: dict) -> int:
        return raw['serverTime']

    def convertSymbolPriceTickerRawToReal(self, raw: dict) -> SymbolPriceTicker:
        response = SymbolPriceTicker()
        response.symbol = raw['symbol']
        response.price = raw['price']
        return response

    def convertCurrentAveragePriceRawToReal(self, raw: dict) -> CurrentAveragePrice:
        response = CurrentAveragePrice()
        response.mins = raw['mins']
        response.price = raw['price']
        return response

    def convertKLineDataRawToReal(self, raw: dict) -> List[CandleData]:
        responseList = []

        for i in range(len(raw)):
            response = CandleData()
            response.openTime = raw[i][0]
            response.open = float(raw[i][1])
            response.high = float(raw[i][2])
            response.low = float(raw[i][3])
            response.close = float(raw[i][4])
            response.volume = float(raw[i][5])
            response.closeTime = raw[i][6]
            response.quoteAssetVolume = float(raw[i][7])
            response.numberOfTrades = raw[i][8]
            response.takerBuyBaseAssetVolume = float(raw[i][9])
            response.takerBuyQuoteAssetVolume = float(raw[i][10])
            response.ignore = raw[i][11]
            responseList.append(response)
        return responseList
