from tkinter import *
import table


window = Tk()
window.title("My Pong")


my_table = table.Table(window, net_color="green", vertical_net=True)


#start the program
window.mainloop()