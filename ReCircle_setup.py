import os
import time
import sys

os.system('echo "# ReCircle Startup" | sudo tee -a /etc/crontab')
os.system('echo "@reboot sudo python3 /home/pi/RaspiReCircle/ReCircle.py &" | sudo tee -a /etc/crontab')

os.system('echo "# ReCircle Startup" | sudo tee -a /boot/config.txt')
os.system('echo "dtparam=spi=on" | sudo tee -a /boot/config.txt')
os.system('echo "dtoverlay=mcp2515-can0,oscillator=16000000,interrupt=25,spimaxfrequency=500000" | sudo tee -a /boot/config.txt')
os.system('echo "dtoverlay=spi-bcm2835-overlay" | sudo tee -a /boot/config.txt') 