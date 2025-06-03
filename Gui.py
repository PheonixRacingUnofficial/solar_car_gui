from src.Battery import Battery
from src.Wattage import Wattage

from tkinter import Tk, Frame
import logging

logger = logging.getLogger(__name__)

class Gui:
    def __init__(self, battery_level=0, wattage_level0=0, wattage_level1=0, wattage_level2=0, wattage_level3=0, wattage_level4=0, wattage_level5=0, wattage_level6=0):
        self.root = Tk()
        self.root.title("Solar Car Dashboard")

        # Main container for layout
        self.container = Frame(self.root)
        self.container.pack(padx=20, pady=20)

        # Wrap Battery in a Frame
        self.battery_frame = Frame(self.container)
        self.battery_frame.grid(row=0, column=0)
        self.battery = Battery(self.battery_frame, battery_level)
        self.battery.pack() if hasattr(self.battery, "pack") else None
        self.batteryCharge = battery_level

        # Wrap Wattage in a Frame
        self.wattage_frame = Frame(self.container)
        self.wattage_frame.grid(row=0, column=1)
        self.wattage = Wattage(self.wattage_frame)
        self.wattage.pack() if hasattr(self.wattage, "pack") else None
        self.wattagePercent = wattage_level0

        # Wrap Wattage in a Frame
        self.wattage_frame = Frame(self.container)
        self.wattage_frame.grid(row=0, column=2)
        self.wattage = Wattage(self.wattage_frame)
        self.wattage.pack() if hasattr(self.wattage, "pack") else None
        self.wattagePercent = wattage_level1      

        # Wrap Wattage in a Frame
        self.wattage_frame = Frame(self.container)
        self.wattage_frame.grid(row=0, column=3)
        self.wattage = Wattage(self.wattage_frame)
        self.wattage.pack() if hasattr(self.wattage, "pack") else None
        self.wattagePercent = wattage_level2   

        # Wrap Wattage in a Frame
        self.wattage_frame = Frame(self.container)
        self.wattage_frame.grid(row=1, column=0)
        self.wattage = Wattage(self.wattage_frame)
        self.wattage.pack() if hasattr(self.wattage, "pack") else None
        self.wattagePercent = wattage_level3   

        # Wrap Wattage in a Frame
        self.wattage_frame = Frame(self.container)
        self.wattage_frame.grid(row=1, column=1)
        self.wattage = Wattage(self.wattage_frame)
        self.wattage.pack() if hasattr(self.wattage, "pack") else None
        self.wattagePercent = wattage_level4   

        # Wrap Wattage in a Frame
        self.wattage_frame = Frame(self.container)
        self.wattage_frame.grid(row=1, column=2)
        self.wattage = Wattage(self.wattage_frame)
        self.wattage.pack() if hasattr(self.wattage, "pack") else None
        self.wattagePercent = wattage_level5

        # Wrap Wattage in a Frame
        self.wattage_frame = Frame(self.container)
        self.wattage_frame.grid(row=1, column=3)
        self.wattage = Wattage(self.wattage_frame)
        self.wattage.pack() if hasattr(self.wattage, "pack") else None
        self.wattagePercent = wattage_level6                            

    def update_battery(self, battery_level):
        logger.info("Updated GUI Battery: " + str(battery_level))
        self.battery.update_battery(battery_level)
        self.batteryCharge = battery_level

    def update_wattage(self, wattage_level0):
        logger.info("Updated GUI Wattage: " + str(wattage_level0))
        self.wattage.update_wattage(wattage_level0)
        self.wattagePercent = wattage_level0

    def update_wattage(self, wattage_level1):
        logger.info("Updated GUI Wattage: " + str(wattage_level1))
        self.wattage.update_wattage(wattage_level1)
        self.wattagePercent = wattage_level1

    def update_wattage(self, wattage_level2):
        logger.info("Updated GUI Wattage: " + str(wattage_level2))
        self.wattage.update_wattage(wattage_level2)
        self.wattagePercent = wattage_level2

    def update_wattage(self, wattage_level3):
        logger.info("Updated GUI Wattage: " + str(wattage_level3))
        self.wattage.update_wattage(wattage_level3)
        self.wattagePercent = wattage_level3

    def update_wattage(self, wattage_level4):
        logger.info("Updated GUI Wattage: " + str(wattage_level4))
        self.wattage.update_wattage(wattage_level4)
        self.wattagePercent = wattage_level4

    def update_wattage(self, wattage_level5):
        logger.info("Updated GUI Wattage: " + str(wattage_level5))
        self.wattage.update_wattage(wattage_level5)
        self.wattagePercent = wattage_level5

    def update_wattage(self, wattage_level6):
        logger.info("Updated GUI Wattage: " + str(wattage_level6))
        self.wattage.update_wattage(wattage_level6)
        self.wattagePercent = wattage_level6
