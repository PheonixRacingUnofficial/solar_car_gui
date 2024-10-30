import time
from tkinter import Tk
from Speedometer import Speedometer  # Assuming Speedometer is defined in speedometer_module.py

# Constants
wheel_diameter_inches = 16.0
pi = 3.14159
pulses_per_rotation = 16

# Initialize the Tkinter root and Speedometer
root = Tk()
speedometer = Speedometer(root)

# Function to calculate pulse interval based on speed
# Function to calculate pulse interval based on speed
def calculate_pulse_interval(mph):
    wheel_circumference_inches = pi * wheel_diameter_inches
    inches_per_minute = (mph * 63360) / 60.0  # Convert mph to inches per minute
    rpm = inches_per_minute / wheel_circumference_inches
    pulses_per_minute = rpm * pulses_per_rotation

    # Avoid division by zero by setting a minimum threshold
    if pulses_per_minute < 0.01:
        pulses_per_minute = 0.01  # Arbitrary small value to avoid zero division

    pulse_interval = (60.0 / pulses_per_minute) * 1000000.0
    return pulse_interval


# Function to simulate speed change and update the speedometer
def simulate_speed_change(speed=0):
    speedometer.update_speed(speed)  # Update the GUI speedometer
    pulse_interval_micros = calculate_pulse_interval(speed)  # Update pulse interval based on speed

    print(f"Speed: {speed:.2f} MPH | Pulse interval: {pulse_interval_micros:.2f} microseconds")

    # Increment speed and reset if it exceeds max speed
    speed = (speed + 0.01) % (speedometer.max_speed + 1)
    root.after(1, simulate_speed_change, speed)  # Continuously update every 1 ms

# Start the simulation
simulate_speed_change()
root.mainloop()
