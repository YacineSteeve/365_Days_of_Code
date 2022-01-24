import turtle
from start_configs import *


turtle.title("Game of Life")
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)


def draw_bow(location):
    turtle.up()
    turtle.goto(*location)
    turtle.down()
    for _ in range(3):
        turtle.forward(CELL_SIZE)
        turtle.right(90)
    turtle.right(90)
        

def draw_grid():
    for line in CELLS_POS:
        for pos in line:
            draw_bow(pos)
            

while True:
    draw_grid()
    turtle.getscreen()