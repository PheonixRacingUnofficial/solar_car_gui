# BatteryTest.py

from Battery import Battery


def run_battery_test():
    # Starting battery level
    battery_level = 60
    app = Battery(battery_level)
    app.mainloop()


if __name__ == "__main__":
    run_battery_test()
