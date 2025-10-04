from turtle import Turtle, Screen

s = Screen()
s.setup(600, 600)
s.bgcolor('black')
s.title('The Snake Game')

all_turtles = []
t_width = -20
for _ in range(3):
    t = Turtle('square')
    t.color('white')
    t.goto(t_width, 0)
    t_width += 20
    all_turtles.append(t)

game_on = True
while game_on:
    for t in all_turtles:
        t.penup()
        t.forward(10)











s.exitonclick()