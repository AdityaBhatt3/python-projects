
from turtle import Turtle

class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file="data.txt") as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f'Score: {self.score} HIGH SCORE : { self.high_score}',align='center',font=('arial',20,'normal'))



    def reboot(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="data.txt",mode='w') as file:
                file.write(f'{self.high_score}')

            self.score = 0
            self.update_scoreboard()

    # def over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align='center', font=('arial', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_data = 0
        self.update_scoreboard()





