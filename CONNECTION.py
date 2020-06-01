import time
import sys
import os

sys.path.append("/home/pi/RaspiWifi/libs/reset_device")
import reset_lib

def checkConnection():
	return reset_lib.is_wifi_active()
	
def resetConnection():
	reset_lib.reset_to_host_mode()