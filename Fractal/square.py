from Fractal.drawLine import plot_line
from PIL import Image
import random as rand
import numpy as np
import sys

sys.setrecursionlimit(10**7)


def draw_square(center, side_lenght, pixels, colour):
    topLeft = [(center[0] - side_lenght / 2), (center[1] - side_lenght / 2)]

    topRight = [(center[0] + side_lenght / 2), (center[1] - side_lenght / 2)]

    bottomLeft = [(center[0] - side_lenght / 2), (center[1] + side_lenght / 2)]

    bottomRight = [(center[0] + side_lenght / 2), (center[1] + side_lenght / 2)]

    plot_line(topLeft, topRight, 1, colour, pixels)
    plot_line(bottomLeft, bottomRight, 1, colour, pixels)
    plot_line(topLeft, bottomLeft, 1, colour, pixels)
    plot_line(topRight, bottomRight, 1, colour, pixels)

    return pixels, topLeft, topRight, bottomLeft, bottomRight


def checkProx(center, side_lenght, currentPoint):
    smSide = side_lenght / 3
    x = 1
    topLeftCenter = [(center[0] - x * smSide), (center[1] - x * smSide)]
    topMidCenter = [center[0], (center[1] - x * smSide)]
    topRightCenter = [(center[0] + x * smSide), (center[1] - x * smSide)]
    midLeftCenter = [(center[0] - x * smSide), center[1]]
    midRightCenter = [(center[0] + x * smSide), center[1]]
    botLeftCenter = [(center[0] - x * smSide), (center[1] + x * smSide)]
    botMidCenter = [center[0], (center[1] + x * smSide)]
    botRightCenter = [(center[0] + x * smSide), (center[1] + x * smSide)]
    centerPoints = [
        topLeftCenter,
        topMidCenter,
        topRightCenter,
        botLeftCenter,
        botRightCenter,
        botMidCenter,
        midLeftCenter,
        midRightCenter,
    ]
    colours = [
        [148, 0, 211],
        [190, 0, 188],
        [221, 0, 161],
        [242, 0, 133],
        [255, 0, 104],
        [255, 0, 75],
        [255, 0, 45],
        [255, 0, 0],
    ]
    for smCenter in centerPoints:
        topLeft = [round((smCenter[0] - smSide / 2)), round((smCenter[1] - smSide / 2))]
        topRight = [
            round((smCenter[0] + smSide / 2)),
            round((smCenter[1] - smSide / 2)),
        ]
        bottomLeft = [
            round((smCenter[0] - smSide / 2)),
            round((smCenter[1] + smSide / 2)),
        ]

        if currentPoint[0] in range(topLeft[0], topRight[0] + 1):
            if currentPoint[1] in range(topLeft[1], bottomLeft[1] + 1):
                colour = colours[centerPoints.index(smCenter)]
                return colour


def randInSquare(pixels, topLeft, topRight, bottomLeft, bottomRight, colour):
    vertices = [topLeft, topRight, bottomLeft, bottomRight]
    midpoints = [
        [500, 200],
        [200, 500],
        [800, 500],
        [500, 800]
        # [(topRight[0] - topLeft[0] + 200), topLeft[1]],
        # [(bottomRight[0] - bottomLeft[0] + 200), bottomLeft[1]],
        # [topRight[0], (bottomRight[1] - topRight[1] - 200)],
        # [bottomLeft[0], (bottomLeft[1] - topLeft[1] - 200)],
    ]
    points = vertices + midpoints
    xCrd = rand.randint(bottomLeft[0], bottomRight[0])
    yCrd = rand.randint(topLeft[1], bottomLeft[1])
    pixels[yCrd][xCrd] = colour
    currentPoint = [xCrd, yCrd]
    return pixels, currentPoint, points, colour


def randPoint(pixels, currentPoint, points, colour, center, iteration, count):
    side_lenght = points[1][0] - points[0][0]
    if iteration <= 10**6:
        randomPoint = rand.choice(points)
        xCrd = round(currentPoint[0] + (randomPoint[0] - currentPoint[0]) * (2 / 3))
        yCrd = round(currentPoint[1] + (randomPoint[1] - currentPoint[1]) * (2 / 3))
        pixels[yCrd][xCrd] = colour
        currentPoint = [xCrd, yCrd]
        iteration += 1
        # if iteration % (2 * (10**1)) == 0 and iteration <= 10**3:
        #     img = Image.fromarray(pixels)
        #     img.save(f"sq_Fractal{count}.png")
        #     count += 1
        # elif iteration % (2 * (10**2)) == 0 and 10**3 < iteration <= 10**4:
        #     img = Image.fromarray(pixels)
        #     img.save(f"sq_Fractal{count}.png")
        #     count += 1
        # elif iteration % (2 * (10**3)) == 0 and 10**4 < iteration <= 10**5:
        #     img = Image.fromarray(pixels)
        #     img.save(f"sq_Fractal{count}.png")
        #     count += 1
        # elif iteration % (2 * (10**4)) == 0 and 10**5 < iteration <= 10**6:
        #     img = Image.fromarray(pixels)
        #     img.save(f"sq_Fractal{count}.png")
        #     count += 1
        randPoint(
            pixels,
            currentPoint,
            points,
            checkProx(center, side_lenght, currentPoint),
            center,
            iteration,
            count,
        )


pixels = np.zeros((1000, 1000, 3), dtype=np.uint8)
colour = [255, 0, 0]
square = draw_square([500, 500], 600, pixels, [255, 255, 255])
rPoint = randInSquare(square[0], square[1], square[2], square[3], square[4], colour)
randPoint(rPoint[0], rPoint[1], rPoint[2], colour, [500, 500], 1, 1)
img = Image.fromarray(pixels)
# img.save("sq_Fractal0.png")
img.show()
