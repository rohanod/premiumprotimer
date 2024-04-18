import tkinter as tk
import random
import time
from playsound import playsound
import threading
import requests

UPDATE_TIME = 30  # Define update time in milliseconds

class Shape:
    def __init__(self, canvas, x, y, size, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.color = color

class Oval(Shape):
    def create(self):
        self.id = self.canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color)

class Rectangle(Shape):
    def create(self):
        self.id = self.canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color)

class Arc(Shape):
    def create(self):
        self.id = self.canvas.create_arc(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color)

class Line(Shape):
    def create(self):
        self.id = self.canvas.create_line(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color)

class TimeLabel:
    def __init__(self, root, canvas, x, y, font_family, font_size, color):
        self.root = root
        self.canvas = canvas
        self.x = x
        self.y = y
        self.font_family = font_family
        self.font_size = font_size
        self.color = color
        self.text_id = self.canvas.create_text(x, y, text=time.strftime('%H:%M:%S'), font=(font_family, font_size, 'bold'), fill=color)
        self.shape = self.get_random_shape()
        self.shape.create()
        self.canvas.tag_raise(self.text_id)  # Bring the text to the front
        self.root.after(UPDATE_TIME, self.move)

    def get_random_shape(self):
        shapes = [Oval, Rectangle, Arc, Line]
        random_shape = random.choice(shapes)
        shape_color = get_random_color()
        while shape_color == self.color:  # Ensure the shape color is different from the text color
            shape_color = get_random_color()
        shape_size = self.font_size * 2  # Double the size of the shapes
        shape_x = self.x - shape_size / 2  # Adjust the x-coordinate of the shape to align with the text
        shape_y = self.y - shape_size / 2  # Adjust the y-coordinate of the shape to align with the text
        return random_shape(self.canvas, shape_x, shape_y, shape_size, shape_color)

    def update(self):
        self.x = random.randint(0, self.root.winfo_screenwidth())
        self.y = random.randint(0, self.root.winfo_screenheight())
        self.font_size = random.randint(10, 50)  # Generate a new random size for the font
        self.canvas.coords(self.text_id, self.x, self.y)
        self.canvas.itemconfig(self.text_id, text=time.strftime('%H:%M:%S'), font=(self.font_family, self.font_size, 'bold'), fill=self.color)
        new_shape = self.get_random_shape()
        new_shape.create()
        self.canvas.delete(self.shape.id)
        self.shape = new_shape
        self.canvas.tag_raise(self.text_id)  # Bring the text to the front
        threading.Thread(target=playsound, args=('beep.mp3',)).start()

    def move(self):
        self.root.after(UPDATE_TIME, self.move)

def get_random_color():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

def update_time():
    global time_labels
    for time_label in time_labels:
        time_label.update()
    canvas.config(bg=get_random_color())  # Change the background color every frame
    root.after(UPDATE_TIME, update_time)

def on_close():
    print("Program closed by user.")
    root.destroy()

try:
    # Download the sound file
    response = requests.get('https://ieonrzfdjfjyrxludwwg.supabase.co/storage/v1/object/public/Bucket/beep.mp3')
    with open('beep.mp3', 'wb') as f:
        f.write(response.content)

    root = tk.Tk()
    root.title("Professional Colorful Color-changing Location-changing Resizing Font-changing Shape-changing Clock app 2023 Pro Plus S-Class Fold Z Ultra Mega 5G, 6G, 7G, 8G (Workplace approved)")
    root.protocol("WM_DELETE_WINDOW", on_close)  # Handle the window closing event
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack()

    time_labels = [TimeLabel(root, canvas, random.randint(0, root.winfo_screenwidth()), random.randint(0, root.winfo_screenheight()), 'Helvetica', 20, 'white') for _ in range(10)]

    update_time()
    root.mainloop()

except KeyboardInterrupt:
    print("Program interrupted by user.")