import logging

class RC_actuator:

    def __init__(self, CANobject, ID):
        logging.debug('Initializing RC_actuator')
        
        self.CANobject = CANobject 
        self.CAN_ID = ID

    def turnMotor(self, direction):
        self.CANobject.send(self.CAN_ID, [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, direction])
        
    def turnMotorTime(self, time, speed, direction):
        self.CANobject.send(self.CAN_ID, [0x00, 0x00, 0x00, 0x00, 0x00, time, speed, direction])
        
    def turnMotorRevs(self, revs, direction):
        self.CANobject.send(self.CAN_ID, [0x00, 0x00, 0x00, 0x00, revs, 0x00, speed, direction])
        
    def switchSolenoid(self, time, status):
        self.CANobject.send(self.CAN_ID, [0x00, 0x00, 0x00, 0x00, 0x00, time, 0x00, status])
        
    def setMaxCurrent(self, current):
        current = current.to_bytes(2, 'big')
        self.CANobject.send(self.CAN_ID, [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, current[0], currrent[1]])
        
    def show(self, line, text):
        msg = []
        index = 0
        part = 0
        
        # Split text into chars and convert to ascii
        for letter in text:
            msg.append(ord(letter))
            index += 1
            
            if index == 8:
                self.CANobject.send(self.CAN_ID + 2*line+part, msg)
                msg = []
                index = 0
                part += 1
                
        # Pad with spaces and convert to ascii
        for letter in range (8-abs(len(text) - 8*part)):
            msg.append(ord(' '))
            index += 1
            if index == 8:
                self.CANobject.send(self.CAN_ID + 2*line+part, msg)
            
#######################################################################################################
        
if __name__ == "__main__":
    print("Cannot call RC_actuator.py as main") 