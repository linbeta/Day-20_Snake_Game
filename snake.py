from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:
    # The starting 3 squares of snake body.
    def __init__(self, snake_length):
        self.segments = []
        self.create_snake(snake_length)
        self.head = self.segments[0]

    def create_snake(self, snake_length):
        for i in range(snake_length):
            snake_body = Turtle("square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.goto(i * (-20) + 10, 0)
            self.segments.append(snake_body)

    def snake_grow(self):
        new_body = Turtle("square")
        new_body.color("white")
        new_body.penup()
        tail_position = self.segments[-1].position()
        new_body.goto(tail_position)
        self.segments.append(new_body)

    def move(self):
        for seg_n in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_n - 1].xcor()
            new_y = self.segments[seg_n - 1].ycor()
            self.segments[seg_n].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # set a condition from the snake head to turn backward.
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)