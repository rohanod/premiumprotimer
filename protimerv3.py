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

    def move(self):
        dx = random.randint(-10, 10)
        dy = random.randint(-10, 10)
        self.canvas.move(self.id, dx, dy)

    def change_color(self):
        color = get_random_color()
        self.canvas.itemconfig(self.id, fill=color)

class Oval(Shape):
    def create(self):
        self.id = self.canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color, outline=self.color)

    def change_color(self):
        color = get_random_color()
        self.canvas.itemconfig(self.id, fill=color, outline=color)

class Rectangle(Oval):
    def create(self):
        self.id = self.canvas.create_rectangle(self.x, self.y, self.x + self.size * 2, self.y + self.size, fill=self.color, outline=self.color)

class Arc(Oval):
    def create(self):
        self.id = self.canvas.create_arc(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color, outline=self.color)

class Line(Shape):
    def create(self):
        self.id = self.canvas.create_line(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color)

class TimeLabel:
    def __init__(self, root, canvas, x, y, font_family, font_size, color):
        self.label = tk.Label(root, text=time.strftime('%H:%M:%S'), font=(font_family, font_size, 'bold'), fg=color)
        self.label.place(x=x, y=y)
        self.shape = self.get_random_shape(canvas, x, y, font_size, color)
        self.shape.create()

    def get_random_shape(self, canvas, x, y, size, color):
        shapes = [Oval, Rectangle, Arc, Line]
        random_shape = random.choice(shapes)
        return random_shape(canvas, x, y, size, color)

def get_random_color():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

def update_time():
    global time_labels
    for time_label in time_labels:
        time_label.label.destroy()
    canvas.delete("all")
    canvas.config(bg=get_random_color())  # Add this line to change the background color
    time_labels = [TimeLabel(root, canvas, random.randint(0, root.winfo_screenwidth()), random.randint(0, root.winfo_screenheight()), random.choice(font_families), random.randint(10, 100), get_random_color()) for _ in range(10)]
    for time_label in time_labels:
        time_label.shape.move()
        time_label.shape.change_color()
    root.after(10, update_time)

root = tk.Tk()
root.title("Professional Colorful Color-changing Location-changing Resizing Font-changing Shape-changing Clock app 2023 Pro Plus S-Class Fold Z Ultra Mega 5G, 6G, 7G, 8G (Workplace approved)")
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg='white')
canvas.pack()
font_families = ['calibri', 'times', 'helvetica', 'courier', 'arial', 'impact', 'comic sans ms', 'palatino', 'georgia', 'verdana', 'garamond', 'tahoma']
time_labels = []
update_time()
root.mainloop()