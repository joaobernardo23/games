#Easy and fun pong!

import turtle
from pong_items import bar
from pong_items import ball


#Create screen
wn = turtle.Screen()
wn.title("JB's Pong :)")
wn.setup(width=1000, height=800)
wn.bgcolor("black")
wn.tracer(0)

#Score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 360)
score.write("Player A: 0 | Player B: 0", align="center", font=("areal", 24, "normal"))

score_A = 0
score_B = 0

#Bars
bl = turtle.Turtle() 
br = turtle.Turtle()

#Ball
ball1 = turtle.Turtle()

bar_left = bar(bl, score_A)
bar_right = bar(br, score_B)
ball0 = ball(ball1)

#Creating the initial objects
bar_left.create_bar(0, "square", 5.5, 1, "white", -450, 0)
bar_right.create_bar(0, "square", 5.5, 1, "white", 450, 0)
ball0.create_ball(0, "circle", 1, 1, "white", 0, 0, 0.25, 0.25)


#Bar movement commands
wn.listen()
wn.onkeypress(bar_left.bar_up, "w")
wn.onkeypress(bar_left.bar_down, "s")
wn.onkeypress(bar_right.bar_up, "Up")
wn.onkeypress(bar_right.bar_down, "Down")


# Main loop

set = 1

while set == 1:
    wn.update()

    ball0.check_pos(bar_left, bar_right, score)

    if bar_left.score == 5:

        wn.clear()
        set = 2
    

    if bar_right.score == 5:

        wn.clear()
        set = 3
        
        
    ball0.move_ball()

#Player A wins loop    

while set == 2:

    wn.title("JB's Pong :)")
    wn.setup(width=1000, height=800)
    wn.bgcolor("black")
    wn.tracer(0)
    end = turtle.Turtle()
    end.speed(0)
    end.color("white")
    end.penup()
    end.hideturtle()
    end.goto(0, 50)
    end.write("The game ended.\n\n", align="center", font=("areal", 34, "normal"))
    end.write("\n\nPlayer A wins!!!", align="center", font=("areal", 34, "normal"))



#Player B wins loop

while set == 3: 
    
    wn.title("JB's Pong :)")
    wn.setup(width=1000, height=800)
    wn.bgcolor("black")
    wn.tracer(0)
    end = turtle.Turtle()
    end.speed(0)
    end.color("white")
    end.penup()
    end.hideturtle()
    end.goto(0, 50)
    end.write("The game ended.\n\n", align="center", font=("areal", 34, "normal"))
    end.write("\n\nPlayer A wins!!!", align="center", font=("areal", 34, "normal"))

    
    