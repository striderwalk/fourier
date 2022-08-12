"""
 needed to ataction [letter|words] together
 and to make new lines
"""


def __shifter(old_points, new_points, WIDTH, new_line=False):
    # shift points to correct place
    global line_num
    shifted_points = []

    # check for new line
    if old_points[-1][-1][-1]["x"] > WIDTH - 100 or new_line:
        line_num += 1
        oldp = {"x": 0, "y": line_num * 125}
    else:
        # last point should is heights in x
        # shift by last point + gap
        oldp = {"x": old_points[-1][-1][-1]["x"] + 5, "y": line_num * 125}

    # move letter into place
    for i in new_points:
        shifted_points.append({"x": oldp["x"] + i["x"], "y": i["y"] + oldp["y"]})
    if shifted_points[-1]["x"] < WIDTH - 100:
        return shifted_points
    else:
        return __shifter(old_points, new_points, i, WIDTH, new_line=True)



def link(paths, size):
    # max width of text
    WIDTH, HEIGHT = size
    lines = [[paths[0]]]
    global line_num
    line_num = 0
    for i in range(1, len(paths)):
        # dline to check for new line
        dline = line_num
        points = __shifter(lines, paths[i], WIDTH)
        if dline != line_num:
            lines.append([])
        lines[-1].append(points)

    # join all letters into one list
    paths = []
    for points in lines:
        for i in points:
            paths.extend(i)
    indexs = [0]
    
    # paths = [{"x": i["x"], "y": i["y"]} for i in paths]
    return indexs, paths
