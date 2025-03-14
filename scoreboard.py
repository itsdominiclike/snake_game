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

        # Load the high score from file
        with open('data.txt') as data:
            self.high_score = int(data.read())

        # Display the initial score
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        """Update the displayed score without incrementing it."""
        self.clear()  # Clear the previous score display
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score by 1 and update the scoreboard."""
        self.score += 1
        self.update_score()

    def reset(self):
        """Reset the current score and update the high score if needed."""
        if self.score > self.high_score:
            self.high_score = self.score
            # Save the new high score to file
            with open('data.txt', mode='w') as data:
                data.write(f"{self.high_score}")

        # Reset the score and update the display
        self.score = 0
        self.update_score()
