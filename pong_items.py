import os  #Little bouncy sound for ball collisions

class bar: 
    def __init__(self, tob, score):
        self.tob = tob
        self.score = score

    def create_bar(self, anispeed, shape, stretch_wid, stretch_len, color, x0, y0):
        self.tob.speed(anispeed)
        self.tob.shape(shape)
        self.tob.shapesize(stretch_wid=stretch_wid, stretch_len=stretch_len)
        self.tob.color(color)
        self.tob.penup()
        self.tob.goto(x0, y0)
    
    
    def bar_up(self):
        y = self.tob.ycor()

        #Check if it is at the top of the screen (so it doesn't fly off :) )
        if y>=340:
            self.tob.sety(340)
        else:
            y +=20

        self.tob.sety(y)

    def bar_down(self):
        y = self.tob.ycor()

        #Same for the bottom of the screen
        if y<=-340:
            self.tob.sety(-340)
        else:
            y -=20

        self.tob.sety(y)

    def xcor(self): #Bar's x coordenate
        return self.tob.xcor()
    
    def ycor(self): #Bar's y coordenate
        return self.tob.ycor()
    
    def score1(self):
        return self.score
    
    def score_plus(self):
        self.score += 1


class ball:
    def __init__(self, tob):
        self.tob = tob

    def create_ball(self, anispeed, shape, stretch_wid, stretch_len, color, x0, y0, dx, dy):
        self.tob.speed(anispeed)
        self.tob.shape(shape)
        self.tob.shapesize(stretch_wid=stretch_wid, stretch_len=stretch_len)
        self.tob.color(color)
        self.tob.penup()
        self.tob.goto(x0, y0)    
        self.tob.dx = dx
        self.tob.dy = dy

    def check_pos(self, bl, br, text): #Checks collisions with the limits of the screen and with the bars and acts accordingly.
        y = self.tob.ycor()
        x = self.tob.xcor()

        if y>=385:
            self.tob.sety(385)
            self.tob.dy *= -1 
            os.system("aplay bounce.wav&")
            
        
        if y<=-385:
            self.tob.sety(-385)
            self.tob.dy *= -1
            os.system("aplay bounce.wav&")
            

        if x>=480:
            self.tob.sety(0)
            self.tob.setx(0)
            self.tob.dx *= -1
            self.tob.dy *= -1
            bl.score_plus()
            text.clear()
            text.write("Player A: {} | Player B: {}".format(bl.score1(), br.score1()), align="center", font=("areal", 24, "normal"))
            
    
        if x<=-480:
            self.tob.sety(0)
            self.tob.setx(0)
            self.tob.dx *= -1
            self.tob.dy *= -1
            br.score_plus()
            text.clear()
            text.write("Player A: {} | Player B: {}".format(bl.score1(), br.score1()), align="center", font=("areal", 24, "normal"))
            

        if (x<=-430 and x>= -440) and (y < bl.ycor() + 55 and y > bl.ycor() - 55):
            self.tob.setx(-430)
            self.tob.dx *= -1
            os.system("aplay bounce.wav&")
            
            

        if (x>=430 and x<= 440) and (y < br.ycor() + 55 and y > br.ycor() - 55):
            self.tob.setx(430)
            self.tob.dx *= -1
            os.system("aplay bounce.wav&")


    def move_ball(self):

        self.tob.setx(self.tob.xcor() + self.tob.dx)
        self.tob.sety(self.tob.ycor() + self.tob.dy)

    def xcor(self):
        return self.tob.xcor()
    
    def ycor(self):
        return self.tob.ycor()
