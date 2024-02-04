from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DEFAULT_LEN = 3


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.collision = False

    def create_snake(self):
        for i in range(DEFAULT_LEN):
            new = Turtle("square")
            new.color("white")
            new.penup()
            new.goto(x=-20 * i, y=0)
            self.body.append(new)

    def add_segment(self, position):
        new = Turtle("square")
        new.color("white")
        new.penup()
        new.goto(position)
        self.body.append(new)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(x=new_x, y=new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != (UP+180) % 360:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != (DOWN+180) % 360:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != (LEFT+180) % 360:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != (RIGHT+180) % 360:
            self.head.setheading(RIGHT)

    def eat_tail(self):
        for i in self.body[1:]:
            if self.head.distance(i) < 5:
                self.collision = True
        return self.collision
