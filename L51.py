#the author's names are Allison Macrowski and Therese Burns
import turtle
riley=turtle.Turtle()
riley.width(5)
riley.speed(0)

def draw_star(color):
    for side in range(5):
        riley.color(color)
        riley.forward(100)
        riley.right(144)
    
def mood(mood):
    if mood=="happy":
        draw_star('pink')
    elif mood=="sad":
        draw_star('blue')
    elif mood=="sleepy":
        draw_star('green')
    else:
        draw_star('red')

mood("happy")
mood("sad")

