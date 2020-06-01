import logging

class RC_sensor:
    
    def __init__(self, CANobject, ID):
        logging.debug('Initializing RC_sensor')
        
        self.CANobject = CANobject 
        self.CAN_ID = ID

    def getTemperature(self):
        self.CANobject.send(self.CAN_ID, [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        value = self.CANobject.getMessage(self.CAN_ID, 2)
        if value is not None:
            temp = value.split()
            return (int(temp[0], 16))
        
    def setMaxTemperature(temperature):
        self.CANobject.send(self.CAN_ID, [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, temperature])
        
    def getMaterialInput(self):
        self.CANobject.send(self.CAN_ID, [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        value = self.CANobject.getMessage(self.CAN_ID, 2)
        if value is not None:
            input = value.split()
            return (int(input[0], 16))
        
    def getMaterialType(self):
        self.CANobject.send(self.CAN_ID, [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        value = self.CANobject.getMessage(self.CAN_ID, 2)
        if value is not None:
            input = value.split()
            return (int(input[0], 16))    
            
    def getFlow(self):
        self.CANobject.send(self.CAN_ID, [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        value = self.CANobject.getMessage(self.CAN_ID, 2)
        if value is not None:
            temp = value.split()
            return (int(temp[0], 16))
        
    def setMaxFlow(flow):
        self.CANobject.send(self.CAN_ID, [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, flow])   
        
    def getPressure(self):
        self.CANobject.send(self.CAN_ID, [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        value = self.CANobject.getMessage(self.CAN_ID, 2)
        if value is not None:
            temp = value.split()
            return (int(temp[0], 16))
        
    def setMaxPressure(pressure):
        self.CANobject.send(self.CAN_ID, [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, pressure])   

    def getWeight(self):
        self.CANobject.send(self.CAN_ID, [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        value = self.CANobject.getMessage(self.CAN_ID, 2)
        if value is not None:
            temp = value.split()
            return (int(temp[0], 16))
        
    def setMaxWeight(weight):
        self.CANobject.send(self.CAN_ID, [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, weight])  
        
    def getButtonPress():
        self.CANobject.send(self.CAN_ID, [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        value = self.CANobject.getMessage(self.CAN_ID, 2)
        if value is not None:
            button = value.split()
            return (int(button[0], 16))        

#######################################################################################################
        
if __name__ == "__main__":
    print("Cannot call RC_sensor.py as main")