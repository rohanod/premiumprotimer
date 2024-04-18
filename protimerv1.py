import tkinter as tk
from time import strftime
import random

def update_time():
    string_time = strftime('%H:%M:%S %p')
    time_label.config(text=string_time)

    # Change the background color every second
    random_bg_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    time_label.config(bg=random_bg_color)

    # Change the text color every second
    random_text_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    time_label.config(fg=random_text_color)

    # Move the label to a random position within the window
    random_x = random.randint(0, root.winfo_screenwidth() - time_label.winfo_reqwidth())
    random_y = random.randint(0, root.winfo_screenheight() - time_label.winfo_reqheight())
    time_label.place(x=random_x, y=random_y)

    # Change the font family randomly
    font_families = ['calibri', 'times', 'helvetica', 'courier', 'arial', 'impact', 'comic sans ms', 'palatino', 'georgia']
    random_font_family = random.choice(font_families)
    
    # Change the font size randomly within a range
    random_font_size = random.randint(10, 80)
    
    time_label.config(font=(random_font_family, random_font_size, 'bold'))

    # Change the shape randomly
    shapes = ['oval', 'rectangle']
    random_shape = random.choice(shapes)
    canvas.delete("all")
    if random_shape == 'oval':
        shape_id = canvas.create_oval(random_x, random_y, random_x + random_font_size, random_y + random_font_size, fill=random_bg_color, outline=random_text_color)
    elif random_shape == 'rectangle':
        shape_id = canvas.create_rectangle(random_x, random_y, random_x + random_font_size * 2, random_y + random_font_size, fill=random_bg_color, outline=random_text_color)
    move_shape(shape_id)
    time_label.after(1, update_time)  
def move_shape(shape_id):
    random_dx = random.randint(-5, 5)
    random_dy = random.randint(-5, 5)
    canvas.move(shape_id, random_dx, random_dy)
root = tk.Tk()
root.title("Professional Colorful Color-changing Location-changing Resizing Font-changing Shape-changing Clock app 2023 Pro Plus S-Class Fold Z Ultra Mega 5G, 6G, 7G, 8G (Workplace approved)")
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg='white')
canvas.pack()
time_label = tk.Label(root, font=('calibri', 40, 'bold'))
time_label.pack()
update_time()
root.mainloop()