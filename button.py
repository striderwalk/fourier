import pygame
from conts import WIDTH, HEIGHT
from random import random

pygame.font.init()
font = pygame.font.SysFont(None, 24)


class Button:
    """
    a class to represent buttons
     - handle drawing
     - handle
    """

    def __init__(self, x, y, xsize, ysize, text, func, mode, dx=3, dy=3):
        self.rect = pygame.Rect(x, y, xsize, ysize)
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
        self.text = text
        self.func = func
        self.mode = mode
        self.xsize, self.ysize = xsize, ysize
        self.dx = dx
        self.dy = dy

    def draw(self, win):
        # draw button on screen
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            pygame.draw.rect(win, (20, 20, 25), self.rect, border_radius=3)
            img = font.render(self.text, True, (235, 235, 235))
        else:
            pygame.draw.rect(win, (235, 235, 235), self.rect, border_radius=3)
            img = font.render(self.text, True, (20, 20, 25))

        win.blit(
            img,
            (
                self.rect.centerx - img.get_size()[0] / 2,
                self.rect.centery - img.get_size()[1] / 2,
            ),
        )

    def check_click(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                action = True
        if action:
            return self.func, self.mode

    def update(self, others):
        self.x += self.dx
        self.y += self.dy
        self.rect.topleft = (self.x, self.y)

        if 0 > self.x or self.x + self.xsize > WIDTH:
            self.dx *= -1

        if 0 > self.y or self.y + self.ysize > HEIGHT:
            self.dy *= -1

        for other in others:
            if other is self:
                continue

            uppery = (
                self.rect.bottom >= other.rect.top
                and self.rect.bottom <= other.rect.bottom
            )
            upperx = (
                self.rect.right >= other.rect.left
                and self.rect.right <= other.rect.right
            )
            lowery = (
                self.rect.top <= other.rect.bottom and self.rect.top >= other.rect.top
            )
            lowerx = (
                self.rect.left <= other.rect.right
                and self.rect.right >= other.rect.right
            )

            if upperx or lowerx:
                if uppery or lowery:
                    self.dx *= -1 + (random() - 0.5) / 10

            if uppery or lowery:
                if upperx or lowerx:
                    self.dy *= -1 + (random() - 0.5) / 10
