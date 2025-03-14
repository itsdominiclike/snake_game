from turtle import Screen
"""
Main module for Snake Game.

This module sets up the game window, initializes game objects,
and runs the main game loop.
"""
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

# Initialize game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen = Screen()

# Configure the game window
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Disable auto-refresh for smoother animation

# Set up key bindings for controlling the snake
screen.listen()
screen.onkeypress(snake.up, "Up")  # Move snake up when "Up" arrow key is pressed
screen.onkeypress(snake.right, "Right")  # Move snake right when "Right" arrow key is pressed
screen.onkeypress(snake.left, "Left")  # Move snake left when "Left" arrow key is pressed
screen.onkeypress(snake.down, "Down")  # Move snake down when "Down" arrow key is pressed

# Main game loop
playing = True

while playing:
    screen.update()  # Manually refresh the screen
    time.sleep(0.1)  # Delay to control game speed
    snake.move()  # Update snake position

    # Check for collision with food
    if snake.head_snake.distance(food) < 15:
        food.refresh()  # Place food at a new random location
        snake.extend()  # Grow the snake
        scoreboard.increase_score()  # Update the score

    # Check for collision with the wall
    if snake.head_snake.xcor() > 280 or snake.head_snake.xcor() < -300 or \
       snake.head_snake.ycor() > 300 or snake.head_snake.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Check for collision with the snake's body
    for segment in snake.segments[1:]:
        if snake.head_snake.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()  # Close the game window when clicked