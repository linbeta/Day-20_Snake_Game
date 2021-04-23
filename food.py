from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.regenerate_food()

    def regenerate_food(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 270)
        self.goto(x, y)
