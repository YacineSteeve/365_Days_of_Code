import numpy as np

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 980

CELL_SIZE = 7

CELLS = np.zeros((140, 200))

CELLS_POS = np.array([
    [(-700 + x * CELL_SIZE, 490 - y * CELL_SIZE) for x in range(200)] 
                      for y in range(140)])


if __name__ == '__main__':
    print(CELLS_POS)
