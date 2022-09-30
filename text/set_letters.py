import make_svg
import get_points
import json
import concurrent.futures as futures
import timeit
import time


def set():
    # convert fron to svg's
    docs = make_svg.make("C:/Windows/Fonts/COMIC.TTF")
    letters = {}
    # convert svg's to list of point
    with futures.ProcessPoolExecutor() as executor:
        letter_points = executor.map(get_points.get, docs)

    # space normally null - just using a gap
    letters[" "] = [{"x": 0, "y": 0}, {"x": 80.0, "y": 0}]
    for name, points in letter_points:
        letters[name] = points

    with open("letters.json", "w") as file:
        json.dump(letters, file, indent=3)


if __name__ == "__main__":
    set()
