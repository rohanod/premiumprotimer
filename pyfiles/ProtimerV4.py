import tkinter as tk
import random
import time
import numpy as np
import threading
import pygame
import math

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

UPDATE_TIME = 50
FONT_FAMILIES = ['Arial', 'Helvetica', 'Times', 'Courier', 'Verdana', 'Comic Sans MS', 'Impact']

titles = [
    "Ultimate Extravaganza Professional Colorful Color-changing Location-changing Resizing Font-changing Shape-changing Clock App Mega Super Duper Turbo Deluxe Plus Ultra Mega 5G, 6G, 7G, 8G Pro Max S-Class Fold Z Ultra Mega X-Treme Edition (Boss-Approved and Coworker Envy Guaranteed) Now with Extra Cheese and a Side of Existential Dread",
    "Time-bending, Space-warping, Mind-blowing, Reality-altering, Universe-shattering Clock App of Doom, Despair, and Unending Joy (Now with Extra Sprinkles and a Side of Fries)",
    "Clock App of Unparalleled Magnificence, Unmatched Brilliance, and Unquestionable Superiority (Now with Extra Cheese, Pepperoni, and a Crispy Crust)",
    "The Clock App to End All Clock Apps, the Alpha and Omega, the First and the Last, the Beginning and the End (Now with a Free Subscription to the End of the Universe)",
    "Clock App of Infinite Wisdom, Eternal Knowledge, and Unfathomable Understanding (Batteries Not Included, Some Assembly Required, Not Suitable for Children Under 3 Years)",
    "The 'Is It Too Late to Learn TikTok Dances?' Procrastinator's Delight Clock App (Now with Built-in Excuse Generator)",
    "Time Lord's Pocket Watch: The 'Wibbly Wobbly Timey Wimey' Edition (Paradoxes Included at No Extra Charge)",
    "The 'I Swear I'm Only 5 Minutes Late' Self-Delusion Clock App (Pairs Well with Cold Coffee and Wrinkled Shirts)",
    "Schrödinger's Clock: It's Both Too Early and Too Late Until You Look At It (Cat Not Included)",
    "The 'Wait, When Did I Last Sleep?' Insomniac's Dream Clock App (Comes with Complementary Eye Bags)",
    "Chronos' Folly: The 'Time Flies When You're Having Existential Crises' Edition (Now with Integrated Therapy Chatbot)",
    "The 'One More Episode' Binge-Watcher's Nemesis Clock (Automatically Hides When Parents Walk In)",
    "Timey McTimeface: The Clock App That Literally Nobody Asked For (But You're Getting Anyway)",
    "The 'Is It Too Early for Wine?' Sommelier's Dilemma Clock App (Automatically Adjusts to 'Wine O'Clock' After 3 PM)",
    "Quantum Timekeeping: The 'Simultaneously Late and Early' Paradox Clock (Schrödinger Approved)"
]

class ChaosElement:
    def __init__(self, canvas):
        self.canvas = canvas
        self.text_id = None
        self.shape_id = None
        self.rotation = 0
        self.update()

    def update(self):
        x = random.randint(0, self.canvas.winfo_width())
        y = random.randint(0, self.canvas.winfo_height())
        font = (random.choice(FONT_FAMILIES), random.randint(10, 50))
        color = get_random_color()
        text = get_chaotic_time()

        if self.text_id:
            self.canvas.delete(self.text_id)
        if self.shape_id:
            self.canvas.delete(self.shape_id)

        shape_size = random.randint(20, 100)
        shape_color = get_random_color(exclude=color)
        shape_type = random.choice(['oval', 'rectangle', 'arc', 'polygon', 'star'])
        
        self.rotation += random.uniform(-30, 30)
        
        if shape_type == 'oval':
            self.shape_id = self.canvas.create_oval(x-shape_size/2, y-shape_size/2, x+shape_size/2, y+shape_size/2, fill=shape_color)
        elif shape_type == 'rectangle':
            self.shape_id = self.canvas.create_rectangle(x-shape_size/2, y-shape_size/2, x+shape_size/2, y+shape_size/2, fill=shape_color)
        elif shape_type == 'arc':
            self.shape_id = self.canvas.create_arc(x-shape_size/2, y-shape_size/2, x+shape_size/2, y+shape_size/2, fill=shape_color, start=random.randint(0, 360), extent=random.randint(30, 330))
        elif shape_type == 'polygon':
            points = [x + shape_size/2 * math.cos(i*2*math.pi/5) for i in range(5)] + [y + shape_size/2 * math.sin(i*2*math.pi/5) for i in range(5)]
            self.shape_id = self.canvas.create_polygon(points, fill=shape_color)
        elif shape_type == 'star':
            points = []
            for i in range(10):
                angle = i * math.pi / 5
                r = shape_size/2 if i % 2 == 0 else shape_size/4
                points.append(x + r * math.cos(angle))
                points.append(y + r * math.sin(angle))
            self.shape_id = self.canvas.create_polygon(points, fill=shape_color)

        self.text_id = self.canvas.create_text(x, y, text=text, font=font, fill=color, angle=self.rotation)
        self.canvas.tag_raise(self.text_id)

def play_tone():
    while True:
        frequency = np.random.uniform(low=200.0, high=2000.0)
        sample_rate = 44100
        T = 0.1
        t = np.linspace(0, T, int(T * sample_rate), False)
        tone = np.sin(frequency * t * 2 * np.pi)
        stereo_tone = np.column_stack((tone, tone))
        audio = (stereo_tone * 32767).astype(np.int16)
        sound = pygame.sndarray.make_sound(audio)
        sound.play()
        time.sleep(0.5)

def get_random_color(exclude=None):
    while True:
        color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
        if color != exclude:
            return color

def get_chaotic_time():
    formats = [
        '%H:%M:%S', '%I:%M:%S %p', '%H:%M', '%I:%M %p',
        '%S:%M:%H', '%Y-%m-%d %H:%M:%S', '%d/%m/%Y %H:%M',
        'It\'s %I:%M and all is well', 'Time is an illusion',
        str(time.time()), 'Tempus Fugit', 'Carpe Diem',
        'Now o\'clock', 'Time to panic!', 'Coffee time',
        'Nap time', 'Party o\'clock', 'Quantum time: %H:%M:%S'
    ]
    return time.strftime(random.choice(formats))

def shake_screen(root):
    original_geometry = root.geometry()
    for _ in range(5):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        root.geometry(f"+{root.winfo_x() + x}+{root.winfo_y() + y}")
        root.update()
        time.sleep(0.05)
    root.geometry(original_geometry)

def update_chaos(root, canvas, elements, titles):
    for element in elements:
        element.update()
    
    if random.random() < 0.1:
        canvas.config(bg=get_random_color())
    
    if random.random() < 0.1:
        root.title(random.choice(titles))
    
    if random.random() < 0.05:
        shake_screen(root)
    
    root.after(UPDATE_TIME, update_chaos, root, canvas, elements, titles)

def main():
    root = tk.Tk()
    root.title(random.choice(titles))
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    window_width = int(screen_width * 0.95)
    window_height = int(screen_height * 0.95)
    
    position_top = int(screen_height / 2 - window_height / 2)
    position_left = int(screen_width / 2 - window_width / 2)

    root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

    canvas = tk.Canvas(root, width=window_width, height=window_height)
    canvas.pack(fill=tk.BOTH, expand=True)

    elements = [ChaosElement(canvas) for _ in range(10)]

    threading.Thread(target=play_tone, daemon=True).start()

    update_chaos(root, canvas, elements, titles)

    root.mainloop()

if __name__ == "__main__":
    main()