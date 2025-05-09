from cmu-graphics import *
# don't forget to run: pip install cmu-graphics
# this is my first attempt at a wave collapse function, it works but poorly. second attempt is my preferred and works better.


grid = []
app.background='black'
app.stepsPerSecond=10
square_size=10
squares=40
import random
placing = None
biomes={
        'grass':rgb(0,128,0),
        'water':rgb(0,0,200),
        'sand':rgb(255,215,0),
        'stone':rgb(128,128,128),
        'coral':rgb(32, 178, 170)
    }
def fillGrid(x,y, spacing,sizex,sizey):
    for x1 in range(x):
        a=[]
        for y1 in range(y):
            rect = Rect((x1*spacing),(y1*spacing),sizex,sizey,fill='white')
            rect.update=False
            rect.updatable=True
            rect.x=x1
            rect.y=y1
            rect.type=None
            rect.alt=None
            a.insert(y, rect)
        grid.append(a)
fillGrid(squares,squares,10,square_size,square_size)
for column in grid:
    for rect in column:
        if rect.centerX>400 or rect.centerY>400 or rect.centerY<0 or rect.centerX<0:
            print('nah')
        
def advance():    #scrap for now
    for rect in grid:
        if rect.fill!='red':
            for rectsecond in grid:
                if rect.centerX+rect==rectsecond.centerX:
                    rectsecond.update=True
            
def getAdjacent(i, j, m=squares, n=squares):
    adjacent_indices=[]
    if i>0:
        adjacent_indices.append((i-1,j))
    if i+1<m:
        adjacent_indices.append((i+1,j))
    if j>0:
        adjacent_indices.append((i,j-1))
    if j+1<n:
        adjacent_indices.append((i,j+1))
    return adjacent_indices


def onStep():
    if 1==2:
        say('how')
def onMousePress(mouseX,mouseY):
    global placing
    for column in grid:
        for rect in column:
            if placing == None:
                if rect.contains(mouseX,mouseY):
                    if rect.fill=='white':
                        rect.fill='red'
                        rect.update=True
                    elif rect.fill=='red':
                        rect.fill='gray'
                        rect.updatable=False
            else:
                if rect.contains(mouseX,mouseY):
                    rect.type=placing
                    rect.fill = biomes[placing]
                    rect.updatable=False

def most_frequent(List, dict):
    counter = 0
    num = List[0]
    for i in List:
        for x in dict:
            current_frequency = List.count(x)
            if current_frequency > counter:
                counter = current_frequency
                num = x
    return num
    
def squareType(x,y):
    logic=2
    basic_weights=getAdjacent(x,y)
    a=[]
    p=None
    for x,y in basic_weights:
        current_rect = grid[x][y]
        if current_rect.type!=None:
            a.append(current_rect.type)
    if logic==1:
        if len(a)>0:
            for x in biomes:
                p = str(most_frequent(a,biomes))
                if x==p:
                    c=biomes[x]
        else:
            while p ==None:
                for x in biomes:
                    if random.randint(1,20)==1:
                        p= x
                        c=biomes[p]
                        break
    if logic==2:
        for i in range(random.randint(1,5)):
            if random.randint(1,5)==1:
                for x in biomes:
                    if random.randint(1,3)==1:
                        a.append(x)
        if len(a)>0:
            p = choice(a)
            for x in biomes:
                if x==p:
                    c=biomes[x]
        else:
            p = 'grass'
            for x in biomes:
                if x==p:
                    c=biomes[x]
    return p, c

def onKeyPress(key):
    global placing
    if key=='a':
        updateList=[]
        for column in grid:
            for rect in column:
                if rect.update==True and rect.fill=='red':
                    updateList.append(getAdjacent(rect.x,rect.y))
                    rect.update=False
                    rect.updatable=False
                    rect.type, rect.fill=squareType(rect.x,rect.y)
                    
        for box in updateList:
            for coord in box:
                coordx, coordy = coord
                for col in grid:
                    for rect in col:
                        if rect.x == coordx and rect.y==coordy and rect.updatable==True:
                            rect.update=True
                            rect.fill='red'
    
    if key=='1':
        placing = 'grass'
        print('switched to '+placing)
    if key=='2':
        placing = 'water'
        print('switched to '+placing)
    if key=='3':
        placing = 'sand'
        print('switched to '+placing)
    if key=='4':
        placing = 'stone'
        print('switched to '+placing)
    if key=='5':
        placing = None
        print('switched to '+str(placing))
    if key=='space':
        for i in range(squares*2):
            onKeyPress('a')
    if key=='p':
        for i in range(random.randint(1,20)):
            onMousePress(random.randint(0,400),random.randint(0,400))
cmu-graphics.run()
