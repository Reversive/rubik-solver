import pygame as pg
from .utils.variables import *


def set_interface(screen):
    screen.fill(LIGHT_BLUE)


class Interface:
    def __init__(self) -> None:
        self.show = True
        self.image = pg.image.load(IMAGE_PATH)
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()

    def set_image(self, screen):
        rectangle = self.image.get_rect()
        rectangle.topleft = (0, 0)
        screen.blit(self.image, (rectangle.x, rectangle.y))
        pg.display.flip()

    def handle_image(self, scale):
        self.image = self.image.convert()
        self.image = pg.transform.scale(self.image, (int(self.image_width * scale), int(self.image_height * scale)))

    def show_interface(self):
        pg.init()
        screen = pg.display.set_mode((self.image_width, self.image_height/2))
        pg.display.set_caption(CAPTION)
        icon = pg.image.load(ICON_PATH)
        pg.display.set_icon(icon)
        set_interface(screen)
        self.handle_image(0.5)
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
