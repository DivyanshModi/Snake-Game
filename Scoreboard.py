from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("Highscore.txt") as file:
            self.highscore=int(file.read())

        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()

        self.write(f"score= {self.score}  High_score: {self.highscore}", move=False, align="center", font=("Arial",12, "bold"))

    def reset_score(self):
        if self.score > self.highscore :
            self.highscore = self.score
            with open("Highscore.txt","w") as high:
                high.write(f"{self.highscore}")

        self.score=0
        self.update_score()

    #def game_over(self):
     #   self.goto(0,0)
      #  self.write("Game Over", move=False, align="center", font=("Arial", 12, "bold"))

    def increase_score(self):
        self.score+=1

        self.update_score()