import cmath
import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()


def drawHomes():
    t1.up()
    t1.forward(100)
    t1.down()

    t2.up()
    t2.backward(400)
    t2.down()
    home(t1, t2)

    turtle.done()


def foundation(turt1, turt2):
    turt1.right(90)
    turt2.right(90)
    turt1.forward(200)
    turt2.forward(200)
    turt1.left(90)
    turt2.left(90)
    turt1.forward(300)
    turt2.forward(300)
    turt1.left(90)
    turt2.left(90)
    turt1.forward(200)
    turt2.forward(200)
    turt1.left(90)
    turt2.left(90)
    turt1.forward(300)
    turt2.forward(300)
    turt1.right(90)
    turt2.right(90)


def door(turt1, turt2):
    turt1.right(90)
    turt2.right(90)
    turt1.forward(90)
    turt2.forward(90)
    turt1.left(90)
    turt2.left(90)
    turt1.forward(40)
    turt2.forward(40)
    turt1.left(90)
    turt2.left(90)
    turt1.forward(90)
    turt2.forward(90)
    turt1.left(90)
    turt2.left(90)
    turt1.forward(40)
    turt2.forward(40)
    turt1.right(90)
    turt2.right(90)


def roof(turt1, turt2):
    turt1.right(45)
    turt2.right(45)
    turt1.forward(150 * cmath.sqrt(2).real)
    turt2.forward(150 * cmath.sqrt(2).real)
    turt1.right(90)
    turt2.right(90)
    turt1.forward(150 * cmath.sqrt(2).real)
    turt2.forward(150 * cmath.sqrt(2).real)


def window(turt1, turt2):
    turt1.right(90)
    turt2.right(90)
    turt1.forward(50)
    turt2.forward(50)
    turt1.left(90)
    turt2.left(90)
    turt1.forward(70)
    turt2.forward(70)
    turt1.left(90)
    turt2.left(90)
    turt1.forward(50)
    turt2.forward(50)
    turt1.left(90)
    turt2.left(90)
    turt1.forward(70)
    turt2.forward(70)
    turt1.right(90)
    turt2.right(90)


def home(turt1, turt2):
    foundation(turt1, turt2)
    roof(turt1, turt2)
    turt1.right(45)
    turt2.right(45)
    turt1.forward(200)
    turt2.forward(200)
    turt1.right(90)
    turt2.right(90)
    turt1.forward(130)
    turt2.forward(130)
    door(turt1, turt2)
    turt1.up()
    turt2.up()
    turt1.left(180)
    turt2.left(180)
    turt1.forward(100)
    turt2.forward(100)
    turt1.down()
    turt2.down()
    turt1.left(90)
    turt2.left(90)
    window(turt1, turt2)
