from turtle import Screen
import time
from snake import Snake
from Food import Food
from Scoreboard import Score

'''def move_down():
    if Turtle.heading()==180:
        Turtle.left(90)
    elif Turtle.heading()==0:
        Turtle.right(90)'''

screen = Screen()
screen.tracer(0)
snake = Snake()
screen.bgcolor("black")
screen.listen()
screen.setup(width=600, height=600)
food = Food()
score = Score()
is_game = True
level=screen.textinput("Select level", " easy/ medium/ Hard :")
if level.lower() == "easy":
    a=0.1
elif level.lower() == "medium":
    a=0.05
elif level.lower() == "hard":
    a=0.01

while is_game:
    screen.update()
    time.sleep(a)

    snake.move()
    screen.onkeypress(key="Right", fun=snake.move_right)
    screen.onkeypress(key="Left", fun=snake.move_left)
    screen.onkeypress(key="Down", fun=snake.move_down)
    screen.onkeypress(key="Up", fun=snake.move_up)

    if snake.head.distance(food) < 15:
        food.position()
        score.increase_score()

        snake.extend_body()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset()
        score.reset_score()
    for s_body in snake.turtles[1:]:
        if snake.head.distance(s_body) < 5:
            snake.reset()
            score.reset_score()


screen.exitonclick()
