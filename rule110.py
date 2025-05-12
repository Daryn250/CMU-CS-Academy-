#rule 110
from cmu_graphics import *
import math
import time
size = 1000
app.setMaxShapeCount(size*size)

all_shape = Group()

rule = {
    '111':0,
    '110':1,
    '101':1,
    '100':0,
    '011':1,
    '010':1,
    '001':1,
    '000':0
}



def applyRule(a,rule):
    next = []
    for x in range(size):
        current = ''
        if x-1>-1:
            current += str(a[x-1])
        else:
            current += '0'
        current += str(a[x])
        if x+1<size:
            current += str(a[x+1])
        else:
            current+= '0'
        if current != '':
            next.insert(x,rule.get(current))
    return next



def drawFromArray(a):
    culling = a.copy()
    copy3 = a.copy()
    
    for e in range(size):
        for i in range(size):
            cc = 0
            if culling[e][i] > 0:
                for j in range(size):
                    if i+j>size-1:
                        break
                    if culling[e][i+j]>0:
                        culling[e][i+j] = 0
                        cc+=1
                    else:
                        break
                culling[e][i] = cc
            
                        
    
    
    for x1 in range(size):
        for y1 in range(size):
            if culling[x1][y1] > 0:
                r = math.floor(((x1+1)*255)/size)
                g = math.floor(((y1+1)*255)/size)
                b = 255
                all_shape.add(Rect((x1*app.height)/size,((y1*app.height)/size),(app.height/(size)),(app.height/size)*culling[x1][y1],fill=rgb(r,g,b)))



app.array = []
for i in range(size):
    app.array.append([])
    for e in range(size):
        app.array[i].append(0)
app.array[0][size-1] = 1
app.cur = 0

app.drawn = False
app.stepsPerSecond = 60
def onStep():
    
    
    if app.cur<size-1:
        app.array[app.cur+1] = applyRule(app.array[app.cur],rule)
        app.cur+=1
    elif app.drawn == False:
        all_shape.clear()
        drawFromArray(app.array)
        app.drawn = True

def onResize():
    if app.cur>=size-1:
        app.drawn = False
        

cmu_graphics.run()