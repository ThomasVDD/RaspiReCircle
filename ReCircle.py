from CAN import CAN
from CONNECTION import * 
from RC_sensor import RC_sensor
from RC_actuator import RC_actuator
from RC_addresses import *
from RC_bay import *

import sys
import threading
import logging
from time import sleep

class ReCircle:
    
    STATUS = "startup"
	CONNECTION_MODE = True
    
    def __init__(self, CANobject):
        logging.info('Initializing System')
        
        self.CANobject = CANobject
        
        logging.info('Initialized System')
		
		try: 
			connectionfile = file('/etc/cron.raspiwifi/')
			for line in connectionfile:
				if "app.py" in line:
					CONNECTION_MODE = False
					logging.info('Conection: host mode')
					break
					
			if 	CONNECTION_MODE == True:
				logging.info('Connection: client mode')
		except
			pass	
        
    def maincontroller(self):
        logging.info('Starting System')
        
        try:
            self.maincontrollerinit()
            while not CAN.SHUTDOWN:
                self.maincontrollerlogic()
        except KeyboardInterrupt:
            logging.info("Quitting program")
            CAN.SHUTDOWN = True
            sys.exit(0)
    
    def getBays(self):
        return self.bays
    
    def pollBays(self):
        pollBays(self.bays)
        return self.bays
    
#######################################################################################################    
################################################ SETUP ################################################
#######################################################################################################
    
    def maincontrollerinit(self):
        # Add declarations of sensors and actuators here
        self.materialsensor = RC_sensor(self.CANobject, RC_addresses.Magazine_Photoelectric_sensor)
        self.materialscanner = RC_sensor(self.CANobject, RC_addresses.Scan_chamber_Matoha_NIR_spectrometer)
        self.display = RC_actuator(self.CANobject, RC_addresses.Display)  
        self.MagazineMotor = RC_actuator(self.CANobject, RC_addresses.Scan_chamber_Motor_driver)
        
        self.motor1 = RC_actuator(self.CANobject, RC_addresses.Wash_chamber_Motor_driver)
        self.motor2 = RC_actuator(self.CANobject, RC_addresses.Scan_chamber_Motor_driver)
        self.tempsensor1 = RC_sensor(self.CANobject, RC_addresses.Wash_chamber_Water_temperature_sensor)        
        
        self.bays = makeBays(self.CANobject)
        self.chute = RC_actuator(self.CANobject, RC_addresses.Chute_actuator)
        self.solenoid = RC_actuator(self.CANobject, RC_addresses.Bay_unlock_solenoid)
        # Add initialization of sensors and actuators here
        pollBays(self.bays)
  
#######################################################################################################
################################################ LOOP #################################################
#######################################################################################################
              
    def maincontrollerlogic(self):
        # WAIT FOR INPUT
        self.STATUS = "Wait"
        self.display.show(0, self.STATUS)
        while(self.materialsensor.getMaterialInput() == 0):
            pass
        self.MagazineMotor.turnMotor(1)
        
        if checkConnection() == True && CONNECTION_MODE == True:
            self.display.show(0, 'WIFI CONN')
        else if checkConnection() == False && CONNECTION_MODE == True:
			self.display.show(0, 'WIFI NOT CONN')
		else:
            self.display.show(0, '1CONNECT TO WIFI')
            self.display.show(1, '2BROWSE 10.0.0.1')
        
        sleep(10)
        # IDENTIFY MATERIAL
        self.STATUS = "Identification"
        self.display.show(0, self.STATUS)
        while(self.materialscanner.getMaterialType() == 0):
            pass             
        
        # WASH
        
        # SHRED
        self.chute.switchSolenoid(2, 1)
        self.solenoid.switchSolenoid(20, 1)        
        
        # UPDATE MATERIAL BAY
        
        #self.motor1.turnMotor(0)
        sleep(0.1)
        self.motor2.turnMotor(1) 
        print(self.tempsensor1.getTemperature())
        sleep(3)
        self.STATUS = "sleeping"
        
        

#######################################################################################################

def CAN_makethread(CANobject):
    CANobject.receive()
    print('CAN thread stopped')
    
# Initialisation: create thread for CAN 
def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("/home/pi/RaspiReCircle/logs/debug.log"),
            logging.StreamHandler()
        ]
    ) 
    logging.info("")
    logging.info("Executing ReCircle machine control script...")   
    
    CANobject = CAN()
    t1 = threading.Thread(target = CAN_makethread, args = (CANobject,))
    t1.start()
    
    ReCircleobject = ReCircle(CANobject)
    ReCircleobject.maincontroller()  
        
# Run main function upon startup without GUI
if __name__ == "__main__":
    print("Calling main function")
    main()