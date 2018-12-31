from tkinter import *

class Table:
    def __init__(self, window, color="black", net_color="green", width=600, height=400, vertical_net=False, horizontal_net=False):
        self.width = width
        self.height = height
        self.color = color
        
        self.canvas = Canvas(window, bg=self.color, height=self.height, width=self.width)
        self.canvas.pick()

        if(vertical_net):
            self.canvas.create_line(self.width/2, 0, self.width/2, self.height, width=2, fill=net_color, dash=(15, 23))
        
        if(horizontal_net):
            self.canvas.create_line(0,self.height/2, self.width, self.height/2, width=2, fill=net_color, dash=(15, 23))
