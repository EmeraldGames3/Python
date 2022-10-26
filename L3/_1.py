import turtle

l1 = 100
d1 = 200
l2 = 25
d2 = 50


def drawRectangles():
    turtle.up()
    turtle.goto(-40, 0)
    turtle.down()

    drawBigRectangle()

    turtle.up()
    turtle.goto(0, 100)
    turtle.down()

    drawSmallRectangle()

    turtle.done()


def drawBigRectangle():
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(l1)
        else:
            turtle.forward(d1)

        turtle.left(90)


def drawSmallRectangle():
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(l2)
        else:
            turtle.forward(d2)
        turtle.left(90)
