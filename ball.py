import table, random

class Ball:

    def __init__(self, table, width=14, height=14, color="red", x_speed=6, y_speed=4, x_start=0, y_start=0):
        self.width = width
        self.height = height
        self.x_posn = x_start
        self.y_posn = y_start
        self.color = color

        self.x_start = x_start
        self.y_start = y_start
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.table = table
        self.circle = self.table.draw_oval(self)
    
    # methods for the ball