from turtle import Turtle

COR = [(0, 0), (-20, 0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        self.turtles = []
        self.create()
        self.head = self.turtles[0]
        #self.body()

    def create(self):
        timm = Turtle("circle")
        timm.color("white")
        timm.penup()
        timm.pensize(10)
        timm.goto(x=10, y=0)
        self.turtles.append(timm)
        for position in COR:
            self.body(position)

    def body(self,position):

        tim = Turtle(shape="square")
        tim.penup()
        tim.goto(position)
        tim.hideturtle()
        self.turtles.append(tim)
        tim.showturtle()
        tim.color("white")

    def extend_body(self):
        self.body(position=self.turtles[-1].position())

    def move(self):
        for move_turtle in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[move_turtle - 1].xcor()
            new_y = self.turtles[move_turtle - 1].ycor()
            self.turtles[move_turtle].goto(x=new_x, y=new_y)
        self.head.forward(10)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def move_down(self):

        if self.head.heading() != UP:
            self.head.setheading(270)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def reset(self):
        for s_body in self.turtles:
            s_body.goto(x=1000,y=1000)
        self.turtles=[]
        self.create()

        self.head=self.turtles[0]
