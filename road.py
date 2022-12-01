from turtle import Turtle

class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        for n in range(14):
            self.penup()
            self.draw_dash_line((-280, -260 + (n * 40) + 5))
            # self.penup()
        self.hideturtle()

    def draw_dash_line(self, start):
        self.goto(start)
        for n in range(20):
            if n % 2 == 0:
                self.pendown()
                self.goto(self.xcor() + 20, self.ycor())
                self.penup()
            else:
                self.penup()
                self.goto(self.xcor() + 40, self.ycor())
