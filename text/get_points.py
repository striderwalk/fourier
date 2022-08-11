"""
https://stackoverflow.com/questions/69313876/how-to-get-points-of-the-svg-pathsfrom svg.path import parse_path
"""

from svg.path import parse_path
from xml.dom import minidom


def get_point_at(path, distance, scale, offset):
    pos = path.point(distance)
    pos += offset
    pos *= scale
    return pos.real, pos.imag


def points_from_path(path, density, scale, offset):
    step = int(path.length() * density)
    last_step = step - 1

    if last_step == 0:
        yield get_point_at(path, 0, scale, offset)
        return

    for distance in range(step):
        yield get_point_at(path, distance / last_step, scale, offset)


def points_from_doc(doc, density=5, scale=1, offset=0):
    offset = offset[0] + offset[1] * 1j
    points = []
    for element in doc.getElementsByTagName("path"):
        for path in parse_path(element.getAttribute("d")):
            points.extend(points_from_path(path, density, scale, offset))

    return points


def line(points, name):
    # check not desender
    if name in ["g", "j", "q", "p", "y"]:
        return points

    max_y = max(points, key=lambda x: x["y"])["y"]
    ## line = 245
    diff = 245 - max_y
    return [{"x": i["x"], "y": i["y"] + diff} for i in points]


def back(points):
    min_x = min(points, key=lambda x: x["x"])["x"]
    return [{"x": i["x"] - min_x, "y": i["y"]} for i in points]


def get(data):
    name, doc = data
    points = points_from_doc(doc, density=1, scale=5, offset=(0, 5))
    points = [{"x": i[0], "y": i[1]} for i in points]
    points.append(points[0])
    points.insert(0, points[-2])
    points = line(points, name)
    points = back(points)
    doc.unlink()
    points = [{"x": i["x"] / 3, "y": i["y"] / 3} for i in points]
    return [name, points]
