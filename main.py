from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# starting_positions = [(0,0), (-20,0), (-40,0)]
# snake_colors = ["yellow","red","red"]

# segments = []

# for position,body in zip(starting_positions,snake_colors):
#     new_segment = Turtle("square")
#     new_segment.color(body)
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor () < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)< 10:
            game_is_on = False
            scoreboard.game_over()
        
    
    # for seg_num in range(len(segments) -1,0,-1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    # segments[0].forward(20)


    


# segment_1 = Turtle("square")
# segment_1.color("yellow")
# segment_1.goto(0,0)

# segment_2 = Turtle("square")
# segment_2.color("red")
# segment_2.goto(-20,0)

# segment_3 = Turtle("square")
# segment_3.color("red")
# segment_3.goto(-40,0)




















screen.exitonclick()