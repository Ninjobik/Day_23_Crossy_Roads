from turtle import Turtle, Screen
import random


class Car(Turtle):
    def __init__(self, number):
        super().__init__()
        self.penup()
        self.shape("square")
        self.screen = Screen()
        self.screen.colormode(255)
        self.shapesize(1.5, 3)
        self.color(self.set_random_color())
        self.direction = self.set_random_direction()
        self.original_pos = self.set_position(number)
        self.setposition(self.original_pos)
        self.car_speed = 0

    def set_random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color = (r, g, b)
        return random_color

    def set_position(self, number):
        self.x = self.direction
        self.y = -275 + 40 * (number + 1)
        return (self.x * 350, self.y)

    def set_random_direction(self):
        self.dir = random.randrange(-1, 1)
        if self.dir == 0:
            self.dir = 1
        return self.dir

    def update_position(self):
        self.setposition(self.xcor() - self.dir * self.car_speed, self.ycor())

    def set_random_speed(self, level):
        self.car_speed = random.randint(3, 10) + level

