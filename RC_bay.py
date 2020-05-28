import logging
from RC_addresses import *

class RC_bay:

    def __init__(self, CANobject, ID, material, color, name):
        logging.debug('Initializing RC_bay')
        
        self.CANobject = CANobject 
        self.CAN_ID = ID
        self.level = 0.2
        self.material = material
        self.color = color
        self.name = name
        
    def getLevel(self):
        self.CANobject.send(self.CAN_ID, [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        value = self.CANobject.getMessage(self.CAN_ID, 0.2)
        if value is not None:
            input = value.split()
            logging.debug(0.01*int(input[7], 16))
            return (0.01*int(input[7], 16))
        else:
            return 0

def makeBays(CANobject):
    logging.debug('making bays')
    
    bays = []
    
    bays.append(RC_bay(CANobject, RC_addresses.Photoelectric_sensor_glass_colourless, 'GLASS', 'BLUE', 'GLASS TRANS'))
    bays.append(RC_bay(CANobject, RC_addresses.Photoelectric_sensor_PET_green,        'PET', 'GREEN', 'PET GREEN'))
    bays.append(RC_bay(CANobject, RC_addresses.Photoelectric_sensor_PP,               'PP', 'RED', 'PP'))
    
    return bays

def pollBays(bays):
    logging.debug('polling bays')
    for bay in bays:
        bay.level = bay.getLevel()
        #if(bay.level<1):
            #bay.level += 0.1
        #if(bay.level>=1):
            #bay.level = 0

#######################################################################################################
        
if __name__ == "__main__":
    print("Cannot call RC_bay.py as main")