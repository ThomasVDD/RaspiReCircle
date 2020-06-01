import can
import time
import os
import sys
import threading
import logging

class CAN:

    RPI = True
    SHUTDOWN = False
    ERROR = 0x01

    def __init__(self):
            logging.info('Initializing CAN0')            
            
            if (sys.platform == 'win32'):
                CAN.RPI = False
                logging.info('Windows detected')
            else: 
                CAN.RPI = True
                logging.info('RPi detected')

            try:
                if CAN.RPI:
                    os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
                    time.sleep(0.1)                     
                    self.bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
                self.CAN_ID = 0
                self.CAN_message = 0
                self._lock = threading.Lock()
            except OSError:
                logging.error('Cannot find PiCAN board.')
                exit()
                
            logging.info('Initialized CAN0')
     
    # Receives CAN messages by polling the bus: BLOCKING function in own thread 
    def receive(self):
            while (not CAN.SHUTDOWN) and CAN.RPI:
                # Wait (blocking!) until a message is received.
                message = self.bus.recv()   

                c = '{0:x} - {1:x} - '.format(message.arbitration_id, message.dlc)
                s = ''
                for i in range(message.dlc):
                    s +=  '{0:x} '.format(message.data[i])
                logging.info('CAN RX: {}'.format(c+s))
                    
                if message.arbitration_id == self.ERROR:
                    print('ERROR MESSAGE ON CAN BUS')
                    
                with self._lock:
                    self.CAN_message = s
                    self.CAN_ID = message.arbitration_id
    
    # Gets CAN message from specified ID with timeout
    def getMessage(self, ID, timeout):
        timeout = time.time() + timeout
        while time.time() < timeout:
            if self.CAN_ID == ID:
                with self._lock:
                    # reset to 0x00 for next compare
                    self.CAN_ID = 0x00      
                    return self.CAN_message
                    
    # Send CAN message to specified ID           
    def send(self, ID, message):
        c = '{0:x} - {1:x} - '.format(ID, len(message))
        s = ''
        for i in range(len(message)):
            s +=  '{0:x} '.format(int(message[i]))        
        logging.info('CAN TX: {}'.format(c+s))
  
        if CAN.RPI:  
            msg = can.Message(arbitration_id=ID,data=message,extended_id=False)
            self.bus.send(msg)  
        
        time.sleep(0.1)

#######################################################################################################
        
if __name__ == "__main__":
    print("Cannot call CAN.py as main")