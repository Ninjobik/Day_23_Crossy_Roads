from turtle import Turtle, Screen
import frog
import time
import road
import car
import scoreboard

screen = Screen()
turtle = Turtle()

screen.setup(600, 600)
screen.bgcolor("Black")
screen.tracer(0)

road = road.Road()
frog = frog.Frog()
level = 1
score = scoreboard.Scoreboard(level)

cars = []
for n in range(13):
    new_car = car.Car(n)
    new_car.set_random_speed(level)
    cars.append(new_car)

screen.listen()
screen.onkey(frog.move, "w")
screen.onkey(frog.turn_left, "a")
screen.onkey(frog.turn_right, "d")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    for c in cars:
        if c.distance(frog) < 35 and abs(c.ycor()) - abs(frog.ycor()) < 25:
            score.game_over()
            game_on = False
        elif c.xcor() > 350 or c.xcor() < -350:
            c.setposition(c.original_pos)
            c.set_random_speed(level * 1.5)
        else:
            c.update_position()

        if frog.ycor() > 279:
            level += 1
            frog.setposition(frog.start_pos)
            score.update_score(level)


screen.exitonclick()
