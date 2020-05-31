import os
import time
import sys

os.system('echo "# ReCircle Startup" | sudo tee -a /etc/crontab')
#os.system('echo "@reboot sudo python3 /home/pi/RaspiReCircle/ReCircle.py &" | sudo tee -a /etc/crontab')

os.system('echo "# ReCircle Startup" | sudo tee -a /boot/config.txt')
os.system('echo "dtparam=spi=on" | sudo tee -a /boot/config.txt')
os.system('echo "dtoverlay=mcp2515-can0,oscillator=16000000,interrupt=25,spimaxfrequency=500000" | sudo tee -a /boot/config.txt')
os.system('echo "dtoverlay=spi-bcm2835-overlay" | sudo tee -a /boot/config.txt') 

os.chdir("/home/pi/RaspiReCircle/hardbyte-python-can-4085cffd2519/")
os.system("sudo python3 setup.py install") 

print("ReCircle setup is complete. A reboot is required to start CAN devices")
reboot_ans = input("Would you like to do that now? [y/N]: ")

if reboot_ans.lower() == 'y':
	os.system('reboot')
