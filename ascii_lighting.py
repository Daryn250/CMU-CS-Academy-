from cmu-graphics import *
# don't forget to run: pip install cmu-graphics
# could be optimized further by looping over nodes not in the radius of the mouse
xamt = 10
yamt = 10
array = []
ascii = ["$","B","*","k","O","f",";","\"",".",""]
for y in range(yamt):
    array.append([])
for y in range(yamt):
    for x in range(xamt):
        label = Label("",x*(400/xamt)+20,y*(400/yamt)+20)
        array[y].append(label)

def onMouseMove(mouseX,mouseY):
    for y in array:
        for label in y:
            for i in range(len(ascii)):
                if distance(label.centerX,label.centerY,mouseX,mouseY)<(200):
                    if distance(label.centerX,label.centerY,mouseX,mouseY)>i*20:
                        label.value = ascii[i]
                else:
                    pass
cmu-graphics.run()
