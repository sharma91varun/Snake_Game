from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 10, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.write("Score: 0", align=ALIGNMENT, font=FONT)
        
    def food_collision(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=('Arial', 10, 'bold'))

    def collision(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Arial', 10, 'bold'))
