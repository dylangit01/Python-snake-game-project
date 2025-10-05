from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(1200, 600)
screen.bgcolor('black')
screen.title('The Snake Game')
# not showing up the snake at first
screen.tracer(0)

mySnake = Snake()

game_on = True
while game_on:
    # only update the snake when all snakes moved forward by 20
    screen.update()
    time.sleep(0.3)
    mySnake.movement()




screen.exitonclick()