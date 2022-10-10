import pygame as pg
import numpy as np

from .utils.Button import Button

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NAVY_BLUE = (235, 245, 255)
WIDTH = 5
HEIGHT = 7
BLOCK_SIZE = 40
WINDOW_HEIGHT = HEIGHT * BLOCK_SIZE
WINDOW_WIDTH = WIDTH * BLOCK_SIZE + 150
SIDE_DIFF = WINDOW_WIDTH - WIDTH * BLOCK_SIZE
S_BUTTON_Y = WINDOW_HEIGHT * 7 / 8 - 50
R_BUTTON_Y = WINDOW_HEIGHT * 7 / 8 - 10


def write(text, screen, position, color, size):
    font = pg.font.Font(pg.font.get_default_font(), size)  # Defining a font with font and size
    text_surface = font.render(text, True, color)  # Defining the text color which will be rendered
    screen.blit(text_surface, (position[0], position[1]))  # Rendering the font


def set_board(screen):
    screen.fill(NAVY_BLUE)

    start_image = pg.image.load('TP2/multilayer_network/board/utils/start.png').convert_alpha()
    reset_image = pg.image.load('TP2/multilayer_network/board/utils/restart.png').convert_alpha()

    start_button = Button(WIDTH * BLOCK_SIZE + 25, S_BUTTON_Y, start_image, 2 / 12)
    reset_button = Button(WIDTH * BLOCK_SIZE + 20, R_BUTTON_Y, reset_image, 2 / 24)

    start_button.draw(screen)
    reset_button.draw(screen)
    write('The drawn number is', screen, (WIDTH * BLOCK_SIZE + 20, 15), BLACK, 12)


class NumbersBoard:
    def __init__(self, function) -> None:
        self.layers = []
        self.width = WIDTH
        self.height = HEIGHT
        self.show = True
        self.evaluate = function
        for x in range(self.width):
            self.layers.append([])
            for y in range(self.height):
                self.layers[x].append(0)

    def draw_grid(self, screen):
        block_size = BLOCK_SIZE
        for x in range(self.width):
            for y in range(self.height):
                rect = pg.Rect(x * (block_size + 1), y * (block_size + 1), block_size, block_size)
                color = BLACK if (self.layers[x][y] == 0) else WHITE
                pg.draw.rect(screen, color, rect)

    def reset(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                self.layers[x][y] = 0
        set_board(screen)

    def get_positions(self, pos):
        return int(pos[0] // ((WINDOW_WIDTH - SIDE_DIFF) / self.width)), int(pos[1] // (WINDOW_HEIGHT / self.height))

    def numbers_board(self):
        pg.init()
        screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pg.display.set_caption('SIA TP2 - Grupo 1')
        icon = pg.image.load('TP2/multilayer_network/board/utils/nn.png')
        pg.display.set_icon(icon)
        set_board(screen)
        output = '?'

        while self.show:
            self.draw_grid(screen)
            write(output, screen, (WIDTH * BLOCK_SIZE + 60, 50), BLACK, 50)
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONUP:
                    pos = pg.mouse.get_pos()
                    row, col = self.get_positions(pos)
                    if pos[0] <= WIDTH * BLOCK_SIZE:
                        self.layers[row][col] = 1 if self.layers[row][col] == 0 else 0
                    else:
                        if S_BUTTON_Y <= pos[1] < R_BUTTON_Y:
                            set_board(screen)
                            output = str(np.argmax(self.evaluate(np.asarray(np.matrix(self.layers).T).flatten())))
                        elif pos[1] >= R_BUTTON_Y:
                            self.reset(screen)
                            output = '?'

                if event.type == pg.QUIT:
                    pg.quit()
                    pg.display.quit()
                    self.show = False

            if self.show:
                pg.display.update()
