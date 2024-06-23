from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.highscore = int(data.read())
        self.color('white')
        self.pu()
        self.goto(0, 280)
        self.ht()
        self.update_score_screen()

    def update_score_screen(self):
        self.clear()
        self.write(f'Score = {self.score} High Score {self.highscore}', align='center',
                   font=('arial', 14, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.highscore}')
        self.score = 0
        self.update_score_screen()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!", align='center', font=('arial', 14, 'normal'))

    def score_count(self):
        self.score += 1
        self.update_score_screen()
