from signal import simpson_points
from fourier import dft
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


def main():
    global simpson_points
    simpson_points = [
        {"x": i["x"] * -1, "y": i["y"] * -1 - 100} for i in simpson_points[::2]
    ]
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    turtle.delay(0)
    win = turtle.Screen()

    epicycles = dft(simpson_points)

    time = 0
    dt = (math.pi * 2) / len(simpson_points)
    points = []
    while True:
        pen.reset()
        win.tracer(False)
        points.append(draw_epicycles(pen, 0, 0, time, epicycles, 0))
        for i in range(len(points) - 1):
            draw_line(pen, points[i], points[i + 1])
        time += dt
        win.update()

    turtle.done()


if __name__ == "__main__":
    main()
