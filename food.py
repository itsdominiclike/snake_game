from turtle import Turtle
import random

class Food(Turtle):  # Food class inherits from Turtle
    def __init__(self):
        """Initialize the food object with default settings."""
        super().__init__()  # Call the Turtle class constructor
        self.penup()
        self.shape("circle")
        self.shapesize(0.5, 0.5)  # Make the food smaller (default turtle size is 20x20, so this makes it 10x10)
        self.color("blue")
        self.speed(0)  # Set animation speed to the fastest (instant movement)
        self.refresh()  # Place the food at a random position initially

    def refresh(self):
        """Move the food to a random location within the game boundaries."""
        rand_x = random.randint(-280, 280)  # Random x-coordinate within the play area
        rand_y = random.randint(-280, 280)  # Random y-coordinate within the play area
        self.goto(rand_x, rand_y)  # Move food to the new random position