import time
from tkinter import Tk
from Speedometer import Speedometer  # Assuming you saved your code as `speedometer_module.py`

# Initialize the Tkinter root and Speedometer
root = Tk()
speedometer = Speedometer(root)


# Function to update speed
def simulate_speed_change(speed=0):
    # Continuously update speed in increments, then reset
    speedometer.update_speed(speed)
    speed = (speed + 0.01) % (speedometer.max_speed + 1)  # Loop back to 0 when max_speed is exceeded
    root.after(1, simulate_speed_change, speed)  # Update every 500 ms


# Start the simulation
simulate_speed_change()
root.mainloop()
