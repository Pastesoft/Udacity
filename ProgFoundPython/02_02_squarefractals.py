import turtle

def draw_square(brush) :
    for i in range(1,5):
        brush.forward(60)
        brush.right(90)

def draw_circle() :
    window = turtle.Screen()
    window.bgcolor("red")

    brush = turtle.Turtle()
    brush.color("yellow")
    brush.speed(30)

    for i in range(0,36) :
        draw_square(brush)
        brush.right(10)

    window.exitonclick()

draw_circle()

