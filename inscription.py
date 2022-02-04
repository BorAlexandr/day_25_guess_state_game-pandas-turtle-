from turtle import Turtle


class Inscriptions(Turtle):

    def __init__(self, state, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(int(x), int(y))
        self.write(state, align="center", font=("Arial", 10, "normal"))
