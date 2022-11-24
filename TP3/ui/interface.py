import numpy as np
import pygame as pg
import matplotlib.pyplot as plt

from .utils.image import Image
from .utils.variables import *


def set_interface(screen):
    screen.fill(BLACK)


def scale(value, max_value):
    return np.interp(value, (0, max_value), (MIN_RANGE, MAX_RANGE))


class Interface:
    def __init__(self, predict, input_width, input_height, num_channels) -> None:
        self.image = pg.image.load(IMAGE_PATH)
        self.image_width = self.image.get_width() * SCALE
        self.image_height = self.image.get_height() * SCALE
        self.predict = predict
        self.show = True
        self.converted_image = None
        self.clicked_image = None
        self.clicked_image_width = input_width
        self.clicked_image_height = input_height
        self.num_channels = num_channels

    def set_image(self, screen):
        self.converted_image.draw(screen)
        pg.display.update()

    def get_scaled_positions(self, pos):
        x, y = pos[0], pos[1]
        return scale(x, self.image_width), MAX_RANGE - scale(y, self.image_height)

    def show_interface(self):
        pg.init()
        screen = pg.display.set_mode((self.image_width *2, self.image_height))
        pg.display.set_caption(CAPTION)
        icon = pg.image.load(ICON_PATH)
        pg.display.set_icon(icon)
        set_interface(screen)
        self.converted_image = Image(self.image.convert(), self.image_width, self.image_height, ZERO, ZERO)
        self.set_image(screen)

        while self.show:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONUP:
                    pos = pg.mouse.get_pos()
                    if pos[0] <= self.image_width:
                        x, y = self.get_scaled_positions(pos)
                        decoded = self.predict(np.array([[x, y]]))
                        image = decoded.reshape(self.clicked_image_width, self.clicked_image_height, self.num_channels)
                        plt.imshow(image)
                        plt.axis('off')
                        plt.savefig('TP3/ui/utils/images/click.png', bbox_inches='tight', pad_inches=0)
                        self.clicked_image = Image(pg.image.load('TP3/ui/utils/images/click.png').convert(),
                                                   self.image_width, self.image_height, self.image_width, ZERO)
                        self.clicked_image.draw(screen)
                        pg.display.update()

                if event.type == pg.QUIT:
                    pg.quit()
                    pg.display.quit()
                    self.show = False
