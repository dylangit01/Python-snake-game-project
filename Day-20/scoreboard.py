from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f'Score = {self.score}', False, align=ALIGNMENT, font=FONT)
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()