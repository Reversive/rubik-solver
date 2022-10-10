import pygame as pg


class Button:
    def __init__(self, x, y, image, scale) -> None:
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rectangle = self.image.get_rect()
        self.rectangle.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, (self.rectangle.x, self.rectangle.y))
