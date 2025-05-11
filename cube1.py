from cmu_graphics import *
# make sure that you run: pip install cmu-graphics
#Cube
### it takes a few seconds for the cube to load (second set of lines is based off of time offset)
###color combination
colorForIdiots='purple'
opposite='black'
###experimental Settings
pixelize=False
debug=False
firstVisible=True
secondVisible=True
connectors=True
loadingScreens=True
centerLine=False
# default 10
divideAmount=10
#default 1.05
parabolamultiplier=1.05
# pixelize doesnt work because the amount of shapes created is too much for the computer to handle,
#don't turn it on, i'll fix it later :D
# delay before 2nd starts, default 99
delay=99
# top offset default 50
topOffset=50
# top offset 2 default 131
topOffset2=131
# bottom offset default 269
bottomOffset=269
# bottom offset 2 default 350
bottomOffset2=350
# speed default 1
speed=1
#left boundary default 99
leftBoundary=99
# default 302
rightBoundary1=302
# default 301
rightBoundary2=301

### buttons
buttonsOn=False
debugbutton=Rect(0,0,10,10,fill='red',visible=buttonsOn)
fvbutton=Rect(0,10,10,10,fill='red',visible=buttonsOn)
svbutton=Rect(0,20,10,10,fill='red',visible=buttonsOn)
connectorsbutton=Rect(0,30,10,10,fill='red',visible=buttonsOn)

### Dev Settings !!!!DO NOT TOUCH!!!!
center=Line(200,0,200,400,fill=colorForIdiots,visible=centerLine)

engineer100=Rect(0,0,400,400,fill=colorForIdiots,visible=loadingScreens)
loading=Label('LOADING...',200,200,fill=opposite,visible=loadingScreens,align='center')

parabola1=Line(2,375,398,375,lineWidth=5,fill=colorForIdiots,visible=debug)
parabola2=Line(2,380,398,380,lineWidth=5,fill=colorForIdiots,visible=debug)

line1=Line(100,100,100,275,fill=colorForIdiots,visible=firstVisible)
line2=Line(302,100,302,275,fill=colorForIdiots,visible=firstVisible)
line3=Line(100,100,100,275,fill=colorForIdiots,visible=secondVisible)
line4=Line(302,100,302,275,fill=colorForIdiots,visible=secondVisible)

parabolaSwitch=Rect(500,200,5,5,fill='red',visible=True)
psw=Rect(500,210,5,5,fill='red',visible=True)
dirswitch=Rect(500,205,5,5,fill='red',visible=True)

connector1=Line(line1.x1,line1.y1,line3.x1,line3.y1,fill=colorForIdiots,visible=connectors)
connector2=Line(line1.x2,line1.y2,line3.x2,line3.y2,fill=colorForIdiots,visible=connectors)

connector3=Line(line2.x2,line2.y2,line4.x2,line4.y2,fill=colorForIdiots,visible=connectors)
connector4=Line(line2.x2,line2.y2,line4.x2,line4.y2,fill=colorForIdiots,visible=connectors)

connector5=Line(line1.x2,line1.y2,line4.x2,line4.y2,fill=colorForIdiots,visible=connectors)
connector6=Line(line1.x2,line1.y2,line4.x2,line4.y2,fill=colorForIdiots,visible=connectors)

connector7=Line(line2.x2,line2.y2,line4.x2,line4.y2,fill=colorForIdiots,visible=connectors)
connector8=Line(line2.x2,line2.y2,line4.x2,line4.y2,fill=colorForIdiots,visible=connectors)

startLater=Label(1,300,300,fill=colorForIdiots,visible=debug)
istp=Rect(500,220,5,5,fill='red',visible=True)

line1one=Circle(line1.centerX,line1.centerY,5,fill='red',visible=debug)
line2two=Circle(line2.centerX,line2.centerY,5,fill='yellow',visible=debug)
line3three=Circle(line3.centerX,line3.centerY,5,fill='green',visible=debug)
line4four=Circle(line4.centerX,line4.centerY,5,fill='blue',visible=debug)


##### 
pixels=Group(
    Rect(500,500,1,1,fill='gold')
    )

def pixelerHit(x,y):
    pixels.add(Rect(x-8,y-8,16,16,fill=colorForIdiots))

def onStep():
    incat=parabola2.x2
### main
    startLater.value+=1
    if parabolaSwitch.visible==True:
        parabola1.x2=parabola1.x2/parabolamultiplier
    elif parabolaSwitch.visible==False:
        parabola1.x2=parabola1.x2*parabolamultiplier
    
   
    if parabola1.x2<3 and parabolaSwitch.visible==True:
        parabolaSwitch.visible=False
        #Circle(line1.x1,line1.y1,2,fill='blue')
    elif parabola1.x2>398 and parabolaSwitch.visible==False:
        parabolaSwitch.visible=True
        
        
### side
    if startLater.value>99:
        if psw.visible==True:
            parabola2.x2=parabola2.x2/parabolamultiplier
        elif psw.visible==False:
            parabola2.x2=parabola2.x2*parabolamultiplier
            
        if parabola2.x2<3 and psw.visible==True:
            psw.visible=False
            Circle(line3.x1,line3.y1,2,fill='blue',visible=debug)
        elif parabola2.x2>398 and psw.visible==False:
            psw.visible=True
### Main
    
    if dirswitch.visible==True:
        line1.y1=topOffset+parabola1.x2/divideAmount
        line1.y2=bottomOffset2+((parabola1.x2-(2*parabola1.x2))/divideAmount)
        
        line2.y1=topOffset2+((parabola1.x2-(2*parabola1.x2))/divideAmount)
        line2.y2=bottomOffset+parabola1.x2/divideAmount
    if istp.visible==True:
        line3.y1=topOffset2+((incat-(2*incat))/divideAmount)
        line3.y2=bottomOffset+incat/divideAmount
        
        line4.y1=topOffset+incat/divideAmount
        line4.y2=bottomOffset2+((incat-(2*incat))/divideAmount)
            
    if dirswitch.visible==False:
        line1.y1=topOffset2+((parabola1.x2-(2*parabola1.x2))/divideAmount)
        line1.y2=bottomOffset+parabola1.x2/divideAmount
        
        line2.y1=topOffset+parabola1.x2/divideAmount
        line2.y2=bottomOffset2+((parabola1.x2-(2*parabola1.x2))/divideAmount)
        
    if istp.visible==True:
        line4.y1=topOffset2+((incat-(2*incat))/divideAmount)
        line4.y2=bottomOffset+incat/divideAmount
            
        line3.y1=topOffset+incat/divideAmount
        line3.y2=bottomOffset2+((incat-(2*incat))/divideAmount)
    if istp.visible==False:
        line3.y1=topOffset2+((incat-(2*incat))/divideAmount)
        line3.y2=bottomOffset+incat/divideAmount
            
        line4.y1=topOffset+incat/divideAmount
        line4.y2=bottomOffset2+((incat-(2*incat))/divideAmount)
### other lines
    if istp.visible==True and line3.centerX>rightBoundary2:
        istp.visible=False
    if istp.visible==False and line3.centerX<leftBoundary:
        istp.visible=True
        
    if startLater.value>delay:
        engineer100.visible=False
        loading.visible=False
        if istp.visible==True:
            line3.centerX+=speed
            line4.centerX-=speed
        if istp.visible==False:
            line3.centerX-=speed
            line4.centerX+=speed
        
### main
    if dirswitch.visible==True:
        line1.centerX+=speed
        line2.centerX-=speed
    if dirswitch.visible==False:
        line1.centerX-=speed
        line2.centerX+=speed
    
    if dirswitch.visible==True and line1.centerX>rightBoundary1:
        dirswitch.visible=False
        line1.centerX-=speed
    if dirswitch.visible==False and line1.centerX<leftBoundary:
        dirswitch.visible=True
        line1.centerX+=speed
### other lines
### panels
    connector1.x1=line1.x1
    connector1.y1=line1.y1
    connector1.x2=line3.x1
    connector1.y2=line3.y1
    connector2.x1=line1.x2
    connector2.y1=line1.y2
    connector2.x2=line3.x2
    connector2.y2=line3.y2
    
    connector3.x1=line3.x1
    connector3.y1=line3.y1
    connector3.x2=line2.x1
    connector3.y2=line2.y1
    connector4.x1=line3.x2
    connector4.y1=line3.y2
    connector4.x2=line2.x2
    connector4.y2=line2.y2
    
    connector5.x1=line1.x1
    connector5.y1=line1.y1
    connector5.x2=line4.x1
    connector5.y2=line4.y1
    connector6.x1=line1.x2
    connector6.y1=line1.y2
    connector6.x2=line4.x2
    connector6.y2=line4.y2
    
    connector7.x1=line2.x1
    connector7.y1=line2.y1
    connector7.x2=line4.x1
    connector7.y2=line4.y1
    connector8.x1=line2.x2
    connector8.y1=line2.y2
    connector8.x2=line4.x2
    connector8.y2=line4.y2
    
    line1one.centerX=line1.centerX
    line1one.centerY=line1.centerY
    line2two.centerX=line2.centerX
    line2two.centerY=line2.centerY
    line3three.centerX=line3.centerX
    line3three.centerY=line3.centerY
    line4four.centerX=line4.centerX
    line4four.centerY=line4.centerY
    ###pixelization
    if pixelize==True:
        for i in range(25):
            y=i*16
            pixeler=Rect(0,y,16,16,fill='red')
            pixels.clear()
            pixeler.centerX+=16
            if pixeler.hitsShape(line1):
                pixelerHit(pixeler.centerX,pixeler.centerY)
    ###
    engineer100.toFront()
    loading.toFront()
def onKeyHold(keys):
    if debug==True:
        if ('1' in keys):
            Circle(line1.x1,line1.y1,1,fill='red')
            Circle(line1.x2,line1.y2,1,fill='red')
        if ('2' in keys):
            Circle(line2.x1,line2.y1,1,fill='red')
            Circle(line2.x2,line2.y2,1,fill='red')
        if ('3' in keys):
            Circle(line3.x1,line3.y1,1,fill='red')
            Circle(line3.x2,line3.y2,1,fill='red')
        if ('4' in keys):
            Circle(line4.x1,line4.y1,1,fill='red')
            Circle(line4.x2,line4.y2,1,fill='red')
def onMouseMove(mouseX,mouseY):
    if debugbutton.hits(mouseX,mouseY):
        debugbutton.fill='darkRed'
    else:
        debugbutton.fill='red'
def onMousePress(mouseX,mouseY):
    if debugbutton.hits(mouseX,mouseY):
        debug=True
        debugbutton.fill='blue'
cmu_graphics.run()
    
 
    
