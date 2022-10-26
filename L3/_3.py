import turtle
import cmath

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1_dict = {
    "forward": t1.forward,
    "back": t1.backward,
    "left": t1.left,
    "right": t1.right,
}

t2_dict = {
    "forward": t2.forward,
    "back": t2.backward,
    "left": t2.left,
    "right": t2.right,
}


def upTogether():
    t1.up()
    t2.up()


def downTogether():
    t1.down()
    t2.down()


def moveTurtles(direction, n, speed):
    for i in range(int(n / speed)):
        t1_dict[direction](speed)
        t2_dict[direction](speed)


def rotateTurtles(direction, n):
    t1_dict[direction](n)
    t2_dict[direction](n)


def setUp():
    t1.up()
    t1.forward(100)
    t1.down()

    t2.up()
    t2.backward(400)
    t2.down()


def drawRect(l, d, speed):
    rotateTurtles("right", 90)

    for i in range(4):
        if i % 2 == 0:
            moveTurtles("forward", l, speed)
        else:
            moveTurtles("forward", d, speed)

        rotateTurtles("left", 90)


def foundation(speed):
    drawRect(200, 300, speed)


def roof(speed):
    rotateTurtles("right", 45)
    moveTurtles("forward", 150 * cmath.sqrt(2).real + 1, speed)
    rotateTurtles("right", 90)
    moveTurtles("forward", 150 * cmath.sqrt(2).real + 1, speed)


def door(speed):
    drawRect(90, 40, speed)


def window(speed):
    drawRect(50, 60, speed)


def drawHomes():
    setUp()

    foundation(5)
    rotateTurtles("right", 180)
    roof(5)

    upTogether()
    rotateTurtles("right", 45)
    moveTurtles("forward", 200, 10)
    rotateTurtles("right", 90)
    moveTurtles("forward", 130, 10)
    downTogether()

    door(5)

    upTogether()
    moveTurtles("forward", 150, 10)
    rotateTurtles("right", 90)
    moveTurtles("forward", 10, 10)
    downTogether()

    window(5)

    turtle.done()
