from graphics import *
def HorizontalSquare(win,x,y,x1,y1):
    for i in range(10):
        x = x + 10
        y = y - 10
        x1 = x1 + 10
        y1 = y1 - 10
        Rectangle1 = Rectangle(Point(x,y),Point(x1,y1))
        Rectangle1.draw(win)
        Rectangle1.setFill("Blue")
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
def lines(win):
    x = 100
    y = 0
    x2 = 100
    y2 = 500
    for i in range(5):
        y = y + 100
        for i in range(4):
            x = x + 25
            x2 = x2 + 25
            line1 = Line(Point(x,y),Point(x2,y2))
            line1.draw(win)
    line1 = Line(Point(25,0),Point(25,500))
    line1.draw(win)
    line1 = Line(Point(50,0),Point(50,500))
    line1.draw(win)
    line1 = Line(Point(75,0),Point(75,500))
    line1.draw(win)
    line1 = Line(Point(100,0),Point(100,500))
    line1.draw(win)
def linesY(win):
    lines1 = Line(Point(0,0),Point(100,0))
    lines1.draw(win)
    lines1 = Line(Point(0,25),Point(100,25))
    lines1.draw(win)
    lines1 = Line(Point(0,50),Point(100,50))
    lines1.draw(win)
    lines1 = Line(Point(0,75),Point(100,75))
    lines1.draw(win)
    lines1 = Line(Point(0,100),Point(200,100))
    lines1.draw(win)
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    for i in range(5):
        x = x + 100
        for i in range(4):
            y = y + 25
            y2 = y2 + 25
            lines = Line(Point(x,y),Point(x2,y2))
            lines.draw(win)
def drawH(win):
    x = 25
    y = 8.0
    x2 = 15
    y2 = 8.0
    for i in range(4):
        y = y + 25
        y2 = y2 + 25
        rectangleI = Rectangle(Point(x,y),Point(x2,y2))
def main():
    win = GraphWin("UP945169",1000,1000)
    lines(win)
    linesY(win)
    rectangleH = Rectangle(Point(8.8,0),Point(15,8.0))
    rectangleH.draw(win)
    rectangleH = Rectangle(Point(8.8,17),Point(15,25))
    rectangleH.draw(win)
    # rectangle = Rectangle(Point(25,8.0),Point(33,17))
    # rectangle.draw(win)
    # rectangle = Rectangle(Point(50,8.0),Point(42,16))
    # rectangle.draw(win)
    rectangle = Rectangle(Point(25,8.0),Point(35,15))
    rectangle.draw(win)
    rectangle = Rectangle(Point(40,8.0),Point(50,15))
    rectangle.draw(win)
    rectangle = Rectangle(Point(25,33),Point(35,40))
    rectangle.draw(win)
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
    HorizontalSquare(win,100,110,110,100)
    HorizontalSquare(win,200,110,210,100)
    HorizontalSquare(win,300,110,310,100)
    HorizontalSquare(win,400,110,410,100)
    HorizontalSquare(win,500,110,510,100)
    HorizontalSquare(win,500,110,510,100)
    HorizontalSquare(win,500,110,510,100)
    HorizontalSquare(win,600,110,610,100)
    HorizontalSquare(win,700,110,710,100)
    HorizontalSquare(win,800,110,810,100)
    HorizontalSquare(win,200,210,210,200)
    HorizontalSquare(win,300,210,310,200)
    HorizontalSquare(win,400,210,410,200)
    HorizontalSquare(win,500,210,510,200)
    HorizontalSquare(win,600,210,610,200)
    HorizontalSquare(win,700,210,710,200)
    HorizontalSquare(win,800,210,810,200)
    HorizontalSquare(win,300,310,310,300)
    HorizontalSquare(win,400,310,410,300)
    HorizontalSquare(win,600,310,610,300)
    HorizontalSquare(win,500,310,510,300)
    HorizontalSquare(win,700,310,710,300)
    HorizontalSquare(win,800,310,810,300)
    HorizontalSquare(win,400,410,410,400)
    HorizontalSquare(win,500,410,510,400)
    HorizontalSquare(win,600,410,610,400)
    HorizontalSquare(win,800,410,810,400)
    HorizontalSquare(win,700,410,710,400)
    HorizontalSquare(win,500,510,510,500)
    HorizontalSquare(win,600,510,610,500)
    HorizontalSquare(win,700,510,710,500)
    HorizontalSquare(win,800,510,810,500)
    HorizontalSquare(win,600,610,610,600)
    HorizontalSquare(win,700,610,710,600)
    HorizontalSquare(win,800,610,810,600)
    HorizontalSquare(win,700,710,710,700)
    HorizontalSquare(win,800,710,810,700)
    HorizontalSquare(win,800,810,810,800)