import make_svg
import get_points
import json
import concurrent.futures as futures
import timeit
import time


def set():
    docs = make_svg.make("C:/Windows/Fonts/COMIC.TTF")
    letters = {}
    with futures.ProcessPoolExecutor() as executor:
        res = executor.map(get_points.get, docs)

    letters[" "] = [{"x": 0, "y": 0}, {"x": 75.0, "y": 0}]
    for i in res:
        letters[i[0]] = i[1]

    with open("letters.json", "w") as file:
        json.dump(letters, file, indent=3)


if __name__ == "__main__":
    set()
