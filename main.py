# allows use of turtles
import turtle

# set window size
turtle.setup(400,600)

# Create a playground for turtles
wn = turtle.Screen()
wn.bgcolor('green')

# Create turtles
tess = turtle.Turtle()
alex = turtle.Turtle()
henry = turtle.Turtle()

# draw frame for traffic light
def drawLightFrame():
    tess.pensize(3)
    tess.color('black', 'white')
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.left(90)
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

drawLightFrame()

# t - turtle handle
# ht - number of pixels to move forward circle location
# color - circle fill color
def circle(t, ht, color):
    t.penup()
    t.forward(40)
    t.left(90)
    t.forward(ht)
    t.shape('circle')
    t.fillcolor(color)

circle(tess, 40, 'green')
circle(alex, 100, 'orange')
circle(henry, 160, 'red')

# This variable holds the current state of the machine
state = 0

# A state machine for traffic light. Controls the infinite state machine, the creation and execution of the program
def trafficState_machine():
    global state 

    if state == 0: 
        henry.color('darkgrey')
        alex.color('darkgrey')
        tess.color('green')
        wn.ontimer(trafficState_machine, 3000)  
        state = 1
    elif state == 1:  
        henry.color('darkgrey')
        alex.color('orange')
        tess.color('darkgrey')
        wn.ontimer(trafficState_machine, 2000)
        state = 2
    elif state == 2:               
        henry.color('red')
        alex.color('darkgrey')
        wn.ontimer(trafficState_machine, 2000)
        state = 0

trafficState_machine()

# listen for events
wn.listen()
# Wait for user to close window
wn.mainloop()  