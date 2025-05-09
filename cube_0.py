from cmu-graphics import *
# don't forget to run: pip install cmu-graphics
### This file was copied from CS1, 3rd Edition on 2023-02-28.
# makes a cube. this was an attempt from Game Programming 1 for a creative project.

background = Rect(-400,-400,800,800,fill=gradient(rgb(50,173,167),rgb(29,102,98),start='top-left'))
movingRectangle = Rect(100,100,150,150,fill=None,border='black')
movingRectangle2 = Rect(50,50,150,150,fill=None,border='black')
line1 = Line(50,50,100,100)
line2 = Line(200,50,250,100)
line3 = Line(50,200,100,250)
line4 = Line(200,200,250,250)
def onMouseMove(mouseX,mouseY):
    movingRectangle.centerX = 100+mouseX/3
    movingRectangle.centerY = 100+mouseY/3
    movingRectangle2.centerX = 150+mouseX/5
    movingRectangle2.centerY = 150+mouseY/5
    line1.x1 = movingRectangle.centerX-75
    line1.y1 = movingRectangle.centerY-75
    line1.x2 = movingRectangle2.centerX-75
    line1.y2 = movingRectangle2.centerY-75
    line2.x1 = movingRectangle.centerX+75
    line2.y1 = movingRectangle.centerY+75
    line2.x2 = movingRectangle2.centerX+75
    line2.y2 = movingRectangle2.centerY+75
    line3.x1 = movingRectangle.centerX-75
    line3.y1 = movingRectangle.centerY+75
    line3.x2 = movingRectangle2.centerX-75
    line3.y2 = movingRectangle2.centerY+75
    line4.x1 = movingRectangle.centerX+75
    line4.y1 = movingRectangle.centerY-75
    line4.x2 = movingRectangle2.centerX+75
    line4.y2 = movingRectangle2.centerY-75
    background.centerX = mouseY
    background.centerY = mouseX
    if mouseY>145:
        line1.fill=rgb(mouseY-145,mouseY-145,mouseY-145)
        line4.fill=rgb(mouseY-145,mouseY-145,mouseY-145)
        line2.fill=rgb(mouseY-145,mouseY-145,mouseY-145)
        line3.fill=rgb(mouseY-145,mouseY-145,mouseY-145)
        movingRectangle.border=rgb(mouseY-145,mouseY-145,mouseY-145)
        movingRectangle2.border=rgb(mouseY-145,mouseY-145,mouseY-145)
    if mouseY>350:
        background.fill=gradient(rgb(29,102,98),rgb(50,173,167),start='top-left')
    if mouseX>350:
        background.fill=gradient(rgb(50,173,167),rgb(29,102,98),start='top-left')
    pass
cmu-graphics.run()
