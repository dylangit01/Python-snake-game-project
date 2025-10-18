from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score = {self.score}, The highest score is: {self.high_score}', False, align=ALIGNMENT, font=FONT)


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()