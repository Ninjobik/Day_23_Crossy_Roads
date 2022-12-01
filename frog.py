from turtle import Turtle


class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.speed(2)
        self.start_pos = (0, -280)
        self.setposition(self.start_pos)

    def move(self):
        self.setheading(90)
        self.goto(self.xcor(), self.ycor() + 20)

    def turn_right(self):
        self.setheading(0)
        self.goto(self.xcor() + 20, self.ycor())

    def turn_left(self):
        self.setheading(180)
        self.goto(self.xcor() - 20, self.ycor())
