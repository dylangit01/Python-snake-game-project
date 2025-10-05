from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.random_food()

    def random_food(self):
        self.shape('circle')
        self.color('red')
        self.shapesize(0.5, 0.5)
        self.penup()
        self.food_refresh()


    def food_refresh(self):
        random_x = random.randint(-570, 550)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)