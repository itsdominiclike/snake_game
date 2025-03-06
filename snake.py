from turtle import Turtle

# Constants for movement and direction
MOVE_DISTANCE = 20  # Distance the snake moves per step
UP = 90  # Upward direction in degrees
DOWN = 270  # Downward direction in degrees
LEFT = 180  # Left direction in degrees
RIGHT = 0  # Right direction in degrees
STARTING_SEGMENTS = 3  # Initial number of snake segments


class Snake:
    def __init__(self):
        self.segments = []  # List to store all the snake's segments
        self.new_x = 0  # Temporary variable to store x position for movement
        self.new_y = 0  # Temporary variable to store y position for movement
        self.create_snake()  # Create the initial snake segments
        self.head_snake = self.segments[0]  # The first segment is the snake's head
        self.move()  # Move the snake initially

    def create_snake(self):
        """Creates the initial snake with the defined number of segments."""
        for _ in range(STARTING_SEGMENTS):
            self.add_segment()

    def add_segment(self):
        """Adds a new segment to the snake at a default position."""
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.setpos(0, 0)  # Initial position (will be adjusted later)
        self.segments.append(new_segment)  # Add segment to the list

    def extend(self):
        """Adds a new segment at the last segment's position when the snake eats food."""
        additions = Turtle("square")  # Create a new segment
        additions.penup()
        additions.color("white")
        additions.setpos(self.new_x, self.new_y)  # Position it at the last known tail position
        self.segments.append(additions)  # Add the new segment to the snake

    def move(self):
        """Moves the snake forward by shifting each segment to the position of the one in front."""
        for i in range(len(self.segments) - 1, 0, -1):  # Iterate from the tail to the head (excluding the head)
            self.new_x = self.segments[i - 1].xcor()  # Get x position of the segment in front
            self.new_y = self.segments[i - 1].ycor()  # Get y position of the segment in front
            self.segments[i].goto(self.new_x, self.new_y)  # Move current segment to the previous one's position

        self.head_snake.forward(MOVE_DISTANCE)  # Move the head forward

    # Below methods handle direction changes (they could be combined into one method)
    def up(self):
        """Changes the snake's direction to up unless it's currently moving down."""
        if self.head_snake.heading() != DOWN:  # Prevents reversing direction
            self.head_snake.setheading(UP)

    def down(self):
        """Changes the snake's direction to down unless it's currently moving up."""
        if self.head_snake.heading() != UP:
            self.head_snake.setheading(DOWN)

    def left(self):
        """Changes the snake's direction to left unless it's currently moving right."""
        if self.head_snake.heading() != RIGHT:
            self.head_snake.setheading(LEFT)

    def right(self):
        """Changes the snake's direction to right unless it's currently moving left."""
        if self.head_snake.heading() != LEFT:
            self.head_snake.setheading(RIGHT)