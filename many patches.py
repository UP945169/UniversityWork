from graphics import *
def HorizontalSquare(win,x,y,x1,y1):
    # x = 0
    # y = 110
    # x1 = 10
    # y1 = 100
    for i in range(10):
        x = x + 10
        y = y - 10
        x1 = x1 + 10
        y1 = y1 - 10
        #print(x,y,x1,y1)
        Rectangle1 = Rectangle(Point(x,y),Point(x1,y1))
        Rectangle1.draw(win)
        Rectangle1.setFill("Red")
def drawGrid(win):
    x = 0
    x1 = 0
    y = 0
    for i in range(4):
        x = x + 25
        line1 = Line(Point(x,0),Point(x,500))
        line1.draw(win)
    for i in range(20):
        y = y + 25
        line2 = Line(Point(0,y),Point(100,y))
        line2.draw(win)
def gridX(win,x,y,x2,y2):
    for i in range(4):
        x = x + 25
        x2 = x2 + 25
        line1 = Line(Point(x,y),Point(x2,y2))
        line1.draw(win)
def gridY(win,x,y,x2,y2,r):
    for i in range(r):
        y = y + 25
        y2 = y2 + 25
        line1 = Line(Point(x,y),Point(x2,y2))
        line1.draw(win)
def drawFirstHI(win,x,y,x2,y2,r):
    for i in range(r):
        y = y + 25
        y2 = y2 + 25
        rectangle1 = Rectangle(Point(x,y),Point(x2,y2))
        rectangle1.draw(win)
def drawSecondHI(win,x,y,x2,y2,r):
    y = y + 17
    y2 = y2 + 17
    for i in range(r):
        y = y + 25
        y2 = y2 + 25
        rectangle1 = Rectangle(Point(x,y),Point(x2,y2))
        rectangle1.draw(win)
def drawThirdHI(win,x,y,x2,y2,r):
    x = x + 50
    x2 = x2 + 50
    for i in range(r):
        y = y + 25
        y2 = y2 + 25
        rectangle1 = Rectangle(Point(x,y),Point(x2,y2))
        rectangle1.draw(win)
def drawForthHI(win,x,y,x2,y2,r):
    x = x + 50
    x2 = x2 + 50
    y = y + 17
    y2 = y2 + 17
    for i in range(r):
        y = y + 25
        y2 = y2 + 25
        rectangle1 = Rectangle(Point(x,y),Point(x2,y2))
        rectangle1.draw(win)
def codeForBasicPatch(win):
    drawGrid(win)
    rectangleH = Rectangle(Point(8.8,0),Point(15,8.0))
    rectangleH.draw(win)
    rectangleH = Rectangle(Point(8.8,17),Point(15,25))
    rectangleH.draw(win)
    gridX(win,100,100,100,500)
    gridY(win,100,100,200,100,16)
    gridX(win,200,200,200,500)
    gridY(win,200,200,300,200,12)
    gridX(win,300,300,300,500)
    gridY(win,300,300,400,300,8)
    gridX(win,400,400,400,500)
    gridY(win,400,400,500,400,4)
    drawFirstHI(win,8.8,0,15,8.0,19)
    drawSecondHI(win,8.8,0,15,8.0,19)
    drawThirdHI(win,8.8,0,15,8.0,19)
    drawForthHI(win,8.8,0,15,8.0,19)
    drawFirstHI(win,108.8,100,115,108,15)
    drawSecondHI(win,108.8,100,115,108,15)
    drawThirdHI(win,108.8,100,115,108,15)
    drawForthHI(win,108.8,100,115,108,15)
    drawFirstHI(win,208.8,200,215,208,11)
    drawSecondHI(win,208.8,200,215,208,11)
    drawThirdHI(win,208.8,200,215,208,11)
    drawForthHI(win,208.8,200,215,208,11)
    drawFirstHI(win,308.8,300,315,308,7)
    drawSecondHI(win,308.8,300,315,308,7)
    drawThirdHI(win,308.8,300,315,308,7)
    drawForthHI(win,308.8,300,315,308,7)
    drawFirstHI(win,408.8,400,415,408,3)
    drawSecondHI(win,408.8,400,415,408,3)
    drawThirdHI(win,408.8,400,415,408,3)
    drawForthHI(win,408.8,400,415,408,3)
    HorizontalSquare(win,100,110,110,100)
    HorizontalSquare(win,200,110,210,100)
    HorizontalSquare(win,300,110,310,100)
    HorizontalSquare(win,400,110,410,100)
    HorizontalSquare(win,200,210,210,200)
    HorizontalSquare(win,300,210,310,200)
    HorizontalSquare(win,400,210,410,200)
    HorizontalSquare(win,300,310,310,300)
    HorizontalSquare(win,400,310,410,300)
    HorizontalSquare(win,400,410,410,400)
def codeFor7thPatch(win):
    drawGrid(win)
    gridY(win,0,500,600,500,4)
    gridY(win,0,600,700,600,4)
    gridX(win,0,500,0,600)
    gridX(win,100,200,100,600)
    gridX(win,200,200,200,600)
    gridX(win,300,300,300,600)
    gridX(win,400,400,400,600)
    gridX(win,500,500,500,600)
    gridX(win,0,600,0,700)
    gridX(win,100,600,100,700)
    gridX(win,200,600,200,700)
    gridX(win,300,600,300,700)
    gridX(win,400,600,400,700)
    gridX(win,500,600,500,700)
    gridX(win,600,600,600,700)
    drawFirstHI(win,8.8,0,15,8.0,27)
    drawSecondHI(win,8.8,0,15,8.0,27)
    drawThirdHI(win,8.8,0,15,8.0,27)
    drawForthHI(win,8.8,0,15,8.0,27)
    drawFirstHI(win,108.8,100,115,108,23)
    drawSecondHI(win,108.8,100,115,108,23)
    drawThirdHI(win,108.8,100,115,108,23)
    drawForthHI(win,108.8,100,115,108,23)
    drawFirstHI(win,208.8,200,215,208,19)
    drawSecondHI(win,208.8,200,215,208,19)
    drawThirdHI(win,208.8,200,215,208,19)
    drawForthHI(win,208.8,200,215,208,19)
    drawFirstHI(win,308.8,300,315,308,15)
    drawSecondHI(win,308.8,300,315,308,15)
    drawThirdHI(win,308.8,300,315,308,15)
    drawForthHI(win,308.8,300,315,308,15)
    drawFirstHI(win,408.8,400,415,408,11)
    drawSecondHI(win,408.8,400,415,408,11)
    drawThirdHI(win,408.8,400,415,408,11)
    drawForthHI(win,408.8,400,415,408,11)
    drawFirstHI(win,508.8,500,515,508,7)
    drawSecondHI(win,508.8,500,515,508,7)
    drawThirdHI(win,508.8,500,515,508,7)
    drawForthHI(win,508.8,500,515,508,7)
    drawFirstHI(win,608.8,600,615,608,3)
    drawSecondHI(win,608.8,600,615,608,3)
    drawThirdHI(win,608.8,600,615,608,3)
    drawForthHI(win,608.8,600,615,608,3)
    HorizontalSquare(win,500,110,510,100)
    HorizontalSquare(win,500,210,510,200)
    HorizontalSquare(win,500,310,510,300)
    HorizontalSquare(win,500,410,510,400)
    HorizontalSquare(win,500,510,510,500)
    HorizontalSquare(win,600,110,610,100)
    HorizontalSquare(win,600,210,610,200)
    HorizontalSquare(win,600,310,610,300)
    HorizontalSquare(win,600,410,610,400)
    HorizontalSquare(win,600,510,610,500)
    HorizontalSquare(win,600,610,610,600)
def codeFor9thPatch(win):
    print("I think this has not been created yet")
def decision(win):
    sizeOfPatch = int(input("What size patch do you want: "))
    if sizeOfPatch == 5:
        codeForBasicPatch(win)
    elif sizeOfPatch == 7:
        codeForBasicPatch(win)
        codeFor7thPatch(win)
    elif sizeOfPatch == 9:
        codeFor9thPatch(win)
    else:
        print("You have entered the a number that is not recognised: ")
def main():
    win = GraphWin("test",1000,1000)
    decision(win)
