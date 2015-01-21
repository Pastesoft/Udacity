import turtle

def draw_triangle(brush):
    for i in range (1,4):
        brush.forward(100)
        brush.right(120)

def draw_pict():
    window = turtle.Screen()
    window.bgcolor("red")

    brush = turtle.Turtle()
    brush.color("yellow")
    brush.speed(10)

    for i in range(1,100):
        draw_triangle(brush)
        brush.right(10)

    window.exitonclick()

draw_pict()
