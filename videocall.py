# coding=utf8
'''''
@author: zobov
'''

import pyVideoSDK
from pyVideoSDK.methods import Methods
from pyVideoSDK.consts import EVENT, METHOD
import pyVideoSDK.consts as C
import config

sdk = pyVideoSDK.open_session(ip = config.IP, port = config.PORT, pin = config.PIN, debug = False)
methods = Methods(sdk)

@sdk.handler(EVENT[C.EV_appStateChanged])
@sdk.handler(METHOD[C.M_getAppState])
def on_state_change(response):
    print(f'    @@@ {response["appState"]}')

if __name__ == '__main__':
    methods.call("echotest@trueconf.com")
    sdk.run()