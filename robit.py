import random
from graphics import *

class robit:
    _allRobits = []
    _liveRobits = []
    _deadRobits = []
    botNum = 0
    color = "blue"
    def __init__(self) -> None:
        self.name = "bot"+str(robit.botNum)
        self.num = robit.botNum
        self.deadBot = False
        self.posX = random.randrange(1,49) * 10
        self.posY = random.randrange(1,49) * 10
        robit.botNum += 1
        self.gameSprite = Circle(Point(self.posX,self.posY),5) # graphic position

    def SpawnRobits(count):
        for i in range(count):
            thisRobit = robit()
            robit._allRobits.append(thisRobit)
            robit._liveRobits.append(thisRobit)
            #print(thisRobit.name + " is at: " + str(thisRobit.posX) + ", " + str(thisRobit.posY))

    def MoveRobits():
        #print("Guy: " + str(thisGuy.posX) + ", " + str(thisGuy.posY))
        for thisRobit in robit._liveRobits:
            #print(str(thisRobit.name) + ": " + str(thisRobit.posX) + ", " + str(thisRobit.posY))
            if thisRobit.posX < thisGuy.posX:
                thisRobit.posX += 10
                thisRobit.gameSprite.move(10,0)
            elif thisRobit.posX > thisGuy.posX:
                thisRobit.posX -= 10
                thisRobit.gameSprite.move(-10,0)
            if thisRobit.posY < thisGuy.posY:
                thisRobit.posY += 10
                thisRobit.gameSprite.move(0,10)
            elif thisRobit.posY > thisGuy.posY:
                thisRobit.posY -= 10
                thisRobit.gameSprite.move(0,-10)

class hero:
    color = "green"
    def __init__(self) -> None:
        self.name = "hero"
        self.posX = 250  
        self.posY = 250
        self.gameSprite = Circle(Point(self.posX,self.posY),5)

    def MoveHero(self):
        key = thisWindow.getKey()
        key = key.upper()
        match key:
            case 'Q':
                self.posX -= 10
                self.posY -= 10
                self.gameSprite.move(-10,-10)
            case 'W':
                self.posY -= 10
                self.gameSprite.move(0,-10)
            case 'E':
                self.posX += 10
                self.posY -= 10
                self.gameSprite.move(+10,-10)
            case 'A':
                self.posX -= 10
                self.gameSprite.move(-10,0)
            case 'S':
                self.posY += 0
            case 'D':
                self.posX += 10
                self.gameSprite.move(10,0)
            case 'Z':
                self.posX -= 10
                self.posY += 10
                self.gameSprite.move(-10,10)
            case 'X':
                self.posY += 10
                self.gameSprite.move(0,10)
            case 'C':
                self.posX += 10
                self.posY += 10
                self.gameSprite.move(10,10)


class explosion:
    _allExplosions = []
    _boomPosX = []
    _boomPosY = []
    _color="red"
    def __init__(self,posX,posY) -> None:
        self.gameObject = Rectangle(Point(posX+5,posY+5),Point(posX-5,posY-5))
        self.posX = posX
        self.posY = posY
        explosion._boomPosX.append(posX)
        explosion._boomPosY.append(posY)
    
    def CheckDupe(posX,posY):  
        for boom in explosion._allExplosions:
            if boom.posX == posX and boom.posY == posY:
                return True
            else:
                continue
        return False

    
def FindCollisions():
    #compare all pairs of bots and see if botA is on the same tile
    count = 0
    graveyard = []
    print("live: " + str(len(robit._liveRobits)))
    print("dead: " + str(len(robit._deadRobits)))  

    for A in range(len(robit._liveRobits)):
        for B in range(A+1,len(robit._liveRobits)):
            count+=1
            if robit._liveRobits[A].posX == robit._liveRobits[B].posX and robit._liveRobits[A].posY == robit._liveRobits[B].posY:
                if robit._liveRobits[A] not in graveyard:
                    graveyard.append(robit._liveRobits[A])
                    robit._allRobits[A].deadBot = True
                if robit._liveRobits[B] not in graveyard:
                    graveyard.append(robit._liveRobits[B])
                    robit._allRobits[B].deadBot = True

        for boom in explosion._allExplosions:
            count+=1
            if robit._liveRobits[A].posX == boom.posX and robit._liveRobits[A].posY == boom.posY:
                if robit._liveRobits[A] not in graveyard:
                    graveyard.append(robit._liveRobits[A])
                    robit._allRobits[A].deadBot = True

    print("checks: " + str(count))
    print("dead this turn " + str(len(graveyard)))
    for dead in graveyard:
        if dead in robit._liveRobits:
            robit._liveRobits.remove(dead)
        if dead not in robit._deadRobits:
            robit._deadRobits.append(dead)
        dead.gameSprite.undraw()

        if explosion.CheckDupe(dead.posX,dead.posY) == False:
            boom = explosion(dead.posX,dead.posY)
            explosion._allExplosions.append(boom)
            boom.gameObject.setFill(explosion._color)
            boom.gameObject.draw(thisWindow)

    graveyard.clear()

def DrawGrid(thisWindow):
    for i in range(50): #draw grid lines
        vert = Line(Point((i*10)-5,0),Point((i*10)-5,500)) # verticals
        horz = Line(Point(0,(i*10)-5),Point(500,(i*10)-5)) # horizontals
        vert.setOutline('white')
        horz.setOutline('white')
        vert.draw(thisWindow)
        horz.draw(thisWindow)

def main():
    global thisWindow
    thisWindow = GraphWin('Robits',600,500)
    # global allRobits
    global thisGuy
    allRobits = []

    DrawGrid(thisWindow)

    thisGuy = hero()
    thisGuy.gameSprite.setFill(hero.color)
    thisGuy.gameSprite.draw(thisWindow)

    robit.SpawnRobits(20)
    for thisRobit in robit._allRobits:
        thisRobit.gameSprite.setFill(robit.color)
        thisRobit.gameSprite.draw(thisWindow)


    while True:
        click = thisWindow.checkMouse()
        if click:
            if click.x > 500:
                break
            else:
                click = ''

        thisGuy.MoveHero()
        robit.MoveRobits()
        FindCollisions()


    thisWindow.close()



if __name__ == "__main__":
    main()
