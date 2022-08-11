def __linker(old, new, WIDTH, new_line=False):
    global line_num
    new_new = []

    # check for new line
    if old[-1][-1][-1]["x"] > WIDTH - 100 or new_line:
        line_num += 1
        oldp = {"x": 0, "y": line_num * 125}
    else:
        # last point should is heights in x
        # shift by last point + gap
        oldp = {"x": old[-1][-1][-1]["x"] + 5, "y": line_num * 125}

    # move letter into place
    for i in new:
        new_new.append({"x": oldp["x"] + i["x"], "y": i["y"] + oldp["y"]})
    if new_new[-1]["x"] < WIDTH - 100:
        return new_new
    else:
        return __linker(old, new, i, WIDTH, new_line=True)



def link(paths, size):
    # max width of text
    WIDTH, HEIGHT = size
    lines = [[paths[0]]]
    global line_num
    line_num = 0
    for i in range(1, len(paths)):
        # dline to check for new line
        dline = line_num
        points = __linker(lines, paths[i], WIDTH)
        if dline != line_num:
            lines.append([])
        lines[-1].append(points)

    # join all letters into one list
    paths = []
    for points in lines:
        for i in points:
            paths.extend(i)
    indexs = [0]

    paths = [{"x": i["x"], "y": i["y"]} for i in paths]
    return indexs, paths
