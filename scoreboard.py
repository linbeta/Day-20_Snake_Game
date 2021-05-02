from turtle import Turtle

TEXT_ALIGNMENT = "center"
FONT = ("Courier New", 12, "normal")
GAME_OVER_FONT = ("Courier New", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as high_score_record:
            self.high_score = int(high_score_record.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        # Use self.eat_food() to print the very first score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", False, align=TEXT_ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("data.txt", mode="w") as high_score_record:
            high_score_record.write(str(self.high_score))
        self.update_scoreboard()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.color("Orange")
    #     self.write(f"GAME OVER", False, align=TEXT_ALIGNMENT, font=GAME_OVER_FONT)
    #     self.goto(0, -30)
    #     if self.score > self.high_score:
    #         self.high_score = self.score
    #     self.write(f"Your score: {self.score - 1}  High score: {self.high_score - 1}", align=TEXT_ALIGNMENT, font=FONT)

    def eat_food(self):
        self.score += 1
        self.update_scoreboard()
