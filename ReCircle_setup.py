import os
import time
import sys

os.system('echo "# ReCircle Startup" | sudo tee -a /etc/crontab')
os.system('echo "@reboot sudo python3 /usr/ReCircle/ReCircle.py &" | sudo tee -a /etc/crontab')

