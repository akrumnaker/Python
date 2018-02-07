# This python script contains various functions to draw
# shapes using the turtle module of python

def draw_square(turt):
    """
    Draw a square using the Turtle object turt
    :param turt: a Turtle class instance used to draw a square
    :return: None
    """
    turt.shape("square")
    turt.fillcolor("green")
    turt.speed(8)
    for i in range(4):
        turt.forward(150)
        turt.right(90)


def draw_circle(turt):
    """
    Draw a circle using the built-in function of the Turtle class
    :param turt: a Turtle class instance used to draw a circle
    :return: None
    """
    turt.shape("circle")
    turt.fillcolor("blue")
    turt.speed(8)
    turt.circle(50)


def draw_triangle(turt):
    """
    Draw a triangle using the Turtle object turt
    :param turt: a Turtle class instance used to draw a triangle
    :return: None
    """
    turt.shape("triangle")
    turt.fillcolor("red")
    turt.speed(8)
    turt.right(120)

    for i in range(3):
        turt.forward(100)
        turt.right(120)


def draw_polygon(turt, num_sides):
    """
    Draws a polygon with num_sides sides
    :param turt: a Turtle class instance used to draw the polygon
    :param num_sides: the number of sides the polygon will have (integer)
    :return: None
    """
    degrees = 360 // num_sides
    length = 1000 // num_sides

    turt.shape("classic")
    turt.fillcolor("purple")
    turt.speed(8)

    for i in range(num_sides):
        turt.forward(length)
        turt.right(degrees)


def draw_square_circle(turt, degrees):
    """
    Draw a circle by drawing multiple squares
    :param turt: a Turtle class instance used to draw the squares
    :param degrees: number of degrees to rotate between squares (integer)
    :return: None
    """
    for i in range(360//degrees):
        draw_square(turt)
        turt.right(degrees)


def draw_triangle_circle(turt, degrees):
    """
    Draw a circle by drawing multiple triangles
    :param turt: a Turtle class instance used to draw the triangles
    :param degrees: number of degrees to rotate between triangles (integer)
    :return: None
    """
    for i in range(360//degrees):
        draw_triangle(turt)
        turt.right(degrees)


def draw_circle_circle(turt, degrees):
    """
    Draw a circle by drawing multiple circles
    :param turt: a Turtle class instance used to draw the circles
    :param degrees: number of degrees to rotate between circles (integer)
    :return: None
    """
    for i in range(360//degrees):
        draw_circle(turt)
        turt.right(degrees)


def draw_polygon_circle(turt, degrees, sides):
    """
    Draws a circle by drawing multiple n-sided polygons
    :param turt: a Turtle class instance used to draw the polygons
    :param degrees: number of degrees to rotate between polygons (integer)
    :param sides: number of sides for the polygon (integer)
    :return: None
    """
    for i in range(360//degrees):
        draw_polygon(turt, sides)
        turt.right(degrees)


def draw_petal(turt, side_length, deg1, deg2):
    """
    Draws a four sided petal
    :param turt: a Turtle class instance used to draw the petal
    :param side_length: the length of each side of the petal (integer)
    :param deg1: the first complementary angle (integer)
    :param deg2: the second complementary angle (integer)
    :return: None
    """
    turt.shape("classic")
    turt.fillcolor("purple")
    turt.speed(8)

    for i in range(4):
        turt.forward(side_length)
        if i % 2 == 0:
            turt.right(deg1)
        else:
            turt.right(deg2)


def draw_flower(turt, side_length, degrees, num_petals, overlapping=True):
    """
    Draws multiple petals to create a flower with a stem
    :param turt: a Turtle class instance used to draw each petal comprising the flower
    :param side_length: the length of each side of the petal (integer)
    :param degrees: the degrees dictating how wide the petal will be (integer)
    :param num_petals: number of petals the flower will have (integer)
    :param overlapping: whether the petals should overlap or not (boolean)
    :return:
    """
    comp_degrees = 180 - degrees

    for i in range(360 // num_petals):
        draw_petal(turt, side_length, degrees, comp_degrees)
        turt.right(num_petals)

    turt.right(90)
    turt.forward(side_length + 150)
