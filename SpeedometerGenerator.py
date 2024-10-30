import tkinter as tk
import math


class Speedometer:
    def __init__(self, master, max_speed=60):
        self.needle = None
        self.master = master
        self.max_speed = max_speed
        self.speed = 0

        # Increase the canvas size to fit the full speedometer
        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.pack()

        self.draw_speedometer()

    def create_line_with_length(self, x1, y1, length, angle):
        # Calculates the end point of the line based on length and angle
        x2 = x1 + length * math.cos(math.radians(angle))
        y2 = y1 + length * math.sin(math.radians(angle))

        # Draw the line on the canvas
        self.canvas.create_line(x1, y1, x2, y2, width=1)

    def draw_speedometer(self):
        # Draw the arc representing the speedometer
        self.canvas.create_arc(10, 10, 190, 190, start=-45, extent=270, style="arc", outline="black", width=2)

        # Draw the main speed ticks and labels
        for i in range(0, self.max_speed + 1, 10):
            angle = 135 + (270 * i / self.max_speed)
            x = 100 + 80 * math.cos(math.radians(angle))
            y = 100 + 80 * math.sin(math.radians(angle))
            self.create_line_with_length(100, 100, 70, angle)
            self.canvas.create_text(x, y, text=str(i), anchor="center")

        # Draw the mini-ticks without labels
        for i in range(0, self.max_speed + 1, 5):
            angle = 135 + (270 * i / self.max_speed)
            x = 100 + 80 * math.cos(math.radians(angle))
            y = 100 + 80 * math.sin(math.radians(angle))
            if i % 10 != 0:  # Avoid duplicate ticks at main tick positions
                angle = 135 + (270 * i / self.max_speed)
                self.create_line_with_length(100, 100, 55, angle)  # Use shorter length for mini-ticks
                self.canvas.create_text(x, y, text=str(i), anchor="center")  # Display label for mini-ticks

        # Create the needle
        self.needle = self.canvas.create_line(100, 100, 100, 20, fill="red", width=2)

    def update_speed(self, speed):
        self.speed = speed
        angle = 135 + (270 * self.speed / self.max_speed)
        x = 100 + 80 * math.cos(math.radians(angle))
        y = 100 + 80 * math.sin(math.radians(angle))
        self.canvas.coords(self.needle, 100, 100, x, y)

    def moveto(self, param, param1):
        pass

    def changerange(self, Range, rfont):
        pass

    def create_line(self, x1, y1, x2, y2):
        pass
