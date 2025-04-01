# WattageTest.py
from Wattage import Wattage


def run_wattage_test():
    # Starting wattage level
    wattage_level = 60
    app = Wattage(wattage_level)
    app.mainloop()


if __name__ == "__main__":
    run_wattage_test()
