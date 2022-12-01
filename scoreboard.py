from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(-250, 270)
        self.color("white")
        self.update_score(score)

    def update_score(self, score):
        self.clear()
        self.write(f"Level: {score}", False, "center", ("Ariel", 15, "normal"))

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", False, "center", ("Ariel", 15, "normal"))
