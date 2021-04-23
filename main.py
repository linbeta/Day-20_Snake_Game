from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
# screen.screensize(canvwidth=600, canvheight=600, bg="black")
# TODO: check out what's different between the above 2 ways of setting.
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake(3)
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.regenerate_food()
        snake.snake_grow()
        scoreboard.eat_food()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False

    # Detect collision with the tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

scoreboard.game_over()
# TODO: ask user play again? and track the highest score.

screen.exitonclick()
