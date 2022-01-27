from main import *

canvas = tk.Canvas(window, 
                width=canvas_width, 
                height=canvas_height,
                background="white"
                )

canvas.pack(side="left",
            pady=(window_height - int(canvas.cget("height")) ) // 2
            )


def generate_cell(i, j, color):
    canvas.create_rectangle(i*CELL_SIZE, j*CELL_SIZE, 
                            (i+1)*CELL_SIZE, (j+1)*CELL_SIZE,
                            fill=color)
    
    
def trace_grid():
    for i in range(canvas_width//CELL_SIZE):
        for j in range(canvas_height//CELL_SIZE):
            color = ALIVE_CELL_COLOR if i==j else DEAD_CELL_COLOR
            generate_cell(i, j, color)
        

trace_grid()