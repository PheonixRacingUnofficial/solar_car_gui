import tkinter as tk

class Battery(tk.Frame):
    def __init__(self, parent, battery_level):
        super().__init__(parent, width=200, height=420)
        self.pack_propagate(False)  # Prevent shrinking to fit contents

        # Frame for battery
        self.battery_frame = tk.Frame(self, bg="black", width=150, height=310)
        self.battery_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Canvas for the battery filling with extra 10px at the top
        self.canvas = tk.Canvas(self.battery_frame, width=150, height=310, bg="white", highlightthickness=0)
        self.canvas.pack()

        # Battery head (small rectangle on top), shifted down by 10 pixels
        self.canvas.create_rectangle(50, 10, 100, 20, fill="black")

        # Define coordinates for the battery body outline
        self.battery_top = 20
        self.battery_bottom = 300
        self.battery_left = 10
        self.battery_right = 140

        # Draw the battery body outline
        self.canvas.create_rectangle(self.battery_left, self.battery_top, self.battery_right, self.battery_bottom, outline="black", width=3)

        # Draw the initial battery fill rectangle
        self.battery_fill = self.canvas.create_rectangle(self.battery_left + 2, self.battery_top, self.battery_right - 1, self.battery_bottom, fill="white", outline="")

        # Draw the segmented lines every 10%
        segment_height = (self.battery_bottom - self.battery_top) / 10
        for i in range(1, 10):
            y = self.battery_bottom - (i * segment_height)
            self.canvas.create_line(self.battery_left, y, self.battery_right, y, fill="black")

        # Set initial battery level
        self.level = battery_level
        self.update_battery(self.level)

    def update_battery(self, level):
        self.canvas.delete("battery_text")

        fill_height = (level / 100) * (self.battery_bottom - self.battery_top)
        top_fill_position = self.battery_bottom - fill_height

        self.canvas.coords(self.battery_fill, self.battery_left + 2, top_fill_position + 1, self.battery_right - 1, self.battery_bottom)
        self.canvas.itemconfig(self.battery_fill, fill="green")

        self.canvas.create_text(75, (self.battery_top + self.battery_bottom - 25.5) / 2, text=f"{level}%", font=("Arial", 24), fill="black", tags="battery_text")
