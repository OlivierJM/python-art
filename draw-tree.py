import turtle

t = turtle

# initial variables
length = 80
detail = 12
thickness = 20
angle = 40

t.speed(0)

def draw_tree(branch_thickness, branch_length):
    if branch_length > 5:
        if branch_length < 20:
            t.color("green")
        else:
            t.color("brown")
        t.pensize(branch_thickness)
        t.forward(branch_length)
        t.right(angle)
        draw_tree(branch_thickness / 1.5, branch_length-detail)
        t.left(2 * angle)
        draw_tree(branch_thickness / 1.5, branch_length-detail)
        t.right(angle)
        t.back(branch_length)
        t.color("brown")


t.left(90)
t.penup()
t.back(100)
t.pendown()

t.color("brown")
draw_tree(thickness, length)
t.done()
        
        
        