from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 20, 'bold')

def fetch_data():
    with open('data.txt', 'r') as f:
        high_score = int(f.read())
        return high_score

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = fetch_data()
        self.color('white')
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score = {self.score}, The highest score is: {fetch_data()}', False, align=ALIGNMENT, font=FONT)


    def reset_score(self):
        if self.score > self.high_score:
            with open('data.txt', 'w') as nf:
                nf.write(str(self.score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()