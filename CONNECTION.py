import time
import sys
import os

sys.path.append("../RaspiWifi/libs/reset_device")
import reset_lib

no_conn_counter = 0
consecutive_active_reports = 0

def checkConnection():
	return reset_lib.is_wifi_active()
	
	
def resetConnection():
	reset_lib.reset_to_host_mode()