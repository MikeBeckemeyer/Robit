from cgitb import grey
from ctypes import pointer
import random
from graphics import *


def test():
    col_arr=["violet","indigo","blue","green","yellow","orange","red"]
    workArea = GraphWin('Rainbow Circle', 300, 300) # give title and dimensions
    x=workArea.getWidth()/2 # get x of middle of drawing area
    y=workArea.getHeight()/2 # get y of middle of drawing area

    i=0
    while i<len(col_arr):
        cir=Circle(Point(x, y), 10+10*i)# draw circle with center at middle of drawing area
        cir.setOutline(col_arr[i]) #get a next outline color from color array
        cir.setWidth(4)#set outline width
        cir.draw(workArea)#draw the current circle
        i+=1 # increment counter for iteration
        
    message = Text(Point(workArea.getWidth()/2, 250), 'Click to Exit')
    message.draw(workArea)
    workArea.getMouse()# get mouse to click on screen to exit
    workArea.close() # close the drawing window



class robit:
    _allRobits = []
    botNum = 0
    color = "blue"
    def __init__(self) -> None:
        self.name = "bot"+str(robit.botNum)
        self.posX = random.randrange(1,49) * 10
        self.posY = random.randrange(1,49) * 10
        robit.botNum += 1
        self.gameSprite = Circle(Point(self.posX,self.posY),5) # graphic position

    def SpawnRobits(count):
        for i in range(count):
            thisRobit = robit()
            allRobits.append(thisRobit)
            print(thisRobit.name + " is at: " + str(thisRobit.posX) + ", " + str(thisRobit.posY))

    def MoveRobits():
        print("Guy: " + str(thisGuy.posX))
        for thisRobit in allRobits:
            print(thisRobit.posX)
            if thisRobit.posX < thisGuy.posX:
                thisRobit.posX += 10
                thisRobit.gameSprite.move(thisRobit.posX,thisRobit.posY)
                



class hero:
    color = "green"
    def __init__(self) -> None:
        self.name = "hero"
        self.posX = 250  
        self.posY = 250
        self.gameObject = Circle(Point(self.posX,self.posY),5)



def DrawGrid(thisWindow):
    for i in range(50): #draw grid lines
        vert = Line(Point((i*10)-5,0),Point((i*10)-5,500)) # verticals
        horz = Line(Point(0,(i*10)-5),Point(500,(i*10)-5)) # horizontals
        vert.setOutline('white')
        horz.setOutline('white')
        vert.draw(thisWindow)
        horz.draw(thisWindow)

def main():
    thisWindow = GraphWin('Robits',600,500)
    global allRobits
    global thisGuy
    allRobits = []

    DrawGrid(thisWindow)

    thisGuy = hero()
    thisGuy.gameObject.setFill(hero.color)
    thisGuy.gameObject.draw(thisWindow)

    robit.SpawnRobits(20)
    for thisRobit in allRobits:
        thisRobit.gameSprite.setFill(robit.color)
        thisRobit.gameSprite.draw(thisWindow)


    while True:
        click = thisWindow.getMouse()
        print(click.x)
        if click.x > 500:
            break
        else:
            robit.MoveRobits()
            continue


    thisWindow.close()



if __name__ == "__main__":
    main()
