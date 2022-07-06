import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
user_choice = int(screen.textinput(title="Choose difficulty", prompt=" 1 Beginner, 2 Intermediate, 3 Advanced:\n"
                                                                     "                  Move with a\w\d\s"))
screen.setup(width=600, height=600)
screen.title("Nicole Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(key="a", fun=snake.move_left)
screen.onkey(key="d", fun=snake.move_right)
screen.onkey(key="w", fun=snake.move_up)
screen.onkey(key="s", fun=snake.move_down)


def level(choice):
    if choice == 1:
        return 0.15
    elif choice == 2:
        return 0.075
    elif choice == 3:
        return 0.04
    

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(level(user_choice))
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extend()

    y_cor = int(snake.head.ycor())
    x_cor = int(snake.head.xcor())

    if x_cor < -280 or x_cor > 280 or y_cor < -280 or y_cor > 280:
        game_is_on = False
        score.game_over()

    for body_part in snake.body[1:]:
        if body_part.position() == snake.head.position():
            score.game_over()
            game_is_on = False

screen.exitonclick()
