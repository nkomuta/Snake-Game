from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.turtle_list[0].distance(food) < 15:
        food.random_location()
        scoreboard.score_count()
        snake.add_new_turtle()

    if not (not (snake.turtle_list[0].xcor() > 285) and not (snake.turtle_list[0].xcor() < -285) and not (
            snake.turtle_list[0].ycor() > 285) and not (snake.turtle_list[0].ycor() < -285)):
        scoreboard.reset()
        snake.reset()

    for x in snake.turtle_list[1:]:
        if snake.turtle_list[0].distance(x) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
