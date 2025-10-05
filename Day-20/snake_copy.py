from turtle import Turtle, Screen

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):

        start_position = 0
        for _ in range(3):
            segment = Turtle('square')
            segment.color('white')
            # remove the line:
            segment.penup()
            segment.goto(start_position, 0)
            # start_position should always -= a number, so all three segments can be generated in order like: 3, 2, 1
            start_position -= 20
            self.segments.append(segment)

    def turn_left(self):
        # control the 1st item only, so the other elements will follow the head
        self.segments[0].left(90)

    def turn_right(self):
        self.segments[0].right(90)

    def movement(self):
        # move the last snake to the previous snake position,
        # and the 2nd last snake moves to the previous position,
        # since range not including the last time, the first item will out of the loop,
        # can keep moving forward
        screen = Screen()
        screen.listen()
        for each_s in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[each_s - 1].xcor()
            new_y = self.segments[each_s - 1].ycor()
            self.segments[each_s].goto(new_x, new_y)
        screen.onkey(self.turn_left, 'a')
        screen.onkey(self.turn_right, 'd')
        self.segments[0].forward(20)

