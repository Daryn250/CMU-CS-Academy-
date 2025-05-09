from cmu-graphics import *
# don't forget to run: pip install cmu-graphics
# this is an unfinished game that I was making, similar to bossfight.py, except I wanted to make it better.
import math as np
import random
# Bossfight to end all bossfights
# things i need:
    # lasers
    # targeting missles
    # bombs

    # player physics
    # player health
    # attack modes

# player init

intensityFilter = Rect(0,0,400,400,fill=None)

app.background = rgb(180,180,180)
player = Rect(200,400,20,20,fill='gray')
player.collisions = True
player.gravity = True
player.vx = 4
player.vy = 3
player.speed = 1
player.ghostImage = Rect(player.left,player.top, player.width, player.height, fill = player.fill, visible=False)
player.ghostImage.vx = 0
player.ghostImage.vy = 0
app.stepsPerSecond = 60

player.gravity = 0.7
player.bounce_friction = 1.2
player.air_resistance = 1.02
player.friction_coefficient =2

player.lx = 0
player.ly = 0
player.onGround = False

particles = []
collider_objs = []
lasers = []
ghostPlatform = []
blackHoles = []
all_objs = []

all_objs.append(player.ghostImage)

def physics_him(target, gravity, bounce_friction, air_resistance, friction_coefficient):
    target.centerX += target.vx
    target.centerY += target.vy
    # gravity
    if gravity>0:
        target.vy+=gravity
    # collisions
    if target.collisions == True:
        if target.right>400:
            target.right = 400
            target.vx = -target.vx/bounce_friction
        if target.left<0:
            target.left = 0
            target.vx = -target.vx/bounce_friction
        if target.bottom>400:
            target.bottom = 400
            target.vy = -target.vy/bounce_friction+1
            try: 
                if target.onGround == False:
                    for i in range(random.randint(1,5)):
                        makeParticles(target.centerX, target.bottom, random.randint(10,30)-20,random.randint(10,30)-20,3,3,target.fill,False,100,False,random.randint(10,30)-20, 60)
            except:
                pass
        if target.top<0:
            target.top = 0
            target.vy = -target.vy/bounce_friction
    # air resistance
    if air_resistance>0:
        target.vx=target.vx/air_resistance
        target.vy=target.vy/air_resistance
    if friction_coefficient>0:
        if target.bottom == 400:
            target.vx = target.vx/friction_coefficient
# attacks
def makeParticles(x,y,vx,vy,xs,ys,color,glowing, opacity, canCollide, rotationSpeed, lifetime):
    particle = Rect(x,y,xs,ys,fill = color)
    particle.centerX = x
    particle.centerY = y
    particle.vx = vx
    particle.vy = vy
    particle.opacity = opacity
    particle.gravity = 0.01
    particle.collisions = canCollide
    particle.rotationSpeed = rotationSpeed
    particle.lifetime = lifetime
    particle.initialLife = lifetime
    particle.glowing = glowing
    if glowing == True:
        particle.glow = Rect(particle.centerX-particle.width,particle.centerY-particle.height, particle.width*5, particle.height*5, fill = gradient(particle.fill, rgb(180,180,180),rgb(180,180,180)), opacity=50)
    else:
        particle.glow = None
    particles.append(particle)
    all_objs.append(particle)
    
def platform(x,y,xs,xy,vx,vy):
    platform = Rect(x,y,xs,xy,fill='lightGray')
    platform.ghost = Rect(x,y,xs,xy,fill='lightGray', visible=False)
    platform.ghost.vx = 0
    platform.ghost.vy = 0
    platform.vx = vx
    platform.vy = vy
    collider_objs.append(platform)
    all_objs.append(platform.ghost)
    ghostPlatform.append(platform.ghost)
    
def Laser(x1,y1,x2,y2,width,color,delay, particlesAllowed):
    laser = Line(x1,y1,x2,y2,fill = 'white', lineWidth = 1)
    laser.finalWidth = width
    laser.delay = delay
    laser.fireColor = color
    laser.damager = None
    laser.particles = particlesAllowed
    lasers.append(laser)
    #all_objs.append(laser)

def laserArray(x1,y1,dir, amt,lifetime):
    for i in range(amt):
        i+=1
        x,y = getPointInDir(x1,y1,(360/amt)*i,100)
        x2,y2 = getPointInDir(x,y,((360/amt)*i)+dir,500)
        Laser(x,y,x2,y2,8,rgb(0,255,255),lifetime, False)
        
def blackHole(x,y,size,force,growing,growto,lifetime):
    #intensityFilter.fill = gradient(rgb(180,180,180),rgb(180,180,180),rgb(100,100,100))
    black_hole = Circle(x,y,size,fill = gradient(rgb(0,0,0),rgb(50,50,50)))
    black_hole.horizon = Circle(x,y,size*3, opacity = 50, fill= gradient('black','black', rgb(50,50,50),rgb(100,100,100),rgb(160,160,160),rgb(180,180,180)))
    black_hole.horizon.toBack()
    black_hole.magnitude = force
    black_hole.growing = growing
    black_hole.maxSize = growto
    black_hole.life = lifetime
    blackHoles.append(black_hole)
    pass

def screenShake(intensity, duration):
    for obj in all_objs:
        obj.beforeScreenShakeX = obj.centerX
        obj.beforeScreenShakeY = obj.centerY
        obj.bvx = obj.vx
        obj.bvy = obj.vy
        obj.vx, obj.vy = 0, 0
        obj.shakeDuration = duration
        obj.shakeIntensity = intensity

 

def collider(main, obj):
    if obj.hitsShape(main):
        # same thnig but wuith y
        if (abs(obj.top - main.bottom) < abs(obj.bottom - main.top)) and (main.vy>0.1):
            main.vy = obj.vy
            main.vx +=obj.vx
            main.vx = main.vx/(main.friction_coefficient)
            main.bottom = obj.top-1
            
        elif (abs(obj.top - main.bottom) > abs(obj.bottom - main.top)) and (main.vy<-0.1):
            main.vy +=obj.vy
            main.vx +=obj.vx
            main.vx = main.vx/(main.friction_coefficient)
            main.top = obj.bottom-1


#### Test Case:
screenShake(0,1)
app.steps = 0
def onStep():
    app.steps +=1
    ## test Case


    ## test Case
    if player.ly+10 >= 398:
        if player.bottom == 400:
            player.onGround = True
    else:
        player.onGround = False
    player.lx = player.centerX
    player.ly = player.centerY
    physics_him(player, player.gravity, player.bounce_friction, player.air_resistance, player.friction_coefficient)
    player.ghostImage.beforeScreenShakeX = player.centerX
    player.ghostImage.beforeScreenShakeY = player.centerY
    
    
    
    for item in collider_objs:
        collider(player,item)
        item.centerX += item.vx
        item.centerY += item.vy
        item.ghost.centerX = item.centerX
        item.ghost.centerY = item.centerY
        item.ghost.beforeScreenShakeX = item.centerX
        item.ghost.beforeScreenShakeY = item.centerY

    for laser in lasers:
        if laser.lineWidth <= laser.finalWidth and laser.fill != laser.fireColor:
            laser.lineWidth += laser.finalWidth/laser.delay
        elif laser.damager == None:
            if laser.particles == True:
                for i in range(random.randint(3,5)):
                    makeParticles(laser.x2,laser.y2,(random.randint(10,30)-20),(random.randint(1,20)-20),5,5,'white',False,100,False,(random.randint(10,20)-10),40)
            laser.damager = Line(laser.x1,laser.y1,laser.x2,laser.y2,fill = laser.fireColor, lineWidth = laser.lineWidth/1.05, opacity = 100)
            
            
        if laser.damager != None and laser.opacity>0:
            laser.opacity-=1
        elif laser.opacity<1:
            lasers.remove(laser)
        if laser.damager != None and laser.damager.opacity>0:
            laser.damager.opacity-=1
    
    for bh in blackHoles:
        bh.life -= 1
        if bh.life > 0:
            if player.hitsShape(bh.horizon):
                if distance(player.centerX,player.centerY,bh.centerX,bh.centerY) > 5:
                    if player.centerX>bh.centerX:
                        player.vx-=bh.magnitude
                    elif player.centerX<bh.centerX:
                        player.vx+=bh.magnitude
                    if player.centerY>bh.centerY:
                        player.vy-=bh.magnitude
                    elif player.centerY<bh.centerY:
                        player.vy+=bh.magnitude
                else:
                    player.centerX = bh.centerX
                    player.centerY = bh.centerY
            if bh.growing:
                if bh.radius<=bh.maxSize:
                    bh.radius+=(bh.maxSize/10)/bh.radius
                    bh.horizon.radius=bh.radius*3
            player.gravity = 0.1
        if bh.life<1:
            player.gravity = 0.7
            bh.opacity -=2
            bh.horizon.opacity-=1
            if bh.opacity<1:
                blackHoles.remove(bh)
                
                
        
    for particle in particles:
        # particle physics
        physics_him(particle, particle.gravity,1,1.2,1.5)
        particle.rotateAngle += particle.rotationSpeed
        if particle.glowing == True:
            particle.glow.centerX = particle.centerX
            particle.glow.centerY = particle.centerY
        # particle lifetime
        particle.lifetime -= 1
        if particle.lifetime <= 100 and particle.opacity>0:
            particle.opacity -=1
            if particle.glowing == True:
                if particle.glow.opacity>0:
                    particle.glow.opacity-=1
        #particle fade
        if particle.lifetime < 0:
            particle.opacity = 0
            if particle.glowing == True:
                particle.glow.opacity = 0
            particles.remove(particle)
            
            
            
    for laser in lasers:
        laser.toFront()
    for obj in collider_objs:
        obj.toFront
    player.toFront()
    player.ghostImage.toFront()
    
    try:
        player.visible=False
        player.ghostImage.visible = True
        for obj in collider_objs:
            obj.visible = False
        for obj in ghostPlatform:
            obj.visible=True
        for obj in all_objs:
            if obj.shakeDuration > 0:
                obj.shakeDuration -= 1
                obj.centerX = (obj.beforeScreenShakeX)-(random.randint(1,obj.shakeIntensity)-(obj.shakeIntensity/2))
                obj.centerY = (obj.beforeScreenShakeY)-(random.randint(1,obj.shakeIntensity)-(obj.shakeIntensity/2))
            else:
                player.visible=True
                obj.centerX = obj.beforeScreenShakeX
                obj.centerY = obj.beforeScreenShakeY
                obj.vx, obj.vy = obj.bvx, obj.bvy
                player.ghostImage.visible = False
                for obj in collider_objs:
                    obj.visible = True
                for obj in ghostPlatform:
                    obj.visible=False
    except:
        pass
    
def onKeyHold(keys):
    if 'a' in keys:
        player.vx-=player.speed/2
    if 'd' in keys:
        player.vx+=player.speed/2    
    if 's' in keys:
        player.vx = 0
        player.vy+=player.speed
        
        if player.bottom > 399:
            player.vy=0
    if 'e' in keys:
        player.vx = 8
        player.vy -= 0.6
    if 'q' in keys:
        player.vx = -8
        player.vy -= 0.6
    
def onKeyPress(key):
    if key == "w":
        player.vy = -15
    if key == 'down':
        screenShake(12,60)
cmu-graphics.run()
