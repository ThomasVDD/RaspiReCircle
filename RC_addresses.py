class RC_addresses:
    
    # Scan chamber
    Scan_chamber_Inductive_metal_detector = 500
    Scan_chamber_Capacitive_sensor = 480
    Scan_chamber_Barcode_scanner = 460
    Scan_chamber_Hyperspectral_camera = 440
    Scan_chamber_Matoha_NIR_spectrometer = 420
    Scan_chamber_Matoha_VIS_measurement = 400
    Scan_chamber_NeoSpectra_NIR_spectrometer = 380
    Scan_chamber_Motor_driver = 360
       
    # Wash chamber    
    Wash_chamber_Water_temperature_sensor = 760
    Wash_chamber_Flow_sensor = 740
    Wash_chamber_Air_pressure_sensor = 720
    Wash_chamber_Water_heater = 700
    Wash_chamber_Water_solvent_pump = 700
    Wash_chamber_Air_pump_dryer = 680
    Wash_chamber_Motor_driver = 660
    
    # Magazine
    Magazine_Photoelectric_sensor = 1500
    Magazine_Trash_chute_solenoid_lock = 1480
    Magazine_motor_drive = 1460
    
    # Inventory manager
    Photoelectric_sensor_glass_colourless = 1700
    Photoelectric_sensor_glass_green = 1695
    Photoelectric_sensor_glass_blue = 1690
    Photoelectric_sensor_glass_brown = 1685
    Photoelectric_sensor_cans = 1680
    Photoelectric_sensor_PET_colourless = 1660
    Photoelectric_sensor_PET_green = 1650
    Photoelectric_sensor_PET_blue = 1640
    Photoelectric_sensor_PET_brown = 1630
    Photoelectric_sensor_HDPE_white = 1620
    Photoelectric_sensor_HDPE_colour = 1610
    Photoelectric_sensor_PP = 1600
    Photoelectric_sensor_PS = 1590
    Photoelectric_sensor_waste_bay = 1580    
    
    Chute_actuator = 1560
    Bay_unlock_solenoid = 1540
    
    # Central
    User_buttons = 250
    Cellular_modem = 230
    Display = 200
    User_LEDs =	190
    

    def __init__(self):
        pass       
    
#######################################################################################################
        
if __name__ == "__main__":
    print("Cannot call RC_addresses.py as main")