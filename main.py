# allows use of turtles
import turtle

# set window size
turtle.setup(400,600)

# Create window
window = turtle.Screen()
window.bgcolor('green')

# name your tmn turtles
donatello = turtle.Turtle()
rafael = turtle.Turtle()
michaelangelo = turtle.Turtle()

# draw frame for traffic light
def drawLightFrame():
    donatello.pensize(3)
    donatello.color('black', 'black')
    donatello.begin_fill()
    donatello.forward(50)
    donatello.left(90)
    donatello.forward(120)
    donatello.left(90)
    donatello.forward(50)
    donatello.left(90)
    donatello.forward(120)
    donatello.left(90)
    donatello.end_fill()

drawLightFrame()

# t - turtle handle
# ht - number of pixels to move forward circle location
# color - circle fill color
def circle(t, ht, color):
    t.penup()
    t.forward(25)
    t.left(90)
    t.forward(ht)
    t.shape('circle')
    t.fillcolor(color)

circle(donatello, 30, 'green')
circle(rafael, 60, 'orange')
circle(michaelangelo, 90, 'red')

# current state of machine
state = 0

# Controls infinite state machine
def trafficState_machine():
    global state 

    if state == 0: 
        michaelangelo.color('darkgrey')
        rafael.color('darkgrey')
        donatello.color('green')
        window.ontimer(trafficState_machine, 5000)  
        state = 1
    elif state == 1:  
        michaelangelo.color('darkgrey')
        rafael.color('orange')
        donatello.color('darkgrey')
        window.ontimer(trafficState_machine, 5000)
        state = 2
    elif state == 2:               
        michaelangelo.color('red')
        rafael.color('darkgrey')
        window.ontimer(trafficState_machine, 5000)
        state = 0

trafficState_machine()

# listen for events
window.listen()
# Wait for user to close window
window.mainloop()  