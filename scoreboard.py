from turtle import Turtle
TEXT_ALIGNMENT = "center"
FONT = ("Courier New", 12, "normal")
GAME_OVER_FONT = ("Courier New", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        # Use self.eat_food() to print the very first score = 0
        self.eat_food()

    def game_over(self):
        self.goto(0,0)
        self.color("Orange")
        self.write(f"GAME OVER", False, align=TEXT_ALIGNMENT, font=GAME_OVER_FONT)

    def eat_food(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align=TEXT_ALIGNMENT, font=FONT)
        self.score += 1
