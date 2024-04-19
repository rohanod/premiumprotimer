import tkinter as tk
import random
import time
import numpy as np
import simpleaudio as sa
import threading
import os

UPDATE_TIME = 3

normal_font_families = ['calibri', 'times', 'helvetica', 'courier', 'arial', 'impact', 'comic sans ms', 'palatino', 'georgia',
                        'dejavu sans', 'dejavu serif', 'dejavu sans mono', 'roboto', 'ubuntu', 'open sans', 'lato',
                        'source sans pro', 'montserrat', 'raleway', 'droid sans', 'noto sans', 'noto serif', 'fira sans',
                        'fira code', 'inconsolata', 'merriweather', 'playfair display', 'oswald', 'quicksand', 'poppins',
                        'hind', 'josefin sans', 'nunito', 'cabin', 'lobster', 'monospace', 'cursive', 'fantasy', 'system-ui',
                        'apple system', 'segoe ui', 'tahoma', 'verdana', 'geneva', 'impact', 'copperplate', 'palatino linotype',
                        'times new roman', 'book antiqua', 'Brush Script MT']

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
    def __init__(self, canvas, x, y, font_family, font_size, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.font_family = font_family
        self.font_size = font_size
        self.color = color
        self.text_id = self.canvas.create_text(x, y, text=time.strftime('%H:%M:%S'), font=(font_family, font_size, 'bold'), fill=color)
        self.shape = self.get_random_shape()
        self.shape.create()
        self.canvas.tag_raise(self.text_id)
        self.canvas.winfo_toplevel().after(UPDATE_TIME, self.update)
        self.thread = threading.Thread(target=self.play_tone)
        self.thread.start()

    def get_random_shape(self):
        shapes = [Oval, Rectangle, Arc, Line]
        random_shape = random.choice(shapes)
        shape_color = get_random_color()
        while shape_color == self.color:
            shape_color = get_random_color()
        shape_size = self.font_size * 2
        shape_x = self.x - shape_size / 2
        shape_y = self.y - shape_size / 2
        return random_shape(self.canvas, shape_x, shape_y, shape_size, shape_color)

    def update(self):
        self.x = random.randint(0, self.canvas.winfo_toplevel().winfo_screenwidth())
        self.y = random.randint(0, self.canvas.winfo_toplevel().winfo_screenheight())
        self.font_size = random.randint(10, 50)
        self.font_family = random.choice(normal_font_families)
        self.color = get_random_color()
        self.canvas.coords(self.text_id, self.x, self.y)
        self.canvas.itemconfig(self.text_id, text=time.strftime('%H:%M:%S'), font=(self.font_family, self.font_size, 'bold'), fill=self.color)
        new_shape = self.get_random_shape()
        new_shape.create()
        self.canvas.delete(self.shape.id)
        self.shape = new_shape
        self.canvas.tag_raise(self.text_id)

    def play_tone(self):
        while True:
            frequency = np.random.uniform(low=200.0, high=2000.0)
            sample_rate = 44100
            T = 0.1
            t = np.linspace(0, T, int(T * sample_rate), False)
            tone = np.sin(frequency * t * 2 * np.pi)
            audio = tone * (2**15 - 1) / np.max(np.abs(tone))
            audio = audio.astype(np.int16)
            play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
            play_obj.wait_done()
            time.sleep(0.05)

def get_random_color():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

def update_time():
    global time_labels
    for time_label in time_labels:
        time_label.update()
    canvas.config(bg=get_random_color())
    root.after(UPDATE_TIME, update_time)

def on_close():
    print("Program closed by user.")
    os._exit(0)

root = tk.Tk()
root.title("Ultimate Extravaganza Professional Colorful Color-changing Location-changing Resizing Font-changing Shape-changing Clock App Mega Super Duper Turbo Deluxe Plus Ultra Mega 5G, 6G, 7G, 8G Pro Max S-Class Fold Z Ultra Mega X-Treme Edition (Boss-Approved and Coworker Envy Guaranteed)")
root.protocol("WM_DELETE_WINDOW", on_close)
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack()

time_labels = [TimeLabel(canvas, random.randint(0, root.winfo_screenwidth()), random.randint(0, root.winfo_screenheight()), random.choice(normal_font_families), 20, 'white') for _ in range(10)]

update_time()
root.mainloop()