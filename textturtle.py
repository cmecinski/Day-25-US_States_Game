from turtle import Turtle


class Text(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("black")
        self.hideturtle()

    def write_text(self, name, x_position, y_position):
        self.goto(x_position, y_position)
        self.write(name)
