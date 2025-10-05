from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(1200, 600)
screen.bgcolor('black')
screen.title('The Snake Game')
# not showing up the snake at first
screen.tracer(0)

snake_food = Food()
mySnake = Snake()
scoreBoard = ScoreBoard()

game_on = True
while game_on:
    # only update the snake when all snakes moved forward by 20
    screen.update()
    time.sleep(0.1)
    mySnake.movement()

    #Detect collision with food:
    if mySnake.head.distance(snake_food) < 15:
        print('I got food')
        snake_food.food_refresh()
        scoreBoard.add_score()



screen.exitonclick()