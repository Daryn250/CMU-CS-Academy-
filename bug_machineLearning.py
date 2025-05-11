from cmu_graphics import *
# don't forget to run: pip install cmu-graphics
# unfinished
import random
size = 10

class gridsquare:
    def __init__(self,x,y):
        self.shape = Rect(x,y,400/size,400/size,fill='white',border='black',borderWidth = 0.3)
        self.contains = None
    def update(self):
        self.shape.fill='white'
        
def bugbrain(new):
    connections = {}
    input_nodes = ['a','b','c','d','e']
    output_nodes = ['1','2','3','4','5']
    if new:
        # give it a random node tree
        foo = input_nodes + output_nodes
        weight = (random.randint(0,400)/10)-2
        
        connections.
        
print(bugbrain(True))


everyBug = []
class bug:
    def __init__(self,x,y):
        self.fill = 'blue'
        self.data = []
        self.x = x
        self.y = y
        self.parent = all[self.x][self.y]
        self.parent.shape.fill = self.fill
        self.genes = {} # connections to nodes and their weights
        everyBug.append(self)
    def update_data(self):
        self.data.append(neighbor_data(self.x,self.y))
        self.data.append(touchingWalls(self.x,self.y))
        print(self.data)
    def move(self, dir):
        if dir == 'up':
            all[self.x][self.y-1].contains = self
            all[self.x][self.y-1].shape.fill = self.fill
            self.parent.contains = None
            self.parent.shape.fill='white'
            self.y-=1
        if dir == 'down':
            all[self.x][self.y+1].contains = self
            all[self.x][self.y+1].shape.fill = self.fill
            self.parent.contains = None
            self.parent.shape.fill='white'
            self.y+=1
        if dir == 'left':
            all[self.x-1][self.y].contains = self
            all[self.x-1][self.y].shape.fill = self.fill
            self.parent.contains = None
            self.parent.shape.fill='white'
            self.x-=1
        if dir == 'right':
            all[self.x+1][self.y].contains = self
            all[self.x+1][self.y].shape.fill = self.fill
            self.parent.contains = None
            self.parent.shape.fill='white'
            self.x+=1
        self.parent = all[self.x][self.y]

all = []
for i in range(size):
    all.append([])
for x in range(size):
    for y in range(size):
        a = gridsquare((x*400)/size,(y*400)/size)
        all[x].insert(y,a)

def neighbor_data(x,y):
    data = {}
    if x>0:
        data.update({"left": all[x-1][y]})
    if x<size:
        data.update({"right": all[x+1][y]})
    if y>0:
        data.update({"up": all[x][y-1]})
    if y<size:
        data.update({"down": all[x][y+1]})
    return data

def touchingWalls(x,y):
    data = []
    if x==0:
        data.append("left")
    if x==size:
        data.append("right")
    if y==0:
        data.append("up")
    if y==size:
        data.append("down")
    return data

# data nodes:
# neighbor data
# touching walls
# if crammed, die

# action nodes:
# move nodes
# reproduce

# create randomized weights for each brain at start, ones with better weights will live better
all[1][1].contains = bug(1,1)
for x in all:
    for y in x:
        if y.contains!=None:
            Label('s',y.shape.centerX,y.shape.centerX)

def interperetConnections(data):
    pass
def onKeyPress(key):
    for bug in everyBug:
        bug.move(key)
cmu_graphics.run()
