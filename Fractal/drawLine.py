import math


def plot_line(from_coordinates, to_coordinates, thickness, colour, pixels):

    max_x_coordinate = len(pixels[0])
    max_y_coordinate = len(pixels)


    horizontal_distance = to_coordinates[0] - from_coordinates[0]
    vertical_distance = to_coordinates[1] - from_coordinates[1]


    distance = math.sqrt(
        (to_coordinates[0] - from_coordinates[0]) ** 2
        + (to_coordinates[1] - from_coordinates[1]) ** 2
    )


    horizontal_step = horizontal_distance / distance
    vertical_step = vertical_distance / distance


    for i in range(round(distance)):
        current_x_coordinate = round(from_coordinates[0] + (horizontal_step * i))
        current_y_coordinate = round(from_coordinates[1] + (vertical_step * i))


        for x in range(-thickness, thickness):
            for y in range(-thickness, thickness):
                x_value = current_x_coordinate + x
                y_value = current_y_coordinate + y

                if (
                    x_value > 0
                    and x_value < max_x_coordinate
                    and y_value > 0
                    and y_value < max_y_coordinate
                ):
                    pixels[y_value][x_value] = colour


def draw_triangle(center, side_length, thickness, colour, pixels):

    triangle_height = round(side_length * math.sqrt(3) / 2)

    top = [center[0], center[1] - triangle_height / 2]

    bottom_left = [center[0] - side_length / 2, center[1] + triangle_height / 2]

    bottom_right = [center[0] + side_length / 2, center[1] + triangle_height / 2]

    plot_line(top, bottom_left, thickness, colour, pixels)
    plot_line(top, bottom_right, thickness, colour, pixels)
    plot_line(bottom_left, bottom_right, thickness, colour, pixels)
    return pixels, bottom_left, bottom_right, top