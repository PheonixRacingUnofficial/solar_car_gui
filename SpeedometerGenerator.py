import tkinter as tk
import math

# Variables; set scaling_factor and font_size as desired
scaling_factor = 2
max_speed_var = 50
font_size = 36
canvas_length = (200*scaling_factor)
canvas_height = (200*scaling_factor)
speedometer_length = (195*scaling_factor)
speedometer_height = (195*scaling_factor)


class Speedometer:
    def __init__(self, master, max_speed=max_speed_var):
        self.needle = None
        self.master = master
        self.max_speed = max_speed
        self.speed = 0

        # Increase the canvas size to fit the full speedometer
        self.canvas = tk.Canvas(master, width=canvas_length, height=canvas_height)
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
        self.canvas.create_arc(10, 10, speedometer_length, speedometer_height, start=-45, extent=270, style="arc", outline="black", width=2)

        # Draw the main speed ticks and labels
        for i in range(0, self.max_speed + 1, 10):
            angle = 135 + (270 * i / self.max_speed)
            x = (canvas_length/2) + (80*scaling_factor) * math.cos(math.radians(angle))
            y = (canvas_height/2) + (80*scaling_factor) * math.sin(math.radians(angle))
            self.create_line_with_length((canvas_length/2), (canvas_height/2), (70*scaling_factor), angle)
            self.canvas.create_text(x, y, text=str(i), anchor="center", font=font_size)

        # Draw the mini-ticks without labels
        for i in range(0, self.max_speed + 1, 5):
            angle = 135 + (270 * i / self.max_speed)
            x = (canvas_length/2) + (80*scaling_factor) * math.cos(math.radians(angle))
            y = (canvas_height/2) + (80*scaling_factor) * math.sin(math.radians(angle))
            if i % 10 != 0:  # Avoid duplicate ticks at main tick positions
                angle = 135 + (270 * i / self.max_speed)
                self.create_line_with_length((canvas_length/2), (canvas_height/2), (55*scaling_factor), angle)  # Use shorter length for mini-ticks
                self.canvas.create_text(x, y, text=str(i), anchor="center", font=font_size)  # Display label for mini-ticks

        # Create the needle
        self.needle = self.canvas.create_line((canvas_length/2), (canvas_height/2), (100*scaling_factor), 20, fill="red", width=2)

    def update_speed(self, speed):
        self.speed = speed
        angle = 135 + (270 * self.speed / self.max_speed)
        x = (canvas_length/2) + (80*scaling_factor) * math.cos(math.radians(angle))
        y = (canvas_height/2) + (80*scaling_factor) * math.sin(math.radians(angle))
        self.canvas.coords(self.needle, (canvas_length/2), (canvas_height/2), x, y)

    def moveto(self, param, param1):
        pass

    def changerange(self, Range, rfont):
        pass

    def create_line(self, x1, y1, x2, y2):
        pass
