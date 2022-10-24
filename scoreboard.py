from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def reset(self)
        if self.score > self.high_score:
            self.high_score = self.score
        
        self.score = 0
        self.update_scoreboard()
        

    #def game_over(self):
        #self.goto(0,0)
        #self.write("Game Over.", False, align="center", font=FONT)
