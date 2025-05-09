from cmu-graphics import *
# remember to run: pip install cmu-graphics
import random
import math
gravity=0.15
particles = []
global_movement = []
app.stepsPerSecond=1000
app.steps=0
def createWater(amt):
    for i in range(amt):
        water = Circle(200,0,30,fill='blue',opacity=10)
        #water.radius =random.randint(100,1000)/10
        water.dx=(random.randint(1000,2000)/100)-15
        water.dy=0
        water.r = (random.randint(100,200)/100)-1.5
        water.onGround=False
        water.label = Label(((water.dx)*1000)/1000,water.centerX,water.centerY,size=10)
        water.number = Label(i,200,10+(i*10))
        particles.append(water)
createWater(3)
def onStep():
    app.steps+=1
    global_movement.clear()
    for water in particles:
        water.label.centerX=water.centerX
        water.label.centerY=water.centerY
        water.number.centerX=water.centerX
        
        water.centerX+=water.dx
        water.centerY+=water.dy
        water.dx=water.dx/1.005
        water.dy+=gravity
        water.dy+=random.randint(10,20000)/100000
        if water.onGround==True:
            water.dx += water.r
            water.r=water.r/1.1
            water.rotateAngle+=water.r
            
        if water.centerY>400-water.radius:
            water.dy=-water.dy/(random.randint(2000,3000)/1000)
            water.centerY=400-water.radius
            water.onGround=True
        if water.centerX<0+water.radius:
            water.centerX=0+water.radius
            water.dx=-water.dx/(random.randint(1000,3000)/1000)
            water.onGround=True
        if water.centerX>400-water.radius:
            water.centerX=400-water.radius
            water.dx=-water.dx/(random.randint(1000,3000)/1000)
            water.onGround=True
        else:
            water.onGround=False
        avg_movement= (water.dx+water.dy)/2
        water.label.value = (rounded(avg_movement*1000)/1000)
        global_movement.append((pythonRound(avg_movement*1000))/1000)
        
        color = abs(rounded(avg_movement)*40)
        if color>255:
            color=255
        water.fill=rgb(color,255,255)
        if water.centerY==400-water.radius and water.dx<0.1 and water.dx>-0.1:
            water.dx=0
            water.dy=0
def onKeyPress(key):
    if key == 'up':
        for water in particles:
            water.dx+=(random.randint(1000,5000)/1000)-3
            water.dy-=(random.randint(1000,5000)/500)
    if key == 'p':
        print(global_movement)
        for water in particles:
            print(water.r)
                
cmu-graphics.run()
