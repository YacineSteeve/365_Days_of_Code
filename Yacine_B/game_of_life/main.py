import tkinter as tk
from tkinter import messagebox
from start_configs import *


window = tk.Tk()

screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

window_width = int(WINDOW_WIDTH_RATIO * screen_width)
window_height = int(WINDOW_HEIGHT_RATIO * screen_height)

gap_x = (screen_width - window_width) // 2
gap_y = (screen_height - window_height) // 2

button_width = int(window_width * BUTTON_WIDTH_RATIO)
button_height = int(window_height * BUTTON_HEIGHT_RATIO)

button_pady_1 = int(window_height * PADY_RATIO_1)
button_pady_2 = int(window_height * PADY_RATIO_2)


window.title("Game of Life")

window.geometry(f"{window_width}x{window_height}+{gap_x}+{gap_y}")

window.resizable(False, False)


buttons_frame = tk.Frame(window)


var_launch_pause = tk.StringVar()
var_launch_pause.set("Launch")


def running_status(*args):
    state = "Launch" if var_launch_pause.get() == "Pause" else "Pause"
    var_launch_pause.set(state)
    
def warning(*args):
    exit_decision = messagebox.askyesno("Closing...", "Do you really want to exit?")
    if exit_decision:
        window.quit()
    

def generate_canvas():
    global canvas
    
    try:
        cell_size = int(cell_size_btn.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid size type (must be integer).")
        return
    else:
        if cell_size < 3 or cell_size > 300:
            messagebox.showerror("Error", "The cells size must be between 3 and 300.")
            return
    
    def adapt_canvas(num):
        return int(num - num % cell_size)
    
    canvas_width = adapt_canvas(window_width * CANVAS_WIDTH_RATIO)
    canvas_height = adapt_canvas(window_height * CANVAS_HEIGHT_RATIO)
    
    canvas = tk.Canvas(window, 
                width=canvas_width, 
                height=canvas_height,
                background="white"
                )

    canvas.pack(side="left",
            pady=(window_height - int(canvas.cget("height")) ) // 2
            )


    def generate_cell(i, j, color):
        canvas.create_rectangle(i*cell_size, j*cell_size, 
                                (i+1)*cell_size, (j+1)*cell_size,
                                fill=color)
    

    for i in range(canvas_width//cell_size):
        for j in range(canvas_height//cell_size):
            color = ALIVE_CELL_COLOR if i==j else DEAD_CELL_COLOR
            generate_cell(i, j, color)
    
    hide_canvas_setting_buttons()
    
    show_game_managing_buttons()
    
            
def clean_window():
    global canvas
    
    canvas.destroy()
    
    hide_game_managing_buttons()
    
    show_canvas_setting_buttons()
    

label = tk.Label(buttons_frame, 
                 text="Choose the cells size\n (from 3 to 300)",
                 height=3
                 )

cell_size_btn = tk.Spinbox(buttons_frame,
                           from_=3,
                           to=300,
                           width=3,
                           wrap=True
                           )

canvas_generator_btn = tk.Button(buttons_frame,
                               text="Generate grid",
                               width=button_width,
                               height=button_height,
                               command=generate_canvas
                               )

next_btn = tk.Button(buttons_frame, 
                     text="Next Step",
                     width=button_width,
                     height=button_height
                     )

previous_btn = tk.Button(buttons_frame, 
                         text="Previous Step",
                         width=button_width,
                         height=button_height
                         )
                         
launch_pause_btn = tk.Button(buttons_frame, 
                             textvariable=var_launch_pause,
                             command=running_status,
                             compound="left",
                             width=button_width,
                             height=button_height
                             )

refresh_btn = tk.Button(buttons_frame,
                        text="Refresh",
                        width=button_width,
                        height=button_height,
                        command=clean_window
                        )

exit_btn = tk.Button(buttons_frame, 
                     text="Exit",
                     command=warning,
                     width=button_width,
                     height=button_height
                     )
    

def show_canvas_setting_buttons():
    label.grid(column=1, pady=button_pady_1)

    cell_size_btn.grid(column=1)

    canvas_generator_btn.grid(column=1, pady=button_pady_1)
    
    exit_btn.grid(column=1, pady=button_pady_2)
    
    
def hide_canvas_setting_buttons():
    label.grid_forget()
    
    cell_size_btn.grid_forget()
    
    canvas_generator_btn.grid_forget()
    
    exit_btn.grid_forget()
    

def show_game_managing_buttons():
    launch_pause_btn.grid(column=1, pady=button_pady_2)

    next_btn.grid(column=1)

    previous_btn.grid(column=1, pady=button_pady_1)

    refresh_btn.grid(column=1, pady=button_pady_2)
    
    exit_btn.grid(column=1, pady=button_pady_2)
    
    
def hide_game_managing_buttons():
    launch_pause_btn.grid_forget()

    next_btn.grid_forget()

    previous_btn.grid_forget()

    refresh_btn.grid_forget()
    
    exit_btn.grid_forget()
    
            

buttons_frame.pack(side="right", padx=30, fill="y")
show_canvas_setting_buttons()
window.mainloop()