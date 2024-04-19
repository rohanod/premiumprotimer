import tkinter as tk
import random
import time
import pygame
from multiprocessing import Process, Queue
import requests

UPDATE_TIME = 3  # Define update time in milliseconds

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
        self.root.after(UPDATE_TIME, self.update)
        self.queue = Queue()  # Queue to signal the beeping process to stop
        self.queue.put(False)  # Initialize the queue with False
        self.process = Process(target=self.play_beep, args=(self.queue,))  # Create a new process for the beeping sound
        self.process.start()  # Start the beeping process

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
        self.font_family = random.choice(normal_font_families)  # Change the font family every frame
        self.color = get_random_color()  # Change the text color every frame
        self.canvas.coords(self.text_id, self.x, self.y)
        self.canvas.itemconfig(self.text_id, text=time.strftime('%H:%M:%S'), font=(self.font_family, self.font_size, 'bold'), fill=self.color)
        new_shape = self.get_random_shape()
        new_shape.create()
        self.canvas.delete(self.shape.id)
        self.shape = new_shape
        self.canvas.tag_raise(self.text_id)  # Bring the text to the front

    def play_beep(self, queue):
        pygame.mixer.init()
        beep_sound = pygame.mixer.Sound('beep.mp3')
        while not queue.get():  # Check if the stop event is set
            Process(target=pygame.mixer.Sound.play, args=(beep_sound,)).start()
            time.sleep(0.1)  # Wait for half a second before starting the next beep sound

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
    for time_label in time_labels:
        time_label.queue.put(True)  # Set the stop event
        if time_label.process.is_alive():  # Check if the process is still running
            time_label.process.join()  # Stop the process
    root.destroy()

try:
    # Download the sound file
    response = requests.get('https://ieonrzfdjfjyrxludwwg.supabase.co/storage/v1/object/public/Bucket/beep.mp3')
    with open('beep.mp3', 'wb') as f:
        f.write(response.content)

    root = tk.Tk()
    root.title("Ultimate Extravaganza Professional Colorful Color-changing Location-changing Resizing Font-changing Shape-changing Clock App Mega Super Duper Turbo Deluxe Plus Ultra Mega 5G, 6G, 7G, 8G Pro Max S-Class Fold Z Ultra Mega X-Treme Edition (Boss-Approved and Coworker Envy Guaranteed)")
    root.protocol("WM_DELETE_WINDOW", on_close)  # Handle the window closing event
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack()

    time_labels = [TimeLabel(root, canvas, random.randint(0, root.winfo_screenwidth()), random.randint(0, root.winfo_screenheight()), random.choice(normal_font_families), 20, 'white') for _ in range(10)]

    update_time()
    root.mainloop()

except KeyboardInterrupt:
    print("Program interrupted by user.")