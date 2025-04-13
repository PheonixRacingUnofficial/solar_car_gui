from src.solar_car_gui.SpeedometerGenerator import Speedometer 
from src.solar_car_gui.Battery import Battery
from src.solar_car_gui.Wattage import Wattage

from tkinter import Tk, Frame
import logging

logger = logging.getLogger(__name__)

class Gui:
    def __init__(self, speed=0, battery_level=0, wattage_level=0):
        self.root = Tk()
        self.root.title("Solar Car Dashboard")

        # Main container for layout
        self.container = Frame(self.root)
        self.container.pack(padx=20, pady=20)

        # Wrap Speedometer in a Frame
        self.speed_frame = Frame(self.container)
        self.speed_frame.pack(side="left", padx=10)
        self.speedometer = Speedometer(self.speed_frame)
        self.speedometer.pack() if hasattr(self.speedometer, "pack") else None
        self.speed = speed

        # Wrap Battery in a Frame
        self.battery_frame = Frame(self.container)
        self.battery_frame.pack(side="left", padx=10)
        self.battery = Battery(self.battery_frame, battery_level)
        self.battery.pack() if hasattr(self.battery, "pack") else None
        self.batteryCharge = battery_level

        # Wrap Wattage in a Frame
        self.wattage_frame = Frame(self.container)
        self.wattage_frame.pack(side="left", padx=10)
        self.wattage = Wattage(self.wattage_frame)
        self.wattage.pack() if hasattr(self.wattage, "pack") else None
        self.wattagePercent = wattage_level

    def update_speed(self, speed):
        logger.info("Updated GUI Speed: " + str(speed))
        self.speedometer.update_speed(speed)
        self.speed = speed

    def update_battery(self, battery_level):
        logger.info("Updated GUI Battery: " + str(battery_level))
        self.battery.update_battery(battery_level)
        self.batteryCharge = battery_level

    def update_wattage(self, wattage_level):
        logger.info("Updated GUI Wattage: " + str(wattage_level))
        self.wattage.update_wattage(wattage_level)
        self.wattagePercent = wattage_level
