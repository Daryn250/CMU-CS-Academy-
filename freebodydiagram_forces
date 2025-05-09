from cmu-academy import *
# don't forget to run: pip install cmu-graphics
# forces
# each force (should) get a line showing that it exists and what direction it is. I made this in physics
circ = Circle(200,200,15,fill='blue')
circ.xforces=[10]
circ.yforces=[1]
app.stepsPerSecond=60
draw_forces=True
walls_absorb_energy=1.5
friction=0
gravity=0
forcelinex = Line(circ.centerX,circ.centerY,circ.centerX,circ.centerY,arrowStart=False,arrowEnd=False,visible=draw_forces,fill='red')
forceliney = Line(circ.centerX,circ.centerY,circ.centerX,circ.centerY,arrowStart=False,arrowEnd=False,visible=draw_forces,fill='red')

def onStep():
    #add all forces together and add to ball
    circ.totalx=0
    circ.totaly=0
    for force in circ.xforces:
        circ.totalx+=force
    for force in circ.yforces:
        circ.totaly+=force
    circ.centerX+=circ.totalx
    circ.centerY+=circ.totaly
    #friction and other standard forces
    for i in range(len(circ.xforces)):
        circ.xforces[i]=circ.xforces[i]/(friction+1)
    for i in range(len(circ.yforces)):
        circ.yforces[i]=circ.yforces[i]/(friction+1)
    if gravity!=0:
        circ.yforces.append(gravity)
    #walls
    if 400-circ.radius<circ.centerX:
        circ.centerX=400-circ.radius
        for i in range(len(circ.xforces)):
            circ.xforces[i]=-(circ.xforces[i]/(walls_absorb_energy+1))
    if circ.radius>circ.centerX:
        circ.centerX=circ.radius
        for i in range(len(circ.xforces)):
            circ.xforces[i]=-(circ.xforces[i]/(walls_absorb_energy+1))
    if 400-circ.radius<circ.centerY:
        circ.centerY=400-circ.radius
        for i in range(len(circ.yforces)):
            circ.yforces[i]=-(circ.yforces[i]/(walls_absorb_energy+1))
    if circ.radius>circ.centerY:
        circ.centerY=circ.radius
        for i in range(len(circ.yforces)):
            circ.yforces[i]=-(circ.yforces[i]/(walls_absorb_energy+1))
    # drawing forces
    posx_force=0
    negx_force=0
    posy_force=0
    negy_force=0
    if draw_forces==True:
        for force in circ.xforces:
            if force<0:
                negx_force+=force
            else:
                posx_force+=force
        if negx_force<0:
            forcelinex.startArrow=True
        else:
            forcelinex.startArrow=False
        if posx_force>0:
            forcelinex.endArrow=True
        else:
            forcelinex.endArrow=False
        forcelinex.x1=circ.centerX+(negx_force*10)
        forcelinex.y1=circ.centerY
        forcelinex.x2=circ.centerX+(posx_force*10)
        forcelinex.y2=circ.centerY
        for force in circ.yforces:
            if force<0:
                negy_force+=force
            else:
                posy_force+=force
        if negy_force<0:
            forceliney.startArrow=True
        else:
            forceliney.startArrow=False
        if posy_force>0:
            forceliney.endArrow=True
        else:
            forceliney.endArrow=False
        forceliney.x1=circ.centerX
        forceliney.y1=circ.centerY+(negy_force*10)
        forceliney.x2=circ.centerX
        forceliney.y2=circ.centerY+(posy_force*10)
cmu-graphics.run()
