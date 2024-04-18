import tkinter as tk
import random
import time

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
        self.root.after(100, self.move)

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
        self.canvas.coords(self.text_id, self.x, self.y)
        self.canvas.itemconfig(self.text_id, text=time.strftime('%H:%M:%S'), font=(self.font_family, self.font_size, 'bold'), fill=self.color)
        new_shape = self.get_random_shape()
        new_shape.create()
        self.canvas.delete(self.shape.id)
        self.shape = new_shape

    def move(self):
        self.root.after(100, self.move)

def get_random_color():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

def update_time():
    global time_labels
    for time_label in time_labels:
        time_label.update()
    root.after(1000, update_time)

root = tk.Tk()
root.attributes('-fullscreen', True)
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.config(bg='#123456')  # Change the background color
canvas.pack()

time_labels = [TimeLabel(root, canvas, random.randint(0, root.winfo_screenwidth()), random.randint(0, root.winfo_screenheight()), 'Helvetica', 20, 'white') for _ in range(10)]

update_time()
root.mainloop()
