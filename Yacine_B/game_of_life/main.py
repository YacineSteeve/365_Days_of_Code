import tkinter as tk
import numpy as np
from random import randint
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


var_launch_pause_text = tk.StringVar()
var_launch_pause_text.set("Launch Cycle")
    
    
def warning(*args):
    exit_decision = messagebox.askyesno("Closing...", "Do you really want to exit?")
    if exit_decision:
        window.quit()
        
        
def cycle(*args):
    global canvas, CELLS, CELLS_STATE, COLS_NUM, ROWS_NUM, CELL_SIZE
    
    if var_launch_pause_text.get() == "Stop Cycle":
        var_launch_pause_text.set("Launch Cycle")
        launch_pause_btn.configure(background="green")
        
        for cell in CELLS:
            canvas.delete(cell)
        
    else:
        var_launch_pause_text.set("Stop Cycle")
        launch_pause_btn.configure(background="red")
        
        CELLS_STATE = np.array([randint(0, 1) for _ in range(ROWS_NUM * COLS_NUM)]).reshape(ROWS_NUM, COLS_NUM)

        for i in range(ROWS_NUM):
            for j in range(COLS_NUM):
                color = "black" if CELLS_STATE[i, j] else "white"
                CELLS.append(canvas.create_rectangle(j*CELL_SIZE, i*CELL_SIZE, 
                                                     (j+1)*CELL_SIZE, (i+1)*CELL_SIZE,
                                                     fill=color,
                                                     outline=color
                                                    )
                            )
    

def generate_canvas():
    global canvas, CELLS, ROWS_NUM, COLS_NUM, CELL_SIZE
    
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
    
    CELL_SIZE = cell_size
    COLS_NUM = canvas_width//cell_size
    ROWS_NUM = canvas_height//cell_size
    
    canvas = tk.Canvas(window, 
                width=canvas_width, 
                height=canvas_height,
                background="white"
                )
    
    canvas.pack(side="left",
                pady=(window_height - int(canvas.cget("height"))) // 2
                )
    
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

launch_pause_btn = tk.Button(buttons_frame, 
                             textvariable=var_launch_pause_text,
                             background="green",
                             overrelief="groove",
                             command=cycle,
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

    refresh_btn.grid(column=1, pady=button_pady_2)
    
    exit_btn.grid(column=1, pady=button_pady_2)
    
    
def hide_game_managing_buttons():
    launch_pause_btn.grid_forget()

    refresh_btn.grid_forget()
    
    exit_btn.grid_forget()
    
            

buttons_frame.pack(side="right", padx=30, fill="y")
show_canvas_setting_buttons()
window.mainloop()