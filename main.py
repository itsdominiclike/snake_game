from turtle import Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

# **Create game objects**
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen = Screen()

# **Set up the game window**
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off automatic updates to manually control screen refresh

# **Detect player input (arrow key presses)**
screen.listen()  # Enable the screen to listen for key presses
screen.onkeypress(snake.up, "Up")  # Move snake up when "Up" arrow key is pressed
screen.onkeypress(snake.right, "Right")  # Move snake right when "Right" arrow key is pressed
screen.onkeypress(snake.left, "Left")  # Move snake left when "Left" arrow key is pressed
screen.onkeypress(snake.down, "Down")  # Move snake down when "Down" arrow key is pressed

# **Game loop control**
playing = True

while playing:
    screen.update()  # Refresh the screen manually (since tracer is off)
    time.sleep(0.1)  # Pause for 0.1 seconds to control the game speed
    snake.move()  # Move the snake forward in its current direction

    # **Detect collision with food**
    if snake.head_snake.distance(food) < 15:  # Check if the snake's head is close to the food
        food.refresh()  # Generate new food at a random position
        snake.extend()  # Add a new segment to the snake
        scoreboard.update_score()  # Increase the player's score

    # **Detect collision with the wall**
    if snake.head_snake.xcor() > 280 or snake.head_snake.xcor() < -300 or \
       snake.head_snake.ycor() > 300 or snake.head_snake.ycor() < -280:  # Check if the snake hits the wall
        playing = False  # End the game
        scoreboard.game_over()  # Display "Game Over" on the screen

    # **Detect collision with the snake's own body **
    for i in snake.segments[1:]:  # Loop through all segments except the head
        if snake.head_snake.distance(i) < 10:  # Check if the head is too close to a body segment
            playing = False  # End the game
            scoreboard.game_over()  # Display "Game Over" on the screen

screen.exitonclick()  # Close the game window when clicked