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
        self.posX = random.randrange(1,50) * 10
        self.posY = random.randrange(1,50) * 10
        robit.botNum += 1
        self.gameSprite = Circle(Point(self.posX,self.posY),5) # graphic position

    def SpawnRobits(count):
        for i in range(count):
            if i >= len(robit._allRobits):
                thisRobit = robit()
                robit._allRobits.append(thisRobit)
                robit._liveRobits.append(thisRobit)
            else:
                robit._allRobits[i].posX = random.randrange(1,49) * 10
                robit._allRobits[i].posY = random.randrange(1,49) * 10
                robit._allRobits[i].gameSprite = Circle(Point(robit._allRobits[i].posX,robit._allRobits[i].posY),5)

    def MoveRobits():
        for thisRobit in robit._liveRobits:
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
    _moveSet = [(-10,-10),(0,-10),(+10,-10),(-10,0),(0,0),(10,0),(-10,10),(0,10),(10,10)]
    color = "green"
    def __init__(self) -> None:
        self.name = "hero"
        self.posX = 250  
        self.posY = 250
        self.gameSprite = Circle(Point(self.posX,self.posY),5)

    def ValidMove(dir):
        if thisGuy.posX + hero._moveSet[dir][0] > 500 or thisGuy.posX + hero._moveSet[dir][0] < 10:
            print("bad move")
            return False
        elif thisGuy.posY + hero._moveSet[dir][1] > 500 or thisGuy.posY + hero._moveSet[dir][1] < 10:
            print("bad move")
            return False
        else:
            thisGuy.gameSprite.move(hero._moveSet[dir][0],hero._moveSet[dir][1])
            thisGuy.posX += hero._moveSet[dir][0]
            thisGuy.posY += hero._moveSet[dir][1]
            return True

    def MoveInput(self):
        while(True):
            key = thisWindow.getKey()
            key = key.upper()
            match key:
                case 'Q':
                    if hero.ValidMove(0):
                      break
                    else:
                        continue
                case 'W':
                    if hero.ValidMove(1):
                      break
                    else:
                        continue
                case 'E':
                    if hero.ValidMove(2):
                      break
                    else:
                        continue
                case 'A':
                    if hero.ValidMove(3):
                      break
                    else:
                        continue
                case 'S':
                    if hero.ValidMove(4):
                      break
                    else:
                        continue
                case 'D':
                    if hero.ValidMove(5):
                      break
                    else:
                        continue
                case 'Z':
                    if hero.ValidMove(6):
                      break
                    else:
                        continue
                case 'X':
                    if hero.ValidMove(7):
                      break
                    else:
                        continue
                case 'C':
                    if hero.ValidMove (8):
                      break
                    else:
                        continue
                case 'T':
                    self.Teleport()
                    break
                case 'G':
                    self.HeroWait()
                    break
                case _:
                    continue
        
    def Teleport(self):
        self.posX = random.randrange(1,49) * 10
        self.posY = random.randrange(1,49) * 10
        self.gameSprite.undraw()
        self.gameSprite = Circle(Point(self.posX,self.posY),5)
        self.gameSprite.setFill(hero.color)
        self.gameSprite.draw(thisWindow)

    def HeroWait():
        
        pass


class explosion:
    _allExplosions = []
    _boomPosX = []
    _boomPosY = []
    _color="red"
    def __init__(self,posX,posY) -> None:
        self.gameSprite = Rectangle(Point(posX+5,posY+5),Point(posX-5,posY-5))
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
        if robit._liveRobits[A].posX == thisGuy.posX and robit._liveRobits[A].posY == thisGuy.posY:
            currentLevel = 0
            print("Game Over")
            NewLevel()

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

    #print("checks: " + str(count))
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
            boom.gameSprite.setFill(explosion._color)
            boom.gameSprite.draw(thisWindow)

    graveyard.clear()

def DrawGrid(thisWindow):
    for i in range(51): #draw grid lines
        vert = Line(Point((i*10)-5,0),Point((i*10)-5,510)) # verticals
        horz = Line(Point(0,(i*10)-5),Point(510,(i*10)-5)) # horizontals
        vert.setOutline('white')
        horz.setOutline('white')
        vert.draw(thisWindow)
        horz.draw(thisWindow)
    border = Rectangle(Point(0,0),Point(510,510))
    border.setOutline("black")
    border.setWidth(10)
    border.draw(thisWindow)

def NewLevel():
    for i in range(len(explosion._allExplosions)):
        explosion._allExplosions[0].gameSprite.undraw()
        del explosion._allExplosions[0]

    for thisRobit in robit._allRobits:
        thisRobit.gameSprite.undraw()
        if thisRobit in robit._deadRobits:
            robit._liveRobits.append(thisRobit)
            robit._deadRobits.remove(thisRobit)

    robit.SpawnRobits(currentLevel*2 + 20)

    for thisRobit in robit._allRobits:
        thisRobit.gameSprite.setFill(robit.color)
        thisRobit.gameSprite.draw(thisWindow)
    thisGuy.gameSprite.undraw()
    thisGuy.posX = 250
    thisGuy.posY = 250
    thisGuy.gameSprite = Circle(Point(thisGuy.posX,thisGuy.posY),5)
    thisGuy.gameSprite.setFill(hero.color)
    thisGuy.gameSprite.draw(thisWindow)
     


def main():
    print (hero._moveSet)
    global thisWindow
    global currentLevel
    global thisGuy
    thisWindow = GraphWin('Robits',600,550)
    DrawGrid(thisWindow)
    
    currentLevel = 1
    thisGuy = hero()
    thisGuy.gameSprite.setFill(hero.color)
    thisGuy.gameSprite.draw(thisWindow)



    while True:
        if len(robit._liveRobits) == 0:
            currentLevel+=1
            NewLevel()
        thisGuy.MoveInput()
        robit.MoveRobits()
        FindCollisions()




if __name__ == "__main__":
    main()
