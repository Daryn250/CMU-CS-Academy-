from cmu_graphics import *
import math
# don't forget to run: pip install cmu-graphics
# could be optimized further by looping over nodes not in the radius of the mouse
app.background = rgb(20,20,30)
size = 4
xamt = size*16
yamt = size*9
app.setMaxShapeCount(xamt*yamt)
strength = 10
array = []
ascii = ["$","B","k","O","f","\"",";",".",""]
for y in range(yamt):
    array.append([])
for y in range(yamt):
    for x in range(xamt):
        label = Label("",x*(app.width/xamt)+20,y*(app.height/yamt)+20,align='center',fill='white')
        array[y].append(label)

def onMouseMove(mouseX,mouseY):
    iicsa = ascii[::-1]
    for y in array:
        for label in y:
            
            dist = distance(label.centerX,label.centerY,mouseX,mouseY)
            if strength>100:
                label.value = '$$'
                continue
            if dist!=0:
                k = rounded(len(ascii)*(app.width)/(dist*(100-strength)))
                if dist>(app.width/(dist*(100-strength))):
                    if k<len(ascii):
                        label.value = iicsa[k]
                    else:
                        label.value = ascii[0]
def onResize():
    for y in range(yamt):
        for x in range(xamt):
            array[y][x].centerX = (x*app.width/xamt+20)
            array[y][x].centerY = (y*app.height/yamt+20)

cmu_graphics.run()
