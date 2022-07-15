
# Initializing some constants in order to adapt the window 
#   and its widgets sizes to each screen when the app is running.

WINDOW_WIDTH_RATIO = 0.75
WINDOW_HEIGHT_RATIO = 0.85

CANVAS_WIDTH_RATIO = 0.80
CANVAS_HEIGHT_RATIO = 0.90

BUTTON_WIDTH_RATIO = 0.01
BUTTON_HEIGHT_RATIO = 0.003

PADY_RATIO_1 = 0.02
PADY_RATIO_2 = 0.12


# Global elements to represent the cells and their state at each generation.

canvas = None   # is initialized when the canvas is generated for the first time.

CELLS_STATE = []
CELLS = []


# Global variables (with default values) which can be set/modified
#   either by the user or the program itself.

ROWS_NUM = 1
COLS_NUM = 1
CELL_SIZE = 1
CYCLE_SPEED = 100
