from Fractal.drawLine import draw_triangle
from PIL import Image
import random as rand
import numpy as np
import math
import sys

sys.setrecursionlimit(10**7)


def randInTriangle(pixels, bottomLeft, bottomRight, top, colour):
    n = (bottomRight[0] - bottomLeft[0]) / 2
    xCrd = rand.randint(bottomLeft[0], bottomRight[0])
    rHeight = n * math.sqrt(3) - abs(xCrd - n - 100) * math.sqrt(3) + 1
    yCrd = rand.randint(math.ceil(bottomLeft[1] - rHeight), math.floor(bottomLeft[1]))
    pixels[yCrd][xCrd] = colour
    currentPoint = [xCrd, yCrd]
    return pixels, bottomLeft, bottomRight, top, currentPoint


def randVertex(
    pixels, bottomLeft, bottomRight, top, currentPoint, colour, iteration, count
):
    vertices = [bottomLeft, bottomRight, top]
    if iteration <= 10**6:
        randomVertex = rand.choice(vertices)
        xCrd = round((currentPoint[0] + randomVertex[0]) / 2)
        yCrd = round((currentPoint[1] + randomVertex[1]) / 2)
        pixels[yCrd][xCrd] = colour
        currentPoint = [xCrd, yCrd]
        iteration += 1
        # if iteration % (2 * (10**1)) == 0 and iteration <= 10**3:
        #     img = Image.fromarray(pixels)
        #     img.save(f"tri_Fractal{count}.png")
        #     count += 1
        # elif iteration % (2 * (10**2)) == 0 and 10**3 < iteration <= 10**4:
        #     img = Image.fromarray(pixels)
        #     img.save(f"tri_Fractal{count}.png")
        #     count += 1
        # elif iteration % (2 * (10**3)) == 0 and 10**4 < iteration <= 10**5:
        #     img = Image.fromarray(pixels)
        #     img.save(f"tri_Fractal{count}.png")
        #     count += 1
        # elif iteration % (2 * (10**4)) == 0 and 10**5 < iteration <= 10**6:
        #     img = Image.fromarray(pixels)
        #     img.save(f"tri_Fractal{count}.png")
        #     count += 1
        randVertex(
            pixels, bottomLeft, bottomRight, top, currentPoint, colour, iteration, count
        )


pixels = np.zeros((1000, 1000, 3), dtype=np.uint8)

triangle = draw_triangle([500, 500], 800, 1, [0, 130, 200], pixels)

randPoint = randInTriangle(
    triangle[0], triangle[1], triangle[2], triangle[3], [120, 0, 220]
)

randVertex(
    randPoint[0],
    randPoint[1],
    randPoint[2],
    randPoint[3],
    randPoint[4],
    [120, 0, 220],
    1,
    1,
)

img = Image.fromarray(pixels)
img.show()
# img.save("tri_Fractal0.png")
