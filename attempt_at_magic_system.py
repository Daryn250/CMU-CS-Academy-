from cmu_graphics import *
# don't forget to run: pip install cmu-graphics
# magic system
app.background=rgb(21,20,21)
templine=Line(500,500,500,500,fill='red',visible=False)
s=6
grid=Group()
hitting=[]
rem=[]
for x in range(s):
    for y in range(s):
        g=Rect((rounded(400/s)/2)+x*rounded(400/s),(rounded(400/s)/2)+y*rounded(400/s),10,10,align='center',fill='white')
        grid.add(g)
for x in range(s-1):
    for y in range(s-1):
        g=Rect((rounded(400/s))+x*rounded(400/s),(rounded(400/s))+y*rounded(400/s),10,10,align='center',fill='white')
        grid.add(g)
def onMouseDrag(mouseX,mouseY):
    for g in grid:
        if g.contains(mouseX,mouseY):
            hitting.append(g)
    for g in hitting:
        if len(hitting)>0:
            one=hitting[0]
            templine.visible=True
            templine.x1=one.centerX
            templine.y1=one.centerY
            templine.x2=mouseX
            templine.y2=mouseY
        if len(hitting)>2:
            one=hitting.pop(0)
            two=hitting.pop(1)
            Line(one.centerX,one.centerY,two.centerX,two.centerY,fill='red')
            templine.visible=False
        if len(hitting)>4:
            for obj in hitting:
                hitting.remove(obj)
def onMouseRelease(mouseX,mouseY):
    templine.visible=False
cmu_graphics.run()
