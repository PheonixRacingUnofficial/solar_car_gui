import tkinter as tk

# Define scaling
scaling_factor = 1.6
canvas_length = int(200 * scaling_factor)
canvas_height = int(200 * scaling_factor)
integrated = 20  # how many small lines are defined

class Wattage(tk.Frame):
    def __init__(self, parent, wattage_level=100):
        super().__init__(parent)

        # Set the Frame's size and appearance
        # Removed the geometry and resizable calls since they're not valid for Frames
        self.configure(width=canvas_length, height=canvas_height)

        # Frame for wattage
        self.wattage_frame = tk.Frame(self, bg="black", width=canvas_length, height=canvas_height)
        self.wattage_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Canvas for the wattage filling with extra 10px at the top
        self.canvas = tk.Canvas(self.wattage_frame, width=canvas_length, height=canvas_height, bg="white", highlightthickness=0)
        self.canvas.pack()

        # Wattage head (small rectangle on top), shifted down by 10 pixels
        self.canvas.create_rectangle((16 / 36) * canvas_height, (5 / 36) * canvas_height, 
                                     (20 / 36) * canvas_length, (4 / 36) * canvas_height, fill="black")

        # Define coordinates for the wattage body outline
        self.wattage_top = (5 / 36) * canvas_height
        self.wattage_bottom = (31 / 36) * canvas_height
        self.wattage_left = (11 / 36) * canvas_length
        self.wattage_right = (25 / 36) * canvas_length

        # Draw the wattage body outline
        self.canvas.create_rectangle(self.wattage_left, self.wattage_top, self.wattage_right, self.wattage_bottom,
                                     outline="black", width=3)

        # Draw the initial wattage fill rectangle
        self.wattage_fill = self.canvas.create_rectangle(self.wattage_left + 2, self.wattage_top,
                                                         self.wattage_right - 1, self.wattage_bottom, fill="white",
                                                         outline="")

        # Draw the segmented lines every 10%, dynamically calculated based on the outline
        segment_height = (self.wattage_bottom - self.wattage_top) / integrated
        for i in range(1, integrated):
            y = self.wattage_bottom - (i * segment_height)
            self.canvas.create_line(self.wattage_left, y, self.wattage_right, y, fill="black")

        # Set initial wattage level
        self.level = wattage_level
        self.update_wattage(self.level)

    def update_wattage(self, level):
        # Clear any existing text
        self.canvas.delete("wattage_text")

        # Calculate height of the fill based on the level and wattage outline coordinates
        fill_height = (level / 100) * (self.wattage_bottom - self.wattage_top)
        top_fill_position = self.wattage_bottom - fill_height

        # Update the wattage fill
        self.canvas.coords(self.wattage_fill, self.wattage_left + 2, top_fill_position + 1, self.wattage_right - 1,
                           self.wattage_bottom)
        self.canvas.itemconfig(self.wattage_fill, fill="yellow")

        # Display the wattage percentage in the middle of the wattage
        self.canvas.create_text((18 / 36) * canvas_length, (self.wattage_top + self.wattage_bottom - 25.5) / 2,
                                text=f"{level}%", font=("Arial", 24), fill="black", tags="wattage_text")
