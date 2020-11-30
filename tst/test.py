# Imports
from lib.exchange.tst.test_request import *
from lib.exchange.tst.test_converter import *

def testExchangeIF():
    testGetPingRaw()
    testGetServerTimeRaw()
    testGetSymbolPriceTickerRaw()
    testGetCurrentAveragePriceRaw()

def testConverter():
    testConvertPingRawToReal()
    testConvertServerTimeRawToReal()
    testConvertSymbolPriceTickerRawToReal()
    testConvertCurrentAveragePriceRawToReal()

def executeTests():
    testExchangeIF()
    testConverter()
