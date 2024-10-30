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


def calculate_mph_from_pulses(pulse_count, interval_seconds):
    # Calculate wheel circumference in inches
    wheel_circumference_inches = pi * wheel_diameter_inches

    # Calculate rotations per interval based on pulse count
    rotations = pulse_count / pulses_per_rotation

    # Calculate inches traveled during interval
    distance_inches = rotations * wheel_circumference_inches

    # Convert inches per interval to inches per hour
    inches_per_hour = (distance_inches / interval_seconds) * 3600

    # Convert inches per hour to miles per hour (1 mile = 63,360 inches)
    mph = inches_per_hour / 63360
    return mph


def update_speedometer_with_pulses(pulse_count, interval_seconds=1):
    mph = calculate_mph_from_pulses(pulse_count, interval_seconds)
    speedometer.update_speed(mph)
    print(f"Speed: {mph:.2f} MPH")


def simulate_pulse_input():
    # Simulated pulse input example
    pulse_count = 20  # Replace with actual pulse count as received; will happen later
    update_speedometer_with_pulses(pulse_count, interval_seconds=1)
    root.after(1000, simulate_pulse_input)  # Repeat every second


# Start the simulation
simulate_pulse_input()
root.mainloop()
