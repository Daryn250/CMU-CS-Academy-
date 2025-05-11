from cmu_graphics import *
# don't forget to run: pip install cmu-graphics
### This file was copied from CS1, 3rd Edition on 2023-02-28.
# most simple version of a world builder, made without for loops

import random
app.background=gradient('gray','darkGray',start='top-left')
drawer = Rect(0,0,20,20,fill=None,border='black',visible=True)
player = Rect(185,185,10,10,fill=rgb(72,125,67),visible=False)
blockCount = Label(0,200,220,align='center')
loadingScreen = Label('Loading.',200,190,align='center',size=20)
loadingBar = Line(0,200,0,200,lineWidth=400,fill='white',opacity=50)
loadingDots = Label(0,100,100,visible=False)
def drawBlock(x,y,color):
    Rect(x-10,y-10,20,20,fill=color)
    pass
def drawerMove():
    drawer.centerX+=20
    blockCount.value+=1
    blockCount.toFront()
    loadingBar.toFront()
    loadingScreen.toFront()
    loadingDots.toFront()
    if drawer.centerX>=400:
        drawer.centerY+=20
        drawer.centerX=10
def onMouseMove(mouseX,mouseY):
    loadingBar.x1=400-blockCount.value
    loadingDots.value+=1
    blockCount.toFront()
    if loadingDots.value==10:
        loadingScreen.value='Loading..'
    elif loadingDots.value==20:
        loadingScreen.value='Loading...'
    elif loadingDots.value==30:
        loadingScreen.value='Loading.'
        loadingDots.value=0
    if player.visible==False:    
        if random.randint(0,1)==1:
            drawBlock(drawer.centerX,drawer.centerY,'lightGray')
            drawer.toFront()
            drawerMove()
        else:
            drawerMove()
            drawer.toFront()
        if blockCount.value>=400:
            player.visible=True
            player.toFront()
            loadingScreen.visible=False
            loadingBar.visible=False
            blockCount.visible=False
def onKeyPress(key):
    if player.visible==True:
        if (key=='up'):
            drawer.centerX=player.centerX
            drawer.centerY=player.centerY-20
            drawBlock(drawer.centerX,drawer.centerY,rgb(173,123,76))
            player.toFront()
            player.centerY-=20
        if (key=='down'):
            drawer.centerX=player.centerX
            drawer.centerY=player.centerY+20
            drawBlock(drawer.centerX,drawer.centerY,rgb(173,123,76))
            player.toFront()
            player.centerY+=20
        if (key=='left'):
            drawer.centerX=player.centerX-20
            drawer.centerY=player.centerY
            drawBlock(drawer.centerX,drawer.centerY,rgb(173,123,76))
            player.toFront()
            player.centerX-=20
        if (key=='right'):
            drawer.centerX=player.centerX+20
            drawer.centerY=player.centerY
            drawBlock(drawer.centerX,drawer.centerY,rgb(173,123,76))
            player.toFront()
            player.centerX+=20
cmu_graphics.run()
