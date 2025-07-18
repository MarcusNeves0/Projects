import turtle

BODY_COLOR = "PINK"
BODY_SHADOW = ""
GLASS_COLOR = '#9acedc'
GLASS_SHADOW = ""
BACKPACK_COLOR = 'red'
BACKPACK_SHADOW = ""

s = turtle.getscreen()
t = turtle.Turtle()

def body():
    t.pensize(15)

    t.fillcolor(BODY_COLOR)
    t.begin_fill()

    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)

    t.right(180)
    t.circle(100, -180)

    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)

    t.circle(40, -180)
    t.left(7)
    t.backward(50)

    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()
    t.right(240)
    t.circle(50, -70)

    t.end_fill()

def glass():
    t.up()
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)

    t.down()
    t.fillcolor(GLASS_COLOR)
    t.begin_fill()

    t.right(150)
    t.circle(90, -55)

    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)

    t.circle(50, -190)
    t.right(170)
    t.forward(80)

    t.right(180)
    t.circle(45, -30)

    t.end_fill()
    t.fillcolor(BODY_COLOR)
    t.begin_fill()

    t.end_fill()

def backpack():
    t.up()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)

    t.end_fill()
    t.fillcolor(BACKPACK_COLOR)
    t.begin_fill()

    t.end_fill()

body()
glass()
backpack()

t.screen.exitonclick()
