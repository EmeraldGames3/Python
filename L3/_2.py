import turtle


def curve():
    for i in range(50):
        turtle.right(4)
        turtle.forward(4)


def drawHeart():
    turtle.left(140)
    turtle.forward(113)

    curve()
    turtle.left(120)
    curve()

    turtle.forward(113)

    turtle.done()

