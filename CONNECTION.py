import time
import sys
import os

sys.path.append("../RaspiWifi/libs/reset_device")
import reset_lib

no_conn_counter = 0
consecutive_active_reports = 0

# Main connection monitoring loop at 10 second interval
while True:
	time.sleep(10)

	# If iwconfig report no association with an AP add 10 to the "No
	# Connection Couter"
	if reset_lib.is_wifi_active() == False:
		no_conn_counter += 10
		consecutive_active_reports = 0
	# If iwconfig report association with an AP add 1 to the
	# consecutive_active_reports counter and 10 to the no_conn_counter
	else:
		consecutive_active_reports += 1
		no_conn_counter += 10
		# Since wpa_supplicant seems to breifly associate with an AP for
		# 6-8 seconds to check the network key the below will reset the
		# no_conn_counter to 0 only if two 10 second checks have come up active.
		if consecutive_active_reports >= 2:
			no_conn_counter = 0
			consecutive_active_reports = 0

	# If the number of seconds not associated with an AP is greater or
	# equal to the auto_config_delay specified in the /etc/raspiwifi/raspiwifi.conf
	# trigger a reset into AP Host (Configuration) mode.
	if no_conn_counter >= 100:
		# no connection
		reset_lib.reset_to_host_mode()