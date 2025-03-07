from turtle import Turtle

class Ball(Turtle):
    """it creates the ball and make it move"""
    def __init__(self):
      super().__init__()
      self.width(20)
      self.color("orange")
      self.shape("circle")
      self.penup()
      self.x_move = 10
      self.y_move = 10
      self.move_speed = 0.1
    def moves(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    def restart(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()