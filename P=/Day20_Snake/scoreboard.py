from turtle import Turtle

FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=FONT)
        self.hideturtle()
        
    def increase_score(self):
        self.score +=1 
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)
        
    def game_over(self):

        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
        