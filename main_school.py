from signal import simpson_points as points
from fourier import dft
from text import get
import turtle
import math


def draw_circle(pen, center, radius, width):
    # move
    pen.up()
    pen.goto(center)
    pen.pensize(width)
    pen.setheading(90)
    pen.forward(radius)
    pen.left(90)
    pen.down()
    # circle
    pen.circle(radius)


def draw_line(pen, start, end):
    pen.up()
    pen.goto(start)
    pen.down()
    pen.goto(end)


def draw_epicycles(pen, x, y, time, fourier, rotation):
    # draw each circle and line
    for i in range(len(fourier)):
        prevx = x
        prevy = y
        freq = fourier[i]["freq"]
        radius = fourier[i]["amp"]
        phase = fourier[i]["phase"]
        x += radius * math.cos(freq * time + phase + rotation)
        y += radius * math.sin(freq * time + phase + rotation)
        draw_circle(pen, (prevx, prevy), radius, 1)
        draw_line(pen, (x, y), (prevx, prevy))

    return (x, y)


def find_dis(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def main():

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    turtle.delay(0)

    win = turtle.Screen()
    _, points = get(None, win.textinput, ["what would you like to write", "hello"])
    points = [{"x": i["x"], "y": i["y"] * -1 - 110} for i in points[::3]]
    epicycles = dft(points)

    time = 0
    dt = (math.pi * 2) / len(points)
    pen.reset()
    win.tracer(False)
    pen.color("blue")
    pen.pensize(1)
    pointss = [[draw_epicycles(pen, 0, 0, time, epicycles, 0)]]
    while True:
        pen.reset()
        win.tracer(False)
        pen.color("blue")
        pen.pensize(1)
        x = draw_epicycles(pen, 0, 0, time, epicycles, 0)
        if find_dis(x, pointss[-1][-1]) > 25:
            pointss.append([])
        pointss[-1].append(x)

        pen.color("black")
        pen.pensize(2)
        for points in pointss:
            for i in range(len(points) - 1):
                draw_line(pen, points[i], points[i + 1])
        time += dt
        win.update()

    turtle.done()


if __name__ == "__main__":

    main()
