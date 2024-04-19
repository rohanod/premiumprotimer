import tkinter as tk
import random
import time
import os

def get_random_color():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

def update_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time, fg=get_random_color())
    canvas.config(bg=get_random_color())

    random_x = random.randint(0, root.winfo_screenwidth() - time_label.winfo_reqwidth())
    random_y = random.randint(0, root.winfo_screenheight() - time_label.winfo_reqheight())
    time_label.place(x=random_x, y=random_y)

    font_families = ['calibri', 'times', 'helvetica', 'courier', 'arial', 'impact', 'comic sans ms', 'palatino', 'georgia', 'verdana', 'garamond', 'tahoma']
    random_font_family = random.choice(font_families)
    
    random_font_size = random.randint(10, 100)
    
    time_label.config(font=(random_font_family, random_font_size, 'bold'))

    shapes = ['oval', 'rectangle', 'arc', 'line']
    random_shape = random.choice(shapes)
    canvas.delete("all")
    if random_shape == 'oval':
        shape_id = canvas.create_oval(random_x, random_y, random_x + random_font_size, random_y + random_font_size, fill=get_random_color(), outline=get_random_color())
    elif random_shape == 'rectangle':
        shape_id = canvas.create_rectangle(random_x, random_y, random_x + random_font_size * 2, random_y + random_font_size, fill=get_random_color(), outline=get_random_color())
    elif random_shape == 'arc':
        shape_id = canvas.create_arc(random_x, random_y, random_x + random_font_size, random_y + random_font_size, fill=get_random_color(), outline=get_random_color())
    elif random_shape == 'line':
        shape_id = canvas.create_line(random_x, random_y, random_x + random_font_size, random_y + random_font_size, fill=get_random_color())
    move_shape(shape_id)
    time_label.after(1, update_time)  

def move_shape(shape_id):
    random_dx = random.randint(-10, 10)
    random_dy = random.randint(-10, 10)
    canvas.move(shape_id, random_dx, random_dy)

def on_close():
    print("Program closed by user.")
    os._exit(0)

root = tk.Tk()
root.title("Professional Colorful Color-changing Location-changing Resizing Font-changing Shape-changing Clock app 2023 Pro Plus S-Class Fold Z Ultra Mega 5G, 6G, 7G, 8G (Workplace approved)")
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg='white')
canvas.pack()
time_label = tk.Label(root, font=('calibri', 40, 'bold'))
time_label.pack()
update_time()
root.mainloop()