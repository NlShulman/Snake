from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.up()
        self.goto(0, 270)
        self.scoreboard()

    def scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.scoreboard()

    def game_over(self):
        self.goto(0,  0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


