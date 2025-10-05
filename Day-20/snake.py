from turtle import Turtle, Screen
import keyword
# Starting position should be positioned from bigger x position to a smaller one, otherwise, the first segment will have some issues
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen = Screen()
screen.listen()

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            segment = Turtle('square')
            segment.color('white')
            # remove the line:
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)


    def turn_left(self):
        # control the 1st item only, so the other elements will follow the head
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def turn_up(self):
        # control the 1st item only, so the other elements will follow the head
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def movement(self):
        # move the last snake to the previous snake position,
        # and the 2nd last snake moves to the previous position,
        # since range not including the last time, the first item will out of the loop,
        # can keep moving forward

        for each_s in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[each_s - 1].xcor()
            new_y = self.segments[each_s - 1].ycor()
            self.segments[each_s].goto(new_x, new_y)

        screen.onkey(self.turn_left, 'Left')
        screen.onkey(self.turn_right, 'Right')
        screen.onkey(self.turn_up, 'Up')
        screen.onkey(self.turn_down, 'Down')

        self.segments[0].forward(MOVE_DISTANCE)

