from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in POSITION:
            self.add_part(position)

    def add_part(self, position):
        body_part = Turtle(shape="square")
        body_part.color("white")
        body_part.penup()
        self.body.append(body_part)
        body_part.goto(position)

    def extend(self):
        self.add_part(self.body[-1].position())

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            position = self.body[i - 1].position()
            self.body[i].speed(0.5)
            self.body[i].goto(position)
        self.head.forward(MOVE_DISTANCE)


    def move_right(self):
        if int(self.head.heading()) == 90:
            self.head.right(90)
        elif int(self.head.heading()) == 270:
            self.head.left(90)

    def move_up(self):
        if int(self.head.heading()) == 0:
            self.head.left(90)
        elif int(self.head.heading()) == 180:
            self.head.right(90)

    def move_left(self):
        if int(self.head.heading()) == 90:
            self.head.left(90)
        elif int(self.head.heading()) == 270:
            self.head.right(90)

    def move_down(self):
        if int(self.head.heading()) == 0:
            self.head.right(90)
        elif int(self.head.heading()) == 180:
            self.head.left(90)
