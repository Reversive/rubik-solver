from enum import Enum

class Directions(Enum):
    NULL=-1

    TOP_RIGHT = 5
    TOP_LEFT = 7

    LEFT_UP = 4
    LEFT_DOWN = 8
    
    RIGHT_UP = 9
    RIGHT_DOWN = 3

    BOTTOM_LEFT = 10
    BOTTOM_RIGHT = 2
    
    FRONT_ROTATE_ANTICLOCKWISE = 11
    FRONT_ROTATE_CLOCKWISE = 1
    
    BACK_ROTATE_ANTICLOCKWISE = 12
    BACK_ROTATE_CLOCKWISE = 0
    