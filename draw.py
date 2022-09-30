from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import math
from conts import *
from text import get
from button import Button
from get_bee import get_bee
from get_signal import get_signal
from random import randint


def draw_epicycles(win, x, y, time, fourier, rotation):
    # draw each circle and line
    for i in range(len(fourier)):
        prevx = x
        prevy = y
        freq = fourier[i]["freq"]
        radius = fourier[i]["amp"]
        phase = fourier[i]["phase"]
        x += radius * math.cos(freq * time + phase + rotation)
        y += radius * math.sin(freq * time + phase + rotation)
        if radius > 1:
            pygame.draw.circle(win, BLUE, (prevx, prevy), radius, width=1)
        else:
            pygame.draw.circle(win, BLUE, (prevx, prevy), 1, width=1)
        pygame.draw.line(win, RED, (x, y), (prevx, prevy))

    return (x, y)


def recr_len(lst):
    return sum([len(i) for i in lst])

def check_points(p1, p2):
    # check if point are to close
    point_dis = math.hypot(p1[0] - p2[0], p1[1] - p2[1])

    if point_dis > 15:
        return True

    return False



def draw(win, clock, indexs, epicycles, signal, mode):
    # draw loop
    run = True
    time = 0
    dt = (math.pi * 2) / len(signal)
    new = draw_epicycles(win, XOFF, YOFF, time, epicycles, 0)
    # 2d list used to allow gaps (need for writing letters)
    line_points = [[new]]

    while run:
        # find next point
        new = draw_epicycles(win, XOFF, YOFF, time, epicycles, 0)
        # draw each line section
        for line in line_points:

            if len(line) > 1:
                pygame.draw.lines(win, BLACK, False, line, 2)
        # check in new section is needed

        if check_points(line_points[-1][-1], new):
            line_points.append([])
        # add point to current line section
        line_points[-1].append(new)

        if recr_len(line_points) > len(epicycles) or time / (math.pi * 2) == 1:
            time = 0
            new = draw_epicycles(win, XOFF, YOFF, time, epicycles, 0)
            line_points = [[new]]

        time += dt

        # update screen
        pygame.display.flip()
        win.fill(WHITE)

        clock.tick(mode)
        # check for input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "reset"

    return


def menu(win, clock, font):
    # buttons
    select_choices = [
        ("write something", get, 0),
        ("draw something", get_signal, 60),
        ("bees", get_bee, -1),
    ]
    buttons = []
    for index, i in enumerate(select_choices):
        buttons.append(
            Button(
                index * 150 + randint(0, 50),
                index * 200 + randint(0, 50),
                200,
                80,
                *i,
                randint(-3, 3),
                randint(-3, 3),
            )
        )
    select_type = False
    c = 0
    while not select_type:
        c += 1
        for i in buttons:
            i.draw(win)
            i.update(buttons)
            if res := i.check_click():
                return (*res[0](win), res[1])
        # update screen
        pygame.display.flip()
        win.fill(WHITE)

        clock.tick(60)

        # check for input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
