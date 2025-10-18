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
        print(snake_food)
        snake_food.food_refresh()
        mySnake.extend()
        scoreBoard.add_score()

    # Detect collision with wall:
    snake_head_x = mySnake.head.xcor()
    snake_head_y = mySnake.head.ycor()
    if snake_head_x > 580 or snake_head_x < -580 or snake_head_y > 280 or snake_head_y < -280:
        # game_on = False
        scoreBoard.reset_score()
        mySnake.reset_snake()

    #Detect collision with tail
    for segment in mySnake.segments[1:]:
        if mySnake.head.distance(segment) <= 15:
            # game_on = False
            scoreBoard.reset_score()
            mySnake.reset_snake()


screen.exitonclick()