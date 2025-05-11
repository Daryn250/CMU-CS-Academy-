from cmu_graphics import *
# don't forget to run: pip install cmu-graphics
# makes a shape using an algorithm of 2 parabolas ontop of eachother

bottom=Oval(200,350,300,50,fill='red',visible=False)
startProgram=Rect(500,500,10,10,fill='red',visible=True)
label=Label(1,200,200,visible=True)
multi=0.4
inMenu=True
color1='black'
menu=Group( # group for the menu
    Rect(0,0,400,400,fill='white'),
    Label('Octagon',50,100,fill='black',align='center'),
    Label('Heptagon',50,150,fill='black',align='center'),
    Label('Hexagon',50,200,fill='black',align='center'),
    Label('Pentagon',50,250,fill='black',align='center'),
    Label('Square',350,100,fill='black',align='center'),
    Label('Triangle',350,150,fill='black',align='center'),
    Label('Star',350,200,fill='black',align='center'),
    Label('Multiple Panels',350,250,fill='black',align='center'),
    Label('One Panel',200,200,fill='black',align='center')
    )
response=app.getTextInput('What shape?') # selection of shape
totalWait=0
if response.lower() == 'octagon':
    totalWait=7
    inMenu=False
if response.lower() == 'heptagon':
    totalWait=8
    inMenu=False
if response.lower() == 'hexagon':
    totalWait=9.4
    inMenu=False
if response.lower() == 'pentagon':
    totalWait=11.2
    inMenu=False
if response.lower() == 'square':
    totalWait=14
    inMenu=False
if response.lower() == 'triangle':
    totalWait=18.7
    inMenu=False
if response.lower() == 'star':
    totalWait=24
    inMenu=False
if response.lower() == 'multiple panels':
    totalWait=27
    inMenu=False
if response.lower() == 'one panel':
    totalWait=28
    inMenu=False

#fix parabola creation
    # 7 for 8 sides
    # 8 for 7 sides
    # 9.4 for 6 sides
    # 11.2 for 5 sides (has a line though)
    # 14 for square
    # 18.7 for triangle
    # 24 for star
    # 27 for multiple panels
    # 28 for one panel

parabolaAmount=8 #amount of parabolas VISIBLE NOT USED

one=Line(50,50,50,350,visible=False,fill=color1) #creation of parabolas
one.dx=0
one.parabola=0
one.wait=0

two=Line(50,50,50,350,visible=False,fill=color1)
two.dx=0
two.parabola=0
two.wait=0

three=Line(50,50,50,350,visible=False,fill=color1)
three.dx=0
three.parabola=0
three.wait=0

four=Line(50,50,50,350,visible=False,fill=color1)
four.dx=0
four.parabola=0
four.wait=0

five=Line(50,50,50,350,visible=False,fill=color1)
five.dx=0
five.parabola=0
five.wait=0

six=Line(50,50,50,350,visible=False,fill=color1)
six.dx=0
six.parabola=0
six.wait=0

seven=Line(50,50,50,350,visible=False,fill=color1)
seven.dx=0
seven.parabola=0
seven.wait=0

eight=Line(50,50,50,350,visible=False,fill=color1)
eight.dx=0
eight.parabola=0
eight.wait=0
### connectors created
connectors=True
connect1=Line(1,1,1,399,visible=connectors,fill=color1)
connect2=Line(1,1,1,399,visible=connectors,fill=color1)
connect3=Line(1,1,1,399,visible=connectors,fill=color1)
connect4=Line(1,1,1,399,visible=connectors,fill=color1)
connect5=Line(1,1,1,399,visible=connectors,fill=color1)
connect6=Line(1,1,1,399,visible=connectors,fill=color1)
connect7=Line(1,1,1,399,visible=connectors,fill=color1)
connect8=Line(1,1,1,399,visible=connectors,fill=color1)
connect9=Line(1,1,1,399,visible=connectors,fill=color1)
connect10=Line(1,1,1,399,visible=connectors,fill=color1)
connect11=Line(1,1,1,399,visible=connectors,fill=color1)
connect12=Line(1,1,1,399,visible=connectors,fill=color1)
connect13=Line(1,1,1,399,visible=connectors,fill=color1)
connect14=Line(1,1,1,399,visible=connectors,fill=color1)
connect15=Line(1,1,1,399,visible=connectors,fill=color1)
connect16=Line(1,1,1,399,visible=connectors,fill=color1)

# if parabolas Visible
if startProgram.visible==True:
    if parabolaAmount>0:
        one.visible=True
    if parabolaAmount>1:
        two.visible=True
    if parabolaAmount>2:
        three.visible=True
    if parabolaAmount>3:
        four.visible=True
    if parabolaAmount>4:
        five.visible=True
    if parabolaAmount>5:
        six.visible=True
    if parabolaAmount>6:
        seven.visible=True
    if parabolaAmount>7:
        eight.visible=True
# moving parabolas to their next place
def movePara(para):
    para.centerX+=para.dx
    if para.centerX<=200:
        para.dx+=1.5
        para.parabola+=1
        para.y1=50+(para.parabola/multi)
        para.y2=350+(para.parabola/multi)
    elif para.centerX>200:
        para.dx-=1.5
        para.parabola-=1
        para.y1=50+(para.parabola/multi)
        para.y2=350+(para.parabola/multi)
    # main step    
def onStep():
    if inMenu==True: #menu
        menu.toFront()
    else:
        menu.visible=False
    one.wait+=1 # increasing the wait time for each line
    two.wait+=1
    three.wait+=1
    four.wait+=1
    five.wait+=1
    six.wait+=1
    seven.wait+=1
    eight.wait+=1
    
    
    movePara(one) #moves para1 right away 
    label.value=one.parabola
        
    
    if two.wait>totalWait*1: #checking if enough time has passed
        movePara(two)
    if three.wait>totalWait*2:
        movePara(three)
    if four.wait>totalWait*3:
        movePara(four)
    if five.wait>totalWait*4:
        movePara(five)
    if six.wait>totalWait*5:
        movePara(six)
    if seven.wait>totalWait*6:
        movePara(seven)
    if eight.wait>totalWait*7:
        movePara(eight)
        
    # connecting every single parabola, i could've done it a lot more efficiently but it's funnier to show to high level programmers and watch them die inside
    connect1.x1=one.x1
    connect1.y1=one.y1
    connect1.x2=two.x1
    connect1.y2=two.y1
    
    connect2.x1=one.x2
    connect2.y1=one.y2
    connect2.x2=two.x2
    connect2.y2=two.y2
    
    connect3.x1=two.x1
    connect3.y1=two.y1
    connect3.x2=three.x1
    connect3.y2=three.y1    
    
    connect4.x1=two.x2
    connect4.y1=two.y2
    connect4.x2=three.x2
    connect4.y2=three.y2
    
    connect5.x1=three.x1
    connect5.y1=three.y1
    connect5.x2=four.x1
    connect5.y2=four.y1
    
    connect6.x1=three.x2
    connect6.y1=three.y2
    connect6.x2=four.x2
    connect6.y2=four.y2
    
    connect7.x1=four.x1
    connect7.y1=four.y1
    connect7.x2=five.x1
    connect7.y2=five.y1
    
    connect8.x1=four.x2
    connect8.y1=four.y2
    connect8.x2=five.x2
    connect8.y2=five.y2
    
    connect9.x1=five.x1
    connect9.y1=five.y1
    connect9.x2=six.x1
    connect9.y2=six.y1
    
    connect10.x1=five.x2
    connect10.y1=five.y2
    connect10.x2=six.x2
    connect10.y2=six.y2
    
    connect11.x1=six.x1
    connect11.y1=six.y1
    connect11.x2=seven.x1
    connect11.y2=seven.y1
    
    connect12.x1=six.x2
    connect12.y1=six.y2
    connect12.x2=seven.x2
    connect12.y2=seven.y2
    
    connect13.x1=seven.x1
    connect13.y1=seven.y1
    connect13.x2=eight.x1
    connect13.y2=eight.y1
    
    connect14.x1=seven.x2
    connect14.y1=seven.y2
    connect14.x2=eight.x2
    connect14.y2=eight.y2
    
    connect15.x1=eight.x1
    connect15.y1=eight.y1
    connect15.x2=one.x1
    connect15.y2=one.y1
    
    connect16.x1=eight.x2
    connect16.y1=eight.y2
    connect16.x2=one.x2
    connect16.y2=one.y2
    
def onKeyHold(keys): #tracing for the parabola's path
    if 'a' in keys:
        Circle(one.x1,one.y1,1,fill='red')
    if 'd' in keys:
        Circle(one.x1,one.y2,1,fill='red')
cmu_graphics.run()
