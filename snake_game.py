from turtle import Turtle, Screen
from snake_food import Food
from scoreboard import Score
import time
from snake_2 import Snake
screen = Screen()
screen.setup(600,600)
screen.title('python_bite')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_begins = True
while game_begins:
    screen.update()
    time.sleep(0.1)
    snake.move()
# collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()


    # collision with wall
    if snake.head.xcor()> 280 or snake.head.xcor()< -280 or snake.head.ycor()> 280 or snake.head.ycor()< -280:
        # game_begins = False : game over ka liya tha
        # score.over()
        score.reboot()
        snake.reboot()

#         collision with tail
    for i in snake.snakes:
        if i == snake.head:
            pass
        elif snake.head.distance(i) < 10:
            # game_begins = False  game over ka liya tha
            # score.over()
            score.reboot()
            snake.reboot()
screen.exitonclick()

