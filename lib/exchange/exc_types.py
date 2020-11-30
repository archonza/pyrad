from enum import Enum

class ETypeOfData(Enum):
    PING = 0
    SERVER_TIME = 1
    SYMBOL_PRICE_TICKER = 2
    CURRENT_AVE_PRICE = 3
    CANDLE_DATA = 4
    UNDEFINED = 5

class EInterval(Enum):
    ONE_MIN = '1m'
    THREE_MIN = '3m'
    FIVE_MIN = '5m'
    FIFTEEN_MIN = '15m'
    THIRTY_MIN = '30m'
    ONE_HR = '1h'
    TWO_HR = '2h'
    FOUR_HR = '4h'
    SIX_HR = '6h'
    EIGHT_HR = '8h'
    TWELVE_HR = '12h'
    ONE_DAY = '1d'
    THREE_DAY = '3d'
    ONE_WEEK = '1w'
    ONE_MONTH = '1M'
    UNDEFINED = None

class SymbolPriceTicker:
    symbol: str
    price: float

class CurrentAveragePrice:
    mins: int
    price: float

class CandleData:
    openTime: int
    open: float
    high: float
    low: float
    close: float
    volume: float
    closeTime: int
    quoteAssetVolume: float
    numberOfTrades: int
    takerBuyBaseAssetVolume: float
    takerBuyQuoteAssetVolume: float
    ignore: float

class Ping:
    text: str

class ServerTime:
    timeStampMs: int

