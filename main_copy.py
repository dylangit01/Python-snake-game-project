from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(1200, 600)
screen.bgcolor('black')
screen.title('The Snake Game')
# not showing up the snake at first
screen.tracer(0)
screen.listen()
# mySnake = Snake()

all_segments = []

start_position = 0
for _ in range(3):
    segment = Turtle('square')
    segment.color('white')
    # remove the line:
    segment.penup()
    segment.goto(start_position, 0)
    start_position -= 20
    all_segments.append(segment)

def turn_left():
    # control the 1st item only, so the other elements will follow the head
    all_segments[0].left(90)

def turn_right():
    all_segments[0].right(90)


game_on = True
while game_on:
    # only update the snake when all snakes moved forward by 20
    screen.update()
    time.sleep(1)
    # move the last snake to the previous snake position,
    # and the 2nd last snake moves to the previous position,
    # since range not including the last time, the first item will out of the loop,
    # can keep moving forward

    for each_s in range(len(all_segments) - 1, 0, -1):
        new_x = all_segments[each_s - 1].xcor()
        new_y = all_segments[each_s - 1].ycor()
        all_segments[each_s].goto(new_x, new_y)
    screen.onkey(turn_left, 'a')
    screen.onkey(turn_right, 'd')
    all_segments[0].forward(20)
















screen.exitonclick()