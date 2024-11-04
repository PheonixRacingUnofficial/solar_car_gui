# BatteryImplement.py

import time
from Battery import Battery


def run_battery_test():
    # Starting battery level
    # Replace with initial battery input
    battery_level = 100
    app = Battery(battery_level)

    # Replace with battery input
    test_levels = [100, 80, 60, 40, 20, 10, 5, 0, 100]

    # Method to update battery with battery input
    def update_levels():
        for level in test_levels:
            app.update_battery(level)
            app.update_idletasks()  # Update the Tkinter window
            time.sleep(2)  # Pause for 2 seconds

    # Start the test after 1 second to allow window setup
    app.after(1000, update_levels)
    app.mainloop()


if __name__ == "__main__":
    run_battery_test()
