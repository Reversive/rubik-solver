import pygame as pg

from .utils.image import Image
from .utils.variables import *


def set_interface(screen):
    screen.fill(LIGHT_BLUE)


class Interface:
    def __init__(self) -> None:
        self.image = pg.image.load(IMAGE_PATH)
        self.image_width = self.image.get_width() * SCALE
        self.image_height = self.image.get_height() * SCALE
        self.show = True
        self.converted_image = None

    def set_image(self, screen):
        self.converted_image.draw(screen)
        pg.display.flip()

    def show_interface(self):
        pg.init()
        screen = pg.display.set_mode((self.image_width / SCALE, self.image_height))
        pg.display.set_caption(CAPTION)
        icon = pg.image.load(ICON_PATH)
        pg.display.set_icon(icon)
        set_interface(screen)
        self.converted_image = Image(self.image.convert(), self.image_width, self.image_height)
        self.set_image(screen)

        while self.show:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONUP:
                    pos = pg.mouse.get_pos()
                    print(pos)

                if event.type == pg.QUIT:
                    pg.quit()
                    pg.display.quit()
                    self.show = False
