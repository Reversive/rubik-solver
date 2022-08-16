from enum import Enum

class Directions(Enum):
    NULL=0

    TOP_RIGHT = 1
    TOP_LEFT = -1

    LEFT_UP = 2
    LEFT_DOWN = -2
    
    RIGHT_UP = 3
    RIGHT_DOWN = -3

    BOTTOM_LEFT = 4
    BOTTOM_RIGHT = -4
    
    FRONT_ROTATE_ANTICLOCKWISE = 5
    FRONT_ROTATE_CLOCKWISE = -5
    
    BACK_ROTATE_ANTICLOCKWISE = 6
    BACK_ROTATE_CLOCKWISE = -6
    