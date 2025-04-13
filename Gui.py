from src.solar_car_gui.SpeedometerGenerator import Speedometer
from src.solar_car_gui.Battery.py import Battery
from src.solar_car_gui.Wattage.py import Wattage

from tkinter import Tk
import logging

logger = logging.getLogger(__name__)

class Gui:
        def __init__(self, speed, battery_level, wattage_level):
                self.root = Tk()
                self.speedometer = Speedometer(self.root)
                self.speed = speed
                self.battery = Battery(self.root)
                self.batteryCharge = battery_level
                self.wattage = Wattage(self.root)
                self.wattagePercent = wattage_level

        def update_speed(self, speed):
                logger.info("Updated GUI Speed:" + str(speed))
                self.speedometer.update_speed(speed)
                self.speed = speed
        def update_battery(self, battery_level):
                logger.info("Updated GUI Battery:" + str(battery_level))
                self.speedometer.update_battery(battery_level)
                self.battery = battery_level
        def update_wattage(self, wattage_level):
                logger.info("Updated GUI Wattage:" + str(wattage_level))
                self.speedometer.update_wattage(wattage_level)
                self.wattage = wattage_level
        

