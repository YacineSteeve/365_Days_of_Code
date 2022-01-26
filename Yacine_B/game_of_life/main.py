import tkinter as tk
from start_configs import *


window = tk.Tk()
    
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

window_width = int(WINDOW_WIDTH_RATIO * screen_width)
window_height = int(WINDOW_HEIGHT_RATIO * screen_height)


def set_window():
    global window, window_width, window_height, screen_width, screen_height
    
    window.title("Game of Life")
    
    gap_x = (screen_width - window_width) // 2
    gap_y = (screen_height - window_height) // 2
    
    window.geometry(f"{window_width}x{window_height}+{gap_x}+{gap_y}")
    
    window.resizable(False, False)

    window.mainloop()


def watcher(*args):
    state = "Launch" if var_launch_pause.get() == "Pause" else "Pause"
    var_launch_pause.set(state)
    

canvas = tk.Canvas(window, 
                   width=window_width*CANVAS_WIDTH_RATIO, 
                   height=window_height*CANVAS_HEIGHT_RATIO,
                   background="white")

var_launch_pause = tk.StringVar()
var_launch_pause.set("Launch")
    
buttons_frame = tk.Frame(window)
exit_btn = tk.Button(buttons_frame, text="Exit")
next_btn = tk.Button(buttons_frame, text="Next")
previous_btn = tk.Button(buttons_frame, text="Previous")
launch_pause_btn = tk.Button(buttons_frame, 
                             textvariable=var_launch_pause, 
                             command=watcher
                             )
    
buttons_frame.pack(side="right", fill="y")

launch_pause_btn.grid(column=1)
next_btn.grid(column=1)
previous_btn.grid(column=1)
exit_btn.grid(column=1)

canvas.pack(side="left", padx=10, 
            pady=(window_height - int(canvas.cget("height")) ) // 2
            )

set_window()
