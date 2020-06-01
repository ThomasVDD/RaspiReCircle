import time
import sys
import os

sys.path.append("/home/pi/RaspiWifi/libs/reset_device")
import reset_lib

def checkConnection():
	return reset_lib.is_wifi_active()
	
def resetConnection():
	os.system("sudo python3 /usr/lib/raspiwifi/reset_device/manual_reset.py")