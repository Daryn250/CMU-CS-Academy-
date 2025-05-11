from cmu_graphics import *
# don't forget to run: pip install cmu-graphics
# attempt at making magnets, the mouse attracts the cube
app.stepsPerSecond=60
boss = Circle(200,200,15,fill='Green')
boss.d=[10,-18]
player = Rect(200-12.5,200-12.5,25,25,fill='gray')
player.d=[10,-15]
ground=Rect(0,399,400,400,fill=None)
gravity=1
air_resistance=1.01
friction=1.09
affected_air_resistance=[]
collist_circles=[]
collist_squares=[]
collist_circles.append(boss)
collist_squares.append(player)
affected_air_resistance.append(boss)
affected_air_resistance.append(player)
mouse=[200,200]
def onStep():
    for obj in affected_air_resistance:
        if air_resistance>0:
            obj.d[0]=obj.d[0]/air_resistance
            obj.d[1]=obj.d[1]/air_resistance
        if friction>0 and obj.hitsShape(ground):
            obj.d[0]=obj.d[0]/friction
            obj.d[1]=obj.d[1]/friction
    
    boss.d[1]+=gravity
    player.d[1]+=gravity
    boss.centerX+=boss.d[0]
    boss.centerY+=boss.d[1]
    player.centerX+=player.d[0]
    player.centerY+=player.d[1]
    for obj in collist_circles:
        if obj.centerX>400-obj.radius:
            obj.centerX=400-obj.radius
            obj.d[0]=-obj.d[0]
        if obj.centerY>400-obj.radius:
            obj.centerY=400-obj.radius
            obj.d[1]=-obj.d[1]/gravity
        if obj.centerX<obj.radius:
            obj.centerX=obj.radius
            obj.d[0]=-obj.d[0]
        if obj.centerY<obj.radius:
            obj.centerY=obj.radius
            obj.d[1]=-obj.d[1]
    for obj in collist_squares:
        if obj.left<0:
            obj.left=0
            obj.d[0]=-obj.d[0]
        if obj.right>400:
            obj.right=400
            obj.d[0]=-obj.d[0]
        if obj.bottom>400:
            obj.bottom=400
            obj.d[1]=-obj.d[1]/gravity
        if obj.top<0:
            obj.top=0
            obj.d[1]=-obj.d[1]
    if player.centerX>mouse[0]:
        player.d[0]-=distance(mouse[0],mouse[1],player.centerX,player.centerY)/1000
    if player.centerX<mouse[0]:
        player.d[0]+=distance(mouse[0],mouse[1],player.centerX,player.centerY)/1000
    if player.centerY>mouse[1]:
        player.d[1]-=distance(mouse[0],mouse[1],player.centerX,player.centerY)/100
    if player.centerY<mouse[1]:
        player.d[1]+=distance(mouse[0],mouse[1],player.centerX,player.centerY)/100
def onMouseMove(mouseX,mouseY):
    mouse[0]=mouseX
    mouse[1]=mouseY
    
cmu_graphics.run()
