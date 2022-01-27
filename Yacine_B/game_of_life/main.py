import tkinter as tk
from start_configs import *
from tkinter import messagebox


window = tk.Tk()

screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

window_width = int(WINDOW_WIDTH_RATIO * screen_width)
window_height = int(WINDOW_HEIGHT_RATIO * screen_height)

gap_x = (screen_width - window_width) // 2
gap_y = (screen_height - window_height) // 2

button_width = int(window_width * BUTTON_WIDTH_RATIO)
button_height = int(window_height * BUTTON_HEIGHT_RATIO)

canvas_width = adapt_canvas(window_width * CANVAS_WIDTH_RATIO)
canvas_height = adapt_canvas(window_height * CANVAS_HEIGHT_RATIO)



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

def resize_cells(*args):
    CELL_SIZE = cell_size_btn.get()


label = tk.Label(buttons_frame, 
                 text="Choose the cells size\n (from 3 to 300)",
                 height=3
                 )

cell_size_btn = tk.Spinbox(buttons_frame,
                           from_=3,
                           to=300,
                           width=3,
                           wrap=True,
                           command=resize_cells
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

exit_btn = tk.Button(buttons_frame, 
                     text="Exit",
                     command=warning,
                     width=button_width,
                     height=button_height
                     )
    
   
    
buttons_frame.pack(side="right", padx=30, fill="y")

label.grid(column=1)

cell_size_btn.grid(column=1)

launch_pause_btn.grid(column=1, pady=150)

next_btn.grid(column=1)

previous_btn.grid(column=1, pady=25)

exit_btn.grid(column=1, pady=250)



window.mainloop()