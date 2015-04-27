import turtle
def draw_square(brad):

    for i in range(4):
        brad.forward(100)
        brad.right(90)
    angie=turtle.Turtle()
    angie.circle(100)
        
#draw_square()
def art():
    window=turtle.Screen()
    window.bgcolor("blue")
    brad=turtle.Turtle()
    sun_square(brad)
    window.exitonclick()
def sun_square(brad):
    for i in range(36):
        draw_square(brad)
        brad.right(10)
art()
