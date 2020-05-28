import tkinter as tk
from tkinter import filedialog, Text
from PIL import Image, ImageTk

import os
import time
import threading
import logging

from CAN import CAN
from ReCircle import ReCircle
from RC_addresses import RC_addresses

class GUI:

    HEIGHT = 480
    WIDTH  = 800
    
    def __init__(self, master, CANobject, ReCircleobject):
        logging.info('Starting GUI')
        
        self.CANobject = CANobject
        self.ReCircleobject = ReCircleobject
        
        self.currstatus = None
        self.prevstatus = None
        
        # CREATE GUI
        
        self.master = master
        master.title('ReCircle')
        
        canvas = tk.Canvas(self.master, height=self.HEIGHT, width=self.WIDTH, bg="green")
        canvas.pack()
        
        background_image = tk.PhotoImage(file = "Images/landscape.png")
        background_label = tk.Label(self.master, image = background_image)
        background_label.image = background_image
        background_label.place(relwidth = 1, relheight = 1)
        
        self.frame = tk.Frame(self.master, bg = "white")
        self.frame.place(relheight = 0.9, relwidth = 0.9, relx = 0.05, rely = 0.05)
        
        # ADD BUTTONS, LABELS
        
        self.lblState = tk.Label(self.frame, text = "This is the state label", fg = 'blue')
        self.lblState.place(relx = 0.5, rely = 0, relwidth = 0.5, relheight = 0.1,  anchor = 'n')
        
        self.frame.update()
        self.sizex = int(self.frame.winfo_width()*0.5)
        self.sizey = int(self.frame.winfo_height()*0.4)
       
        self.state_image = ImageTk.PhotoImage(Image.open('Images/landscape.png').resize((self.sizex,self.sizey)))
        self.lblStatePic = tk.Label(self.frame, image = self.state_image)
        self.lblStatePic.image = self.state_image
        self.lblStatePic.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.4)
        
        self.btnStart = tk.Button(self.frame, text="Start", fg = "white", bg = "green", command = self.start)
        self.btnStart.place(relx = 0, rely = 0.1, relwidth = 0.25, relheight = 0.4)
        
        self.btnStop = tk.Button(self.frame, text="Stop", fg = "white", bg = "red", command = self.stop)
        self.btnStop.place(relx = 0.75, rely = 0.1, relwidth = 0.25, relheight = 0.2)

        self.btnQuit = tk.Button(self.frame, text="Quit", fg = "white", bg = "red", command = self.quit)
        self.btnQuit.place(relx = 0.75, rely = 0.3, relwidth = 0.25, relheight = 0.2)
        
        # ADD INVENTORY MANAGER
        
        self.inventoryframe = tk.Frame(self.master, bg = "black", bd = 5)
        self.inventoryframe.place(relheight = 0.4, relwidth = 0.9, relx = 0.05, rely = 0.55)
        self.update()
        
        bays = self.ReCircleobject.getBays()
        bay_total = len(bays)
        bay_number = 0        
        for bay in bays:
            bay_i_body_label = tk.Label(self.inventoryframe, bg = "white", borderwidth = 5, relief = "solid")
            bay_i_body_label.place(relx = bay_number/bay_total, rely = 0.2, relwidth = 1/bay_total, relheigh = 0.8)
            
            bay_i_text_label = tk.Label(self.inventoryframe, bg = "white", borderwidth = 5, relief = "solid", text = bay.name)
            bay_i_text_label.place(relx = bay_number/bay_total, rely = 0, relwidth = 1/bay_total, relheigh = 0.2)
            
            bay_i_level_label = tk.Label(self.inventoryframe, bg = bay.color, borderwidth = 5, relief = "solid")
            bay_i_level_label.place(relx = bay_number/bay_total, rely = 1 - 0.8*bay.level, relwidth = 1/bay_total, relheigh = 0.8*bay.level)
            
            bay_number += 1        

    # GUI functions
    
    def start(self):
        print("Starting program")
        self.btnStart.config(state="disabled")
        self.lblState.config(fg = 'green')

    def stop(self):
        print("Stopping program")
        self.btnStart.config(state="normal")
        #self.CANobject.send()

    def quit(self):
        print("Quitting program")
        CAN.SHUTDOWN = True
        self.master.destroy()

    def ask_quit(self):
        print("Quitting program")
        CAN.SHUTDOWN = True
        self.master.destroy()
        
    def update(self):
        print("updating GUI")
        self.currstatus = self.ReCircleobject.STATUS
        
        # Draw status
        if self.currstatus != self.prevstatus:
            self.lblState.config(text = self.currstatus)
            self.state_image = ImageTk.PhotoImage(Image.open('Images/' + self.ReCircleobject.STATUS + '.png').resize((self.sizex,self.sizey)))
            self.lblStatePic = tk.Label(self.frame, image = self.state_image) 
            self.lblStatePic.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.4)
        self.prevstatus = self.currstatus

        # Draw material bay
        bays = self.ReCircleobject.pollBays()
        bay_total = len(bays)
        bay_number = 0        
        for bay in bays:
            bay_i_body_label = tk.Label(self.inventoryframe, bg = "white", borderwidth = 5, relief = "solid")
            bay_i_body_label.place(relx = bay_number/bay_total, rely = 0.2, relwidth = 1/bay_total, relheigh = 0.8)
            
            bay_i_text_label = tk.Label(self.inventoryframe, bg = "white", borderwidth = 5, relief = "solid", text = bay.name)
            bay_i_text_label.place(relx = bay_number/bay_total, rely = 0, relwidth = 1/bay_total, relheigh = 0.2)
            
            bay_i_level_label = tk.Label(self.inventoryframe, bg = bay.color, borderwidth = 5, relief = "solid")
            bay_i_level_label.place(relx = bay_number/bay_total, rely = 1 - 0.8*bay.level, relwidth = 1/bay_total, relheigh = 0.8*bay.level)
            
            bay_number += 1

        self.master.after(10000, self.update)

#######################################################################################################
        
def CAN_makethread(CANobject):
    CANobject.receive()
    print('CAN thread stopped')
    
def ReCircle_makethread(ReCircleobject):
    ReCircleobject.maincontroller()
    print('ReCircle thread stopped')

# Initialisation: create thread for CAN and ReCircle, launch GUI
def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("debug.log"),
            logging.StreamHandler()
        ]
    ) 
    logging.info("")
    logging.info("Executing ReCircle machine control script...")        
    
    CANobject = CAN()
    t1 = threading.Thread(target = CAN_makethread, args = (CANobject,))
    t1.start()
    
    ReCircleobject = ReCircle(CANobject)
    t2 = threading.Thread(target = ReCircle_makethread, args = (ReCircleobject,))
    t2.start()
    
    root = tk.Tk()
    app = GUI(root, CANobject, ReCircleobject)
    root.protocol("WM_DELETE_WINDOW", app.ask_quit)
    root.after(1000, app.update)
    root.mainloop()
        
# Run main function upon startup with GUI
if __name__ == "__main__":
    print("Calling main function")
    main()