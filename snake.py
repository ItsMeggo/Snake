from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.total_snake = []
        self.add_snake()
        self.head = self.total_snake[0]

    def add_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.total_snake.append(snake)

    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.total_snake[-1].position())

    def move(self):
        for seg_number in range(len(self.total_snake) - 1, 0, -1):
            new_x = self.total_snake[seg_number - 1].xcor()
            new_y = self.total_snake[seg_number - 1].ycor()
            self.total_snake[seg_number].goto(new_x, new_y)

        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
