from Fractal.drawLine import plot_line
from square import randPoint
from PIL import Image
import numpy as np
import math
import sys

sys.setrecursionlimit(10**7)


def drawHexagon(center, side_lenght, pixels, colour):
    topLeft = [
        (center[0] - side_lenght / 2),
        round((center[1] - side_lenght * math.sqrt(3) / 2)),
    ]
    topRight = [
        (center[0] + side_lenght / 2),
        round((center[1] - side_lenght * math.sqrt(3) / 2)),
    ]
    midLeft = [round((center[0] - side_lenght * math.sqrt(3) / 2)), center[1]]
    midRight = [round((center[0] + side_lenght * math.sqrt(3) / 2)), center[1]]
    bottomLeft = [
        (center[0] - side_lenght / 2),
        round((center[1] + side_lenght * math.sqrt(3) / 2)),
    ]
    bottomRight = [
        (center[0] + side_lenght / 2),
        round((center[1] + side_lenght * math.sqrt(3) / 2)),
    ]
    points = [topLeft, topRight, midLeft, midRight, bottomLeft, bottomRight]

    plot_line(topLeft, topRight, 1, colour, pixels)
    plot_line(topLeft, midLeft, 1, colour, pixels)
    plot_line(topRight, midRight, 1, colour, pixels)
    plot_line(midLeft, bottomLeft, 1, colour, pixels)
    plot_line(midRight, bottomRight, 1, colour, pixels)
    plot_line(bottomLeft, bottomRight, 1, colour, pixels)

    return points

colour = [0, 255, 0]
pixels = np.zeros((1000, 1000, 3), dtype=np.uint8)
hex = drawHexagon([500, 500], 500, pixels, [255, 255, 255])
randPoint(pixels, [500, 500], hex, colour, 1, 1)
img = Image.fromarray(pixels)
img.show()
