from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
segments=[]
starting_positions = [(0,0),(-20,0),(-40,0)]
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game = True
while game:
    screen.update()
    segments[].forward(1)








screen.exitonclick()