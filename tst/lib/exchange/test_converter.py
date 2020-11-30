# Imports
import sys
import os
base_dir = os.path.dirname(__file__) or '.'
# Import exchange functionality
exchange_dir = os.path.join(base_dir, '..\..\..\lib\exchange')
sys.path.insert(1, exchange_dir)
from exc_converter import *

def testConvertPingRawToReal():
    print("TODO")

def testConvertServerTimeRawToReal():
    print("TODO")

def testConvertSymbolPriceTickerRawToReal():
    print("TODO")

def testConvertCurrentAveragePriceRawToReal():
    print("TODO")