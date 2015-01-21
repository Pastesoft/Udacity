import turtle

def draw_square(myt):
    myt.shape("turtle")
    myt.color("blue")

    i = 0
    while (i < 4):
        myt.forward(30)
        myt.right(90)
        i += 1

def draw_circle(myt):
    myt.shape("arrow")
    myt.color("yellow")
    myt.circle(60)


def draw_triangle(myt):
    myt.shape("square")
    myt.color("white")
    ind = 0
    while(ind < 3):
        myt.forward(100)
        myt.right(120)
        ind += 1

def mydraw():
    ind = 0
    window = turtle.Screen()
    window.bgcolor("red")

    myt = turtle.Turtle()
    myt.speed(30)

    while(ind < 30):
        draw_square(myt)
        draw_circle(myt)
        draw_triangle(myt)
        myt.right(10)
        ind += 1

    window.exitonclick()

mydraw()

