from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

FOOD_COLLISION = 18
WALL = 280

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision
    if snake.head.distance(food) < FOOD_COLLISION:
        food.refresh()
        snake.extend()
        scoreboard.food_collision()

    # Collision with wall and tail
    if (snake.head.xcor() > WALL
            or snake.head.ycor() > WALL
            or snake.head.xcor() < -WALL
            or snake.head.ycor() < -WALL
            or snake.eat_tail()):
        game_is_on = False
        scoreboard.collision()

screen.exitonclick()
