from turtle import Turtle
MOVE_DISTANTE = 20


class Snake():
    def __init__(self):
        self.turtle_list = []
        self.create_snake()

    def create_snake(self):
        a = 0
        for x in range(3):
            new_turtle = Turtle(shape="circle")
            new_turtle.color("white")
            new_turtle.shapesize(stretch_len=0.5, stretch_wid=0.5)
            new_turtle.pu()
            new_turtle.goto(x=a, y=0)
            a -= 20
            self.turtle_list.append(new_turtle)

    def add_new_turtle(self):
        new_turtle = Turtle(shape="circle")
        new_turtle.color("white")
        new_turtle.shapesize(stretch_len=0.5, stretch_wid=0.5)
        new_turtle.pu()
        self.turtle_list.append(new_turtle)
        self.turtle_list[-1].goto(self.turtle_list[-2].position())

    def reset(self):
        for i in self.turtle_list:
            i.goto(1000,1000)
        self.turtle_list.clear()
        self.create_snake()


    def move(self):
        for seg in range(len(self.turtle_list) - 1, 0, -1):
            new_x_cordinate = self.turtle_list[seg - 1].xcor()
            new_y_cordinate = self.turtle_list[seg - 1].ycor()
            self.turtle_list[seg].goto(new_x_cordinate, new_y_cordinate)
        self.turtle_list[0].forward(MOVE_DISTANTE)

    def up(self):
        if self.turtle_list[0].heading() != 270:
            self.turtle_list[0].setheading(90)

    def down(self):
        if self.turtle_list[0].heading() != 90:
            self.turtle_list[0].setheading(270)

    def left(self):
        if self.turtle_list[0].heading() != 0:
            self.turtle_list[0].setheading(180)

    def right(self):
        if self.turtle_list[0].heading() != 180:
            self.turtle_list[0].setheading(0)
