from turtle import Screen
from raquete import Raquete
from bola import Bola
from screboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("#BC8F8F")
screen.setup(width=800, height=600)
screen.title("PingPong dos Crias")
screen.tracer(0)

d_raquete = Raquete((350, 0))
e_raquete = Raquete((-350, 0))
bola = Bola()
score = Scoreboard()

screen.listen()
screen.onkey(d_raquete.go_up, "Up")
screen.onkey(d_raquete.go_down, "Down")
screen.onkey(e_raquete.go_up, "w")
screen.onkey(e_raquete.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    bola.move()

    if bola.ycor() > 280 or bola.ycor() < -280:
        bola.bounce_y()

    if bola.distance(d_raquete) < 50 and bola.xcor() > 320 or bola.distance(e_raquete) < 50 and bola.xcor() < -320:
        bola.bounce_x()

    if bola.xcor() > 380:
        bola.reset_position()
        score.e_point()

    if bola.xcor() < -380:
        bola.reset_position()
        score.d_point()
screen.exitonclick()
