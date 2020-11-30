import sys
import os

base_dir = os.path.dirname(__file__) or '.'

# Import exchange functionality
exchange_dir = os.path.join(base_dir, '..\..\..\lib\exchange')
sys.path.insert(1, exchange_dir)
from exc_request import *


request = Request()

# ---------------------------------------------------------------------------------------
# \name         : testGetPingRaw
#
# \brief        : This function tests getPingRaw().
#
# \requirements : This function shall 
#    \req       : verify whether data returned from getPingRaw is of type 'dict'.
#    \req       : verify whether the value returned from getPingRaw equals '{}'.
#
# \parameters   : [type] [[dir]] : [value] - [Description].
#    \par       : void [in] : none - No parameters.
#
# \return       : [type] : [value] - [Description].
#    \ret       : bool : True - The test passed.
#    \ret       : bool : False - The test failed.
# ---------------------------------------------------------------------------------------
def testGetPingRaw() -> bool:
    data = request.getPingRaw()
    # Verify that type is dict
    if (isinstance(data, dict) == True):
        # Verify that the serialized value returned equals '{}'
        if (json.dumps(data) == "{}"):
            return True
        else:
            print("ERROR: ActualValue: " + json.dumps(data) + " ExpectedValue: {}")
    else:
        print("ERROR: ActualType: " + str(type(data)) + " ExpectedType: <class 'dict'>")
    return False

# ---------------------------------------------------------------------------------------
# \name         : testGetPingRaw
#
# \brief        : This function tests getServerTimeRaw().
#
# \requirements : This function shall 
#    \req       : verify whether data returned from getServerTimeRaw is of type 'dict'.
#    \req       : verify whether the value returned from getServerTimeRaw is greater
#                 than 0.
#
# \parameters   : [type] [[dir]] : [value] - [Description].
#    \par       : void [in] : none - No parameters.
#
# \return       : [type] : [value] - [Description].
#    \ret       : bool : True - The test passed.
#    \ret       : bool : False - The test failed.
# ---------------------------------------------------------------------------------------
def testGetServerTimeRaw() -> bool:
    data = request.getServerTimeRaw()
    # Verify that type is dict
    if (isinstance(data, dict) == True):
        # Verify that the serialized value returned is > 0 and 
        if (data['serverTime'] > 0):
            return True
        else:
            print("ERROR: ActualValue: " + str(data['serverTime']) + " ExpectedValue: value should be > 0")
    else:
        print("ERROR: ActualType: " + str(type(data)) + " ExpectedType: <class 'dict'>")
    return False

def testGetSymbolPriceTickerRaw():
    print("TODO")

def testGetCurrentAveragePriceRaw():
    print("TODO")