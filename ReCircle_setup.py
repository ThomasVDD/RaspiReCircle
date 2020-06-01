import os
import time
import sys

# change CAN settings
os.system('echo "# ReCircle Startup" | sudo tee -a /boot/config.txt')
os.system('echo "dtparam=spi=on" | sudo tee -a /boot/config.txt')
os.system('echo "dtoverlay=mcp2515-can0,oscillator=16000000,interrupt=25,spimaxfrequency=500000" | sudo tee -a /boot/config.txt')
os.system('echo "dtoverlay=spi-bcm2835-overlay" | sudo tee -a /boot/config.txt') 
# install CAN library
os.chdir("/home/pi/RaspiReCircle/hardbyte-python-can-4085cffd2519/")
os.system("sudo python3 setup.py install") 
# launch ReCircle script at boot
os.chdir("/home/pi/")
os.system("sudo apt-get install xterm -y")
os.system("cp /home/pi/RaspiReCircle/ReCircle.desktop /home/pi/.config/autostart")

print("ReCircle setup is complete. A reboot is required to start CAN devices")
reboot_ans = input("Would you like to do that now? [y/N]: ")

if reboot_ans.lower() == 'y':
	os.system('reboot')
