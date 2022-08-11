import math
from point import Point
import numpy as np
from tqdm import tqdm


def dft(x):
    if len(x) > 3000:
        print(f"WARNING: over 3000 points - {len(x)} points")
    x = [complex(i["x"], i["y"]) for i in x]
    X = []
    N = len(x)
    for k in range(N):
        sum_pos = complex(0, 0)
        for n in range(N):
            phi = (math.pi * 2 * k * n) / N
            c = complex(math.cos(phi), -math.sin(phi))
            sum_pos += x[n] * c

        x_pos = sum_pos.real / N
        y_pos = sum_pos.imag / N

        freq = k
        amp = abs(complex(x_pos, y_pos))
        phase = math.atan2(y_pos, x_pos)
        if freq > 0:
            X.append(
                {"re": x_pos, "im": y_pos, "freq": freq, "amp": amp, "phase": phase}
            )
    X.sort(key=lambda x: -x["amp"])
    return X
