#WattageImplement.py

from Wattage import Wattage
import time

def run_Wattage_test():
    # Starting battery level
    # Replace with initial battery input
    initial_value = 100
    app = Wattage(initial_value)

    # Replace with wattage input
    array_power = [100, 80, 60, 40, 20, 10, 5, 0, 100]

    # Method to update wattage with wattage input
    def update_levels():
        for power in array_power:
            app.update_wattage(power)
            app.update_idletasks()  # Update the Tkinter window
            time.sleep(1)  # Pause for 2 seconds

    # Start the test after 1 second to allow window setup
    app.after(500, update_levels)
    app.mainloop()

if __name__ == "__main__":
    run_Wattage_test()

