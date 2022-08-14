from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame  # import after disabling prompt
import math
import random
from fourier import dft

# from signal import simpson_points
from get_signal import get_signal
from text import get
from text import *
from draw import draw, menu
from conts import WIDTH, HEIGHT


def main():
    # set up pygame
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 30, False, False)

    run = True
    while run:
        # data = *get(win, "hello"), 0
        data = menu(win, clock, font)

        indexs, lis, mode = data
        points = dft(lis)
        if draw(win, clock, indexs, points, data[1], mode) != "reset":
            run = False

    pygame.quit()


if __name__ == "__main__":
    main()
