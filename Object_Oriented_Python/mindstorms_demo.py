import turtle

from Object_Oriented_Python import mindstorms as ms


window = turtle.Screen()
tortschwar = turtle.Turtle()

# ms.draw_square_circle(tortschwar, 10)
# ms.draw_triangle_circle(tortschwar, 10)
# ms.draw_circle_circle(tortschwar, 10)
# ms.draw_polygon(tortschwar, 9)
ms.draw_flower(tortschwar, 50, 80, 20)

window.exitonclick()
