from cmu_graphics import *
import math
# don't forget to run: pip install cmu-graphics
# could be optimized further by looping over nodes not in the radius of the mouse
app.background = rgb(20,20,30)
size = 3
xamt = size*16
yamt = size*9
app.setMaxShapeCount(xamt*yamt)
strength = 10
ascii = ["$","B","k","O","f","\"",";",".",""]
all = Group()

coords = []
for y in range(yamt):
    coords.append([])
    for x in range(xamt):
        coords[y].append(((x*(app.width/xamt))+5, (y*(app.height/yamt)+5)))

def draw(mouseX,mouseY):
    iicsa = ascii[::-1] 
    width = app.width
    for y in range(yamt):
        for x in range(xamt):
            lx, ly = coords[y][x]
            dist = distance(lx,ly,mouseX,mouseY)
            if strength>100:
                all.add(Label("$$$", lx, ly, align = 'center', fill = 'white'))
                continue
            if dist!=0:
                k = rounded(len(ascii)*(width)/(dist*(100-strength)))
                if k==0:
                    continue
                ch = iicsa[k] if k < len(ascii) else ascii[0]
                all.add(Label(ch, lx, ly, align='center', fill='white'))

app.stepsPerSecond = 60
def onMouseMove(mouseX,mouseY):
    all.clear()
    draw(mouseX,mouseY)

def onResize():
    for y in range(yamt):
        coords.insert(y,[])
        for x in range(xamt):
            coords[y].insert(x,((x*(app.width/xamt))+5, (y*(app.height/yamt)+5)))
    draw(0,0)

cmu_graphics.run()
