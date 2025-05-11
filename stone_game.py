from cmu_graphics import *
# don't forget to run: pip install cmu-graphics
#stone game, kinda like pokemon except unfinished and just a theory
import random
import math
battle_screen = Group(Rect(0,0,400,400,fill=rgb(69,69,69)),Rect(12.5,12.5,375,375,fill=rgb(90,90,90)),
    Line(0,200,400,200,fill=rgb(69,69,69),lineWidth=15),Rect(30,30,100,140,fill='gray'),
    Rect(150,30,100,140,fill='gray'),Rect(270,30,100,140,fill='gray')
    ,Rect(30,225,100,140,fill='gray'),
    Rect(150,225,100,140,fill='gray'),Rect(270,225,100,140,fill='gray'))
battle_screen.visible=False
settings_menu = Group(Rect(50,50,300,300,fill='Black',opacity=70),Rect(0,0,400,400,fill='Black',opacity=40))
settings_menu.visible=False

state = "Game"
player_turn = True
app.steps_per_second = 60

class make_move: #make a move
    def __init__(self,type,name,damage_range,design,effects,cd,description='indescribably cool'):
        self.name = name
        self.type = type
        self.damage = damage_range
        self.shape = design
        self.shape.border = 'black'
        self.effects = effects
        self.cooldown = cd
        self.description = description
        self.shape.toFront()
        
def use_move(move,use,used):
    types = ["attack","buff","heal","effect","special"]
    if move.type == types[0]:
        used.chp -= random.randint(self.damage[0],self.damage[1])
    if move.type == types[1]:
        use.effects.append(self.effects)
    if move.type == types[2]:
        heal = random.randint(self.damage[0],self.damage[1])
    if move.type == types[3]:
        damage -= random.randint(self.damage[0],self.damage[1])
        used.effects.append(move.effects)

class create_stone:
    def __init__(self,name,classification,damage_min,damage_max,hp,chp,effects,mohs,level,level_multi,color,x,y,radius,moves):
        self.name = name
        self.classification = classification
        self.damage_min = damage_min
        self.damage_max = damage_max
        self.hp = hp
        self.chp = chp
        self.effects = effects
        self.mohs = mohs
        self.level = level
        self.level_multi = level_multi
        self.shape = Circle(x,295,radius,fill=color)
        self.x = x
        self.y = y
        self.moves = moves

class create_enemy:
    def __init__(self,name,classification,damage_min,damage_max,hp,chp,effects,mohs,level,level_multi,color,x,y,radius):
        self.name = name
        self.classification = classification
        self.damage_min = damage_min
        self.damage_max = damage_max
        self.hp = hp
        self.chp = chp
        self.effects = effects
        self.mohs = mohs
        self.level = level
        self.level_multi = level_multi
        self.shape = Circle(x,100,radius,fill=color)
        self.x = x
        self.y = y

player_stones = [
    create_stone("Stone", "Metamorphic", 3, 5, 10, 10, None, 3, 1, 1.15, 'darkGray',80,295,40,[
    make_move("attack","Hit",(3,5),Rect(150,30,50,50,fill='red',visible=True),None,0,'A simple attack. Deals a range of damage, scales with level.'),
    make_move("effect","Smash",(1,5),Rect(210,30,50,50,fill='blue',visible=True),None,2,'Smashes the opponent, has a chance to stun.'),
    make_move("heal","Heal",(2,2),Rect(270,30,50,50,fill='green',visible=True),None,1,'Heals a stone of your choice.')]
    ),
    create_stone("Pumice", "Igneous", 6, 10, 5, 5, None, 1, 1, 1.15, 'lightGray',200,295,40,[
    make_move("attack","Scald",(5,6),Rect(150,30,50,50,fill='red',visible=False),None,0),
    make_move("effect","Melt",(1,2),Rect(210,30,50,50,fill='blue',visible=False),"Burning",2),
    make_move("buff","Lava Barrier",(2,2),Rect(270,30,50,50,fill='lime',visible=False),"Lava Barrier",4)],
    ),
    create_stone("Stone", "Metamorphic", 3, 5, 10, 10, None, 3, 1, 1.15, 'darkGray',320,295,40,[
    make_move("attack","Hit",(3,5),Rect(150,30,50,50,fill='red',visible=False),None,0),
    make_move("effect","Smash",(1,5),Rect(210,30,50,50,fill='red',visible=False),None,2),
    make_move("heal","Heal",(2,2),Rect(270,30,50,50,fill='red',visible=False),None,1)]
    )]
    # need to create the system for attacking and types of attacks
    
                 
enemy_stones = [ create_enemy("Stone", "Metamorphic", 3, 5, 10, 5, None, 3, 1, 1.15, 'darkGray',80,100,40),
                create_enemy("Stone", "killingmyself", 3, 5, 10, 10, None, 3, 1, 1.15, 'darkGray',200,100,40),
                create_enemy("Me", "Metermorphic", 3, 5, 11, 10, None, 3, 1, 1.15, 'red',320,100,40)]

enemy_turn_screen= Rect(0,200,400,200,fill=gradient('black','gray',start='top'),opacity=0)
player_turn_screen= Rect(0,0,400,200,fill=gradient('black','gray',start='bottom'),opacity=0)

tooltip = Rect(200,200,170,80,fill='black',opacity=50,visible=False)
hp_style= [
Label('0',0,0,fill='white',size=15),
Label('0',0,0,fill='white',size=10),
Label('0',0,0,fill='white',size=12),
Label('0',0,0,fill='white',size=12),
Label('0',0,0,fill='white',size=12),
Label('0',0,0,fill='white',size=12),
Line(0,0,0,0,fill='black',lineWidth=20),
Line(0,0,0,0,fill='red',lineWidth=20)
    ]
move_style= [
    Label('0',0,0,fill='white',size=15),
    Label('0',0,0,fill='white',size=12),
    Label('0',0,0,fill='white',size=12),
    Label('0',0,0,fill='white',size=12),
    Label('0',0,0,fill='white',size=12),
    Label('0',0,0,fill='white',size=12)
    ]

def tooltipUpdate(show,style,values,x,y,theme,tooltint):
    tooltip.visible = show
    tooltip.centerX = x+(tooltip.width/2)
    tooltip.centerY = y+(tooltip.height/2)
    tooltip.fill=rgb(tooltint[0],tooltint[1],tooltint[2])
    tooltip.toFront()
    if style == 'hp':
        for obj in hp_style:
            obj.visible=False
        hp_style[0].value = values[0]
        hp_style[0].left = x+10
        hp_style[0].top = y+10
        hp_style[0].fill=theme
        
        hp_style[1].value = values[1]
        hp_style[1].left = x+10
        hp_style[1].top = y+25
        hp_style[1].fill=theme
        
        hp_style[2].value = "HP: " + str(values[2]) + "/"+ str(values[3])
        hp_style[2].left = x+10
        hp_style[2].top = y+40
        
        hp_style[3].value = "ATK: " + str(values[4]) + "-"+ str(values[5])
        hp_style[3].left = hp_style[2].right+10
        hp_style[3].top = y+40
        
        hp_style[4].value = "MOHS: " + str(values[6])
        hp_style[4].left = hp_style[3].right+10
        hp_style[4].top = y+40
        
        hp_style[5].value = "LVL: " + str(values[7])
        hp_style[5].left = tooltip.right-40
        hp_style[5].top = y+10
        
        hp_style[6].x1 = 0
        hp_style[6].x2 = 150
        hp_style[6].centerX = tooltip.centerX
        hp_style[6].y1 = y+65
        hp_style[6].y2 = y+65
        
        calc = (150/values[3])*values[2]
        
        hp_style[7].x1 = hp_style[6].left
        hp_style[7].x2 = hp_style[6].left+calc
        hp_style[7].y1 = y+65
        hp_style[7].y2 = y+65
        
        widths_added = hp_style[2].width + hp_style[3].width + hp_style[4].width +30
        if hp_style[1].width>widths_added:
            tooltip.width = hp_style[1].width+20
        else:
            tooltip.width = widths_added + 10
    
        if tooltip.right>400: #going off page
            tooltip.right=401
            hp_style[0].left = tooltip.left+10
            hp_style[1].left = tooltip.left+10
            hp_style[2].left = tooltip.left+10
            hp_style[3].left = hp_style[2].right+10
            hp_style[4].left = hp_style[3].right+10
            hp_style[5].left = tooltip.right-40
            hp_style[6].centerX = tooltip.centerX
            hp_style[7].x1 = hp_style[6].left
            hp_style[7].x2 = hp_style[6].left+calc
        
        for obj in hp_style:
            obj.visible=True
    if style == 'move':
        mv = move_style
        for obj in move_style:
            obj.visible=False
        if tooltip.right>400:
            tooltip.right = 400
        mv[0].value = values[0]
        mv[0].toFront()
        mv[0].left = tooltip.left + 10
        mv[0].top = tooltip.top+10
        
        mv[1].value = values[1] + ' type'
        mv[1].toFront()
        mv[1].right = tooltip.right - 10
        mv[1].top = tooltip.top+10
        
        if values[1] == 'attack':
            mv[2].value = "Damage: "+str(values[2])
        else:
            mv[2].value = "Chance: "+str((values[2][0]/values[2][1])*100) + '%'
        mv[2].toFront()
        mv[2].left = tooltip.left + 10
        mv[2].top = tooltip.top+30
        
        if values[3] == None:
            mv[3].visible=False
        else:
            mv[3].value = values[3]
        mv[3].toFront()
        mv[3].left = tooltip.left + 10
        mv[3].top = tooltip.top+45
        
        mv[4].value = 'Cooldown: '+ str(values[4])
        mv[4].toFront()
        mv[4].right = tooltip.right - 10
        mv[4].top = tooltip.top+30
        
        mv[5].value = values[5]
        mv[5].toFront()
        mv[5].left = tooltip.left + 10
        mv[5].bottom = tooltip.bottom-10
        
        for obj in move_style:
            obj.visible=True
        for obj in mv:
            obj.toFront()
        if 0==1: ## testcase
            if mv[5].width+20<mv[2].width  + mv[4].width + 40:
                tooltip.width = mv[2].width + mv[4].width + 40
            else:
                tooltip.width = mv[5].width+20
        pass
    pass

mouseShape=Circle(200,200,1,fill='white')

global stats_available
stats_available = True

stats= [Rect(0,000,400,200,opacity=50),
    Label('name',30,30,align='left',fill='white',size=30),
    Label('Classification: ',30, 55,align='left',fill='white',size=15),
    Label('Health:',30,90,align='left',fill='white',size=15),
    Label('Attack:',30,120,align='left',fill='white',size=15),
    Label('Mohs:',30,150,align='left',fill='white',size=15),
    Label('lvl',370,30,align='right',fill='white',size=15),
    Label('slot',370,180,align='right',fill='white',size=10),
    Rect(140,20,190,70,fill='gray')
    ]

for stat in stats:
    stat.visible=False
    
def displayStats(name,classification,hp,chp,atk,atkmin,mohs,lvl,slot):
    stats[1].value = name
    stats[1].left=30
    stats[2].value = classification
    stats[2].left=30
    stats[3].value = 'Health: ' + str(hp) +'/'+str(chp)
    stats[3].left=30
    stats[4].value = 'Attack: ' + str(atkmin) +'-'+str(atk)
    stats[4].left=30
    stats[5].value = '  Mohs: '+ str(mohs)
    stats[5].left=20
    stats[6].value = 'Level ' + str(lvl)
    stats[7].value = "Slot "+ str(slot)
    stats[7].left = 30

# fix the order:
for stone in player_stones:
    for move in stone.moves:
        move.shape.toFront()
        move.shape.visible=False

app.steps = 0
def onStep():
    app.steps+=1
    if state == "Game":
        battle_screen.visible=True
        # mouse hover on player stones
        for stone in player_stones:
            if mouseShape.hitsShape(stone.shape):
                if stone.shape.radius<50:
                    stone.shape.radius+=(51-(stone.shape.radius))/5
            else:
                if stone.shape.radius>40:
                    stone.shape.radius-=(51-(stone.shape.radius))/5
            for move in stone.moves:
                if stats[0].visible==False:
                    move.shape.visible=False
            
        if player_turn:
            if enemy_turn_screen.opacity>2:
                enemy_turn_screen.opacity-=2
            if player_turn_screen.opacity<50:
                player_turn_screen.opacity+=2
            
            
            
        if not player_turn:
            if enemy_turn_screen.opacity<50:
                enemy_turn_screen.opacity+=2
            if player_turn_screen.opacity>2:
                player_turn_screen.opacity-=2
            
            
            
            
            
            
            
            pass
    if state == "Pause":
        pass
    if state == "Walk":
        pass
    
def onMouseMove(mouseX,mouseY):
    mouseShape.centerX=mouseX
    mouseShape.centerY=mouseY
    tooltipUpdate(False, None,None,mouseX,mouseY,'white',[0,0,0])
    for obj in hp_style:
        obj.visible=False
    for obj in move_style:
        obj.visible=False
    for stone in enemy_stones:
        if stone.shape.hitsShape(mouseShape):
            if stats[0].visible==False:
                tooltipUpdate(True, 'hp',[stone.name,stone.classification,stone.chp,stone.hp,stone.damage_min,stone.damage_max,stone.mohs,stone.level],mouseX,mouseY,'red',[20,0,0])
    for stone in player_stones:
        if stone.shape.hitsShape(mouseShape):
            if stats[0].visible==False:
                tooltipUpdate(True, 'hp',[stone.name,stone.classification,stone.chp,stone.hp,stone.damage_min,stone.damage_max,stone.mohs,stone.level],mouseX,mouseY,'white',[0,0,0])
    for stone in player_stones:
        for move in stone.moves:
            if move.shape.hitsShape(mouseShape) and move.shape.visible==True:
                if stats[0].visible==True:
                    tooltip.toFront()
                    tooltipUpdate(True,'move',[move.name,move.type,move.damage,move.effects,move.cooldown,move.description],mouseX,mouseY,'white',[0,5,0])
current = 0
last = 0
def onMousePress(mouseX,mouseY):
    global current
    global last
    for stone in player_stones:
        if mouseShape.hitsShape(stone.shape):
            for move in stone.moves:
                move.shape.visible=False
            if stone == player_stones[0]:
                current = 1
                
            if stone == player_stones[1]:
                current = 2
                
            if stone == player_stones[2]:
                current = 3
                
            if current!=last:
                for stat in stats:
                    stat.visible=True
                for move in stone.moves:
                    move.shape.visible=True
                    move.shape.toFront()    
                displayStats(stone.name,stone.classification,stone.hp,stone.chp,stone.damage_max,stone.damage_min,stone.mohs,stone.level,current)
                
                last = current
            
            elif current==last:
                for stat in stats:
                    stat.visible=False
                for move in stone.moves:
                    move.shape.visible=False
                last = 0
    for i in range(20):
        print('\n')
    for stone in player_stones:
        for move in stone.moves:
            if move.shape.visible==True:
                print(move.name)

def onKeyPress(key):
    global player_turn
    if key=='t':
        if player_turn==True:
            player_turn=False
        elif player_turn==False:
            player_turn=True
cmu_graphics.run()
