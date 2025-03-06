from turtle import Turtle

# Constants for text alignment and font styles
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')  # Font settings for the score display
GAME_OVER_FONT = ('Courier', 30, 'normal')  # Font settings for the "Game Over" message

class Scoreboard(Turtle):
    def __init__(self):
        """Initialize the scoreboard object."""
        super().__init__()  # Call the Turtle class constructor
        self.hideturtle()  # Hide the turtle cursor (only text should be visible)
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)  # Position the scoreboard at the top of the screen
        self.score = 0  # Initialize the score to 0
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # Display the initial score

    def update_score(self):
        """Increase and update the displayed score."""
        self.clear()  # Clear the previous score display
        self.score += 1  # Increment the score by 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # Write the updated score

    def game_over(self):
        """Display the 'Game Over' message at the center of the screen."""
        self.goto(0, 0)  # Move the turtle to the center
        self.write("Game Over", align=ALIGNMENT, font=GAME_OVER_FONT)  # Display "Game Over" message