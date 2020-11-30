# Imports
import requests
import string
import json
from exc_types import *

#from response import *

class Request:
    def __init__(self):
        print()

    def getPingRaw(self) -> dict:
        URL = "https://api.binance.com/api/v1/ping"
        r = requests.get(url = URL)
        if (r.status_code == 200):
            exchangeData = r.json()
            return exchangeData

    def getServerTimeRaw(self) -> dict:
        URL = "https://api.binance.com/api/v3/time"
        r = requests.get(url = URL)
        if (r.status_code == 200):
            exchangeData = r.json()
            return exchangeData

    def getSymbolPriceTickerRaw(self, symbol: str) -> dict:
        URL = "https://api.binance.com/api/v3/ticker/price"
        PARAMS = {'symbol':symbol}
        r = requests.get(url = URL, params= PARAMS)
        if (r.status_code == 200):
            exchangeData = r.json()
            return exchangeData

    def getCurrentAveragePriceRaw(self, symbol: str) -> dict:
        URL = "https://api.binance.com/api/v3/avgPrice"
        PARAMS = {'symbol':symbol}
        r = requests.get(url = URL, params= PARAMS)
        if (r.status_code == 200):
            exchangeData = r.json()
            return exchangeData

    def getCandleDataRaw(self, symbol: str, interval: EInterval, startTime: int = -1, endTime: int = -1, limit: int = -1) -> dict:
        URL = "https://api.binance.com/api/v3/klines"
        if ((startTime == -1) and 
            (endTime == -1) and 
            (limit == -1)):
            PARAMS = {
                'symbol':symbol,
                'interval': interval.value
            }
        elif ((startTime == -1) and 
            (endTime == -1) and 
            (limit != -1)):
            PARAMS = {
                'symbol':symbol,
                'interval': interval.value,
                'limit': limit
            }

        r = requests.get(url = URL, params= PARAMS)
        if (r.status_code == 200):
            exchangeData = r.json()
            return exchangeData

