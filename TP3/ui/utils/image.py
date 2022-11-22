import pygame as pg


class Image:
    def __init__(self, image, width, height) -> None:
        self.image = pg.transform.scale(image, (int(width), int(height)))
        self.rectangle = image.get_rect()
        self.rectangle.topleft = (0, 0)

    def draw(self, screen):
        screen.blit(self.image, (self.rectangle.x, self.rectangle.y))
