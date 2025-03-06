import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorebaord import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((375,0),"orange")
l_paddle = Paddle((-375,0),"orange")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s")
screen.bgpic("snake.gif")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.moves()

    #detecting the ball collission with wall and bounce back after colliding
    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.bounce_y()
    #detect if the ball hit the paddle and it bounces back
    if ball.distance(l_paddle) < 50 and ball.xcor() < -345 or ball.distance(r_paddle) < 50 and ball.xcor() > 345:
        ball.bounce_x()

    #detect R paddle misses
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()

    # detect L paddle misses
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()

screen.exitonclick()