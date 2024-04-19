import tkinter as tk
from datetime import datetime
import random
import math

crazy_font_families = ['Holokai','Bodoni Ornaments','Webdings','Wingdings','Wingdings 1','Wingdings 2','Wingdings 3']

normal_font_families = ['calibri', 'times', 'helvetica', 'courier', 'arial', 'impact', 'comic sans ms', 'palatino', 'georgia',
                        'dejavu sans', 'dejavu serif', 'dejavu sans mono', 'roboto', 'ubuntu', 'open sans', 'lato',
                        'source sans pro', 'montserrat', 'raleway', 'droid sans', 'noto sans', 'noto serif', 'fira sans',
                        'fira code', 'inconsolata', 'merriweather', 'playfair display', 'oswald', 'quicksand', 'poppins',
                        'hind', 'josefin sans', 'nunito', 'cabin', 'lobster', 'monospace', 'cursive', 'fantasy', 'system-ui',
                        'apple system', 'segoe ui', 'tahoma', 'verdana', 'geneva', 'impact', 'copperplate', 'palatino linotype',
                        'times new roman', 'book antiqua', 'Brush Script MT']
# testfont = ['Curlz MT']
choice = int(input("Crazy Font (1) or Normal Font (2): "))
if choice == 1:
    font_families = crazy_font_families
elif choice == 2:
    font_families = normal_font_families
#font_families = testfont
def update_time():
    current_time = datetime.now()
    string_time = current_time.strftime('%I:%M:%S:%f')[:-3] + " " + current_time.strftime('%p')

    random_bg_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

    # Change the text color every 5 milliseconds
    random_text_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

    # Generate random x and y coordinates for the time label
    random_x = random.randint(0, root.winfo_screenwidth() - time_label.winfo_reqwidth())
    random_y = random.randint(0, root.winfo_screenheight() - time_label.winfo_reqheight())
    time_label.place(x=random_x, y=random_y)

    # Change the font family randomly every 5 milliseconds
    random_font_family = random.choice(font_families)

    # Change the font size randomly within a range every 5 milliseconds
    random_font_size = random.randint(10, 50)  # Adjusted font size range

    time_label.config(font=(random_font_family, random_font_size, 'bold'))

    # Clear previous drawings
    canvas.delete("all")

    # Create 50 random shapes and text instances at different places on the canvas
    for i in range(50):
        # Generate random x and y coordinates for the shape and text
        random_x = random.randint(0, root.winfo_screenwidth() - time_label.winfo_reqwidth())
        random_y = random.randint(0, root.winfo_screenheight() - time_label.winfo_reqheight())
        create_random_shape(random_x, random_y, random_bg_color, random_text_color, string_time, random_font_size, random_font_family)

    # Clear the screen after one microsecond
    #canvas.after(100, clear_screen)

    root.after(50, update_time)  # Update every 1 millisecond

def create_random_shape(x, y, bg_color, text_color, text, font_size, font_family=None, sides=None, rotation=None, scale=None):
    # Generate a random color for the shape
    random_bg_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

    # Generate a random number of sides for the shape
    if sides is None:
        sides = random.randint(3, 20)  # Increase the range of sides

    angle = 360 / sides
    size = random.randint(10, 100)  # Adjust the size range

    coordinates = []

    for i in range(sides):
        if rotation is not None:
            x_coord = x + size * (scale or 1.0) * math.cos(math.radians(angle * i + rotation))
            y_coord = y + size * (scale or 1.0) * math.sin(math.radians(angle * i + rotation))
        else:
            x_coord = x + size * (scale or 1.0) * math.cos(math.radians(angle * i))
            y_coord = y + size * (scale or 1.0) * math.sin(math.radians(angle * i))
        coordinates.extend([x_coord, y_coord])

    # Calculate the center coordinates of the shape
    text_x = x + size / 2 * (scale or 1.0)
    text_y = y + size / 2 * (scale or 1.0)

    # Add more randomness to text position
    text_x += random.uniform(-50, 50)
    text_y += random.uniform(-50, 50)

    # Check if text position is within canvas boundaries
    text_x = max(0, min(text_x, root.winfo_screenwidth()))
    text_y = max(0, min(text_y, root.winfo_screenheight()))

    font_family = font_family or random.choice(font_families)
    canvas.create_polygon(coordinates, fill=random_bg_color, outline=text_color)
    canvas.create_text(text_x, text_y, text=text, font=(font_family, int(font_size * 0.6), 'bold'), fill=text_color)

def clear_screen():
    canvas.delete("all")

# Create the main window
root = tk.Tk()
root.title("Colorful Moving Resizing Font-changing Shape-changing Premium Pro Plus Max Ultra Super Duper Extra Timer")

# Create a canvas to draw shapes
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg='white')
canvas.pack()

# Create a label to display the time
time_label = tk.Label(root, font=('calibri', 40, 'bold'))
time_label.pack()

# Call the update_time function to initialize the time display, color change, resizing, font changing, and shape changing
update_time()

# Run the main loop
root.mainloop()