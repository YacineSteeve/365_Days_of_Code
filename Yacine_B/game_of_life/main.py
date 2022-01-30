import tkinter as tk
from tkinter import messagebox
import numpy as np
from start_configs import *
#from random import randint

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

var_launch_stop_text = tk.StringVar()
var_speed = tk.StringVar()
    
    
def warning(*args):
    exit_decision = messagebox.askyesno("Closing...", "Do you really want to exit?")
    if exit_decision:
        window.quit()
        
        
def reverse_color(color):
    return "black" if color == "white" else "white"


def create_cell(x, y, color):
    global canvas, CELL_SIZE
    
    return canvas.create_rectangle(y*CELL_SIZE, 
                                   x*CELL_SIZE, 
                                   (y+1)*CELL_SIZE, 
                                   (x+1)*CELL_SIZE,
                                    fill=color,
                                    outline=reverse_color(color)
                                    )
        
        
def clean_canvas():
    global canvas, CELLS, CELLS_STATE, ROWS_NUM, COLS_NUM
    
    for i in range(ROWS_NUM):
        for j in range(COLS_NUM):
            if CELLS_STATE[i, j]:
                CELLS[i, j] = create_cell(i, j, "white")
                CELLS_STATE[i, j] = 0
        
        
def look_around(x, y):
    global ROWS_NUM, COLS_NUM, CELLS_STATE
    
    cell_around = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), 
                   (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    
    num_alive = 0
    
    for cell in cell_around:
        if cell[0] in range(ROWS_NUM) and cell[1] in range(COLS_NUM) and CELLS_STATE[cell[0], cell[1]]:
            num_alive += 1
            
    return num_alive


def cycle():
    global canvas, CYCLE_SPEED, CELLS, CELLS_STATE, ROWS_NUM, COLS_NUM
    
    new_cells_state = np.zeros((ROWS_NUM, COLS_NUM))
    
    for i in range(ROWS_NUM):
        for j in range(COLS_NUM):
            if not CELLS_STATE[i, j] and look_around(i, j) == 3:
                new_cells_state[i, j] = 1
            elif CELLS_STATE[i, j] and look_around(i, j) not in [2, 3]:
                new_cells_state[i, j] = 0
            else:
                new_cells_state[i, j] = CELLS_STATE[i, j]
                
    CELLS_STATE = new_cells_state
    
    del new_cells_state
    
    for i in range(ROWS_NUM):
        for j in range(COLS_NUM):
            color = "black" if CELLS_STATE[i, j] else "white"
            CELLS[i, j] = create_cell(i, j, color)
    
    if var_launch_stop_text.get() == "Stop Cycle":
        canvas.after(CYCLE_SPEED, cycle)
    
    
def launch_stop(*args):
    global canvas, CELLS
    
    if var_launch_stop_text.get() == "Stop Cycle":
        var_launch_stop_text.set("Launch Cycle")
        launch_stop_btn.configure(background="green")
        
        clean_canvas()
        canvas.bind("<Button-1>", set_cell)
        
    else:
        var_launch_stop_text.set("Stop Cycle")
        launch_stop_btn.configure(background="red")
        
        canvas.unbind("<Button-1>")
        
        cycle()
        

def set_cell(event):
    global canvas, CELL_SIZE, CELLS_STATE, CELLS, ROWS_NUM, COLS_NUM
    
    target_y, target_x = event.x // CELL_SIZE, event.y // CELL_SIZE
    
    if target_x in range(ROWS_NUM) and target_y in range(COLS_NUM):
        if not CELLS_STATE[target_x, target_y]:
            CELLS_STATE[target_x, target_y] = 1
            color = "black"
        else:
            CELLS_STATE[target_x, target_y] = 0
            color = "white"
        
        CELLS[target_x, target_y] = create_cell(target_x, target_y, color)
        
        
def generate_cells(*args):
    global canvas, CELLS, CELLS_STATE, COLS_NUM, ROWS_NUM
    
    CELLS_STATE = np.zeros((ROWS_NUM, COLS_NUM))
    #CELLS_STATE = np.array([randint(0, 1) for _ in range(ROWS_NUM * COLS_NUM)]).reshape(ROWS_NUM, COLS_NUM)
    CELLS = np.zeros((ROWS_NUM, COLS_NUM))

    for i in range(ROWS_NUM):
        for j in range(COLS_NUM):
            color = "black" if CELLS_STATE[i, j] else "white"
            CELLS[i, j] = create_cell(i, j, color)
    
    canvas.focus_set()
    canvas.bind("<Button-1>", set_cell)
    

def generate_canvas(*args):
    global canvas, CELLS, ROWS_NUM, COLS_NUM, CELL_SIZE
    
    try:
        cell_size = int(cell_size_btn.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid size type (must be integer).")
        return
    else:
        if cell_size < 10 or cell_size > 300:
            messagebox.showerror("Error", "The cells size must be between 10 and 300.")
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
    
    var_launch_stop_text.set("Launch Cycle")
    launch_stop_btn.configure(background="green")
    
    generate_cells()
    
    hide_canvas_setting_buttons()
    
    show_game_managing_buttons()
    
            
def refresh_window(*args):
    global canvas
    
    canvas.destroy()
    
    hide_game_managing_buttons()
    
    show_canvas_setting_buttons()
    
    
def set_speed(*args):
    global CYCLE_SPEED, speed_entry
    
    try:
        speed = int(speed_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid speed (must be integer).")
        return
    
    CYCLE_SPEED = abs(speed)
        
    

label = tk.Label(buttons_frame, 
                 text="Choose the cells size\n (from 10 to 300)",
                 height=3
                 )

cell_size_btn = tk.Spinbox(buttons_frame,
                           from_=10,
                           to=300,
                           width=3,
                           wrap=True
                           )

canvas_generator_btn = tk.Button(buttons_frame,
                               text="Generate Cells",
                               width=button_width,
                               height=button_height,
                               command=generate_canvas
                               )

launch_stop_btn = tk.Button(buttons_frame, 
                             textvariable=var_launch_stop_text,
                             background="green",
                             overrelief="groove",
                             width=button_width,
                             height=button_height,
                             command=launch_stop
                             )


speed_entry = tk.Entry(buttons_frame,
                     width=5,
                     justify="left",
                     textvariable=var_speed
                     )


speed_btn = tk.Button(buttons_frame,
                      text="Set Speed (ms)",
                      width=button_width,
                      height=button_height,
                      command=set_speed
                      )


refresh_btn = tk.Button(buttons_frame,
                        text="Refresh",
                        width=button_width,
                        height=button_height,
                        command=refresh_window
                        )

exit_btn = tk.Button(buttons_frame, 
                     text="Exit",
                     width=button_width,
                     height=button_height,
                     command=warning
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
    launch_stop_btn.grid(column=1, pady=button_pady_2)
    
    var_speed.set("100")
    
    speed_entry.grid(column=1)
    
    speed_btn.grid(column=1, pady=button_pady_1)

    refresh_btn.grid(column=1, pady=button_pady_2)
    
    exit_btn.grid(column=1, pady=button_pady_2)
    
    
def hide_game_managing_buttons():
    launch_stop_btn.grid_forget()
    
    speed_entry.grid_forget()
    
    speed_btn.grid_forget()

    refresh_btn.grid_forget()
    
    exit_btn.grid_forget()
    
            

buttons_frame.pack(side="right", padx=30, fill="y")
show_canvas_setting_buttons()
window.mainloop()