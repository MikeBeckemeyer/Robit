import random
from graphics import *

#Base class for all robits
class robit:
    allRobits = [] #all instances of the class created
    liveRobits = [] #list of live bots on the board during gameplay
    deadRobits = [] #bots that have died during gameplay
    botNum = 0
    color = "blue"
    def __init__(self) -> None:
        self.name = "bot"+str(robit.botNum)
        self.num = robit.botNum
        self.posX = random.randrange(1,50) * 10 #Set random position for robit when it is created 
        self.posY = random.randrange(1,50) * 10
        robit.botNum += 1
        self.gameSprite = Circle(Point(self.posX,self.posY),5) # gamesprite with position and size

    #spawn robits.  If all Robits is longer than the # of bots needed more are created, otherwise the existing instances of robits are re-used
    def SpawnRobits(count):
        for i in range(count):
            if i >= len(robit.allRobits): # creating new robits 
                thisRobit = robit()
                robit.allRobits.append(thisRobit)
                robit.liveRobits.append(thisRobit)
            else: # repurposing existings instances of robits
                robit.allRobits[i].posX = random.randrange(1,49) * 10
                robit.allRobits[i].posY = random.randrange(1,49) * 10
                robit.allRobits[i].gameSprite = Circle(Point(robit.allRobits[i].posX,robit.allRobits[i].posY),5)
                robit.liveRobits.append(robit.allRobits[i]) 

    #if the game is still going, move all living bots towards the player, both X and Y axis, both allowed for diagonal movement
    def MoveRobits():
        if scores.gameOver == False:
            for thisRobit in robit.liveRobits:
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

#player class
class hero:
    moveSet = [(-10,-10),(0,-10),(+10,-10),(-10,0),(0,0),(10,0),(-10,10),(0,10),(10,10)] #list of possible moves mapped to each button.  Q,W,E,S... keys
    color = "green"
    def __init__(self) -> None:
        self.name = "hero"
        self.posX = 250  
        self.posY = 250
        self.gameSprite = Circle(Point(self.posX,self.posY),5) #game sprite with position and size

    #checks to see if a move entered by the player is valid.  invalid moves include moving outside of boundaries of play.  If the move is allowed, it will move the player
    #if the move is bad, return false to allow a different move input from player
    def ValidMove(dir):
        if thisGuy.posX + hero.moveSet[dir][0] > 500 or thisGuy.posX + hero.moveSet[dir][0] < 10:
            print("bad move")
            return False
        elif thisGuy.posY + hero.moveSet[dir][1] > 500 or thisGuy.posY + hero.moveSet[dir][1] < 10:
            print("bad move")
            return False           
        else: #Player move performed
            thisGuy.gameSprite.move(hero.moveSet[dir][0],hero.moveSet[dir][1])
            thisGuy.posX += hero.moveSet[dir][0]
            thisGuy.posY += hero.moveSet[dir][1]
            return True

    #get inputs from player.  
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
                case 'Y':
                    if self.safeTeleport():
                        break
                    else:  
                        continue
                case _:
                    continue

    #teleport the player to a random location on the map. could include a spot that kills player when bots move  
    def Teleport(self):
        self.posX = random.randrange(1,49) * 10
        self.posY = random.randrange(1,49) * 10
        self.gameSprite.undraw()
        self.gameSprite = Circle(Point(self.posX,self.posY),5)
        self.gameSprite.setFill(hero.color)
        self.gameSprite.draw(thisWindow)

    #teleport the player to a safe location.  
    def safeTeleport(self):
        dangerLocation = [] #list of all locations that contain a robit or are within 1 move of a robit
        allMarkers = [] #small red marker to show dangerous teleport locations

        if scores.safeTeleports >= 1: #make sure the player has a safe teleport available
            scores.safeTeleports -= 1
            for i in range(len(robit.liveRobits)):
                dangerLocation.append( (robit.liveRobits[i].posX,robit.liveRobits[i].posY ) ) #check each robit position and add to list
                for x in range(len(hero.moveSet)):
                    dangerLocation.append( ((robit.liveRobits[i].posX + hero.moveSet[x][0]),(robit.liveRobits[i].posY + hero.moveSet[x][1])) ) #get all 9 move locations the robit could move to and add to list
            
            for i in range(len(dangerLocation)): #Draw a small marker on all locations taht are dangerous.  
                marker = Circle(Point(dangerLocation[i][0],dangerLocation[i][1]),3)
                marker.setFill('red')
                marker.draw(thisWindow)
                allMarkers.append(marker)
            time.sleep(.5) 
            for i in range(len(allMarkers)): #remove all markers drawn after pause
                allMarkers[i].undraw()

            #picks a random location on the board and compares it to the dangerous locations.  if the random location is dangerous, generates a new one and tries again until teleport is safe
            while (True):
                dest = [ (random.randrange(1,49) * 10, random.randrange(1,49) * 10) ]
                if dest[0] not in dangerLocation:
                    print("safe")
                    self.posX = dest[0][0]
                    self.posY = dest[0][1]
                    self.gameSprite.undraw()
                    self.gameSprite = Circle(Point(self.posX,self.posY),5)
                    self.gameSprite.setFill(hero.color)
                    self.gameSprite.draw(thisWindow)
                    return True
                else:
                    print("bad location, trying again")
                    continue
        else:
            print("no safe teleports available")
            return False

    #bypasses all player inputs until the level is over or the player is killed.  All robits killed while waiting will give the player a safe teleport. 
    def HeroWait(self):
        while(len(robit.liveRobits) > 0):
            time.sleep(.2)
            robit.MoveRobits()
            if PlayerCollision():
                break
            scores.safeTeleports += RobitCollisions()

#explosions from 2 robits colliding
class explosion:
    allExplosions = []
    boomPosX = []
    boomPosY = []
    color="red"
    def __init__(self,posX,posY) -> None:
        self.gameSprite = Rectangle(Point(posX+5,posY+5),Point(posX-5,posY-5))
        self.posX = posX
        self.posY = posY
        explosion.boomPosX.append(posX)
        explosion.boomPosY.append(posY)
    
    #when a robot is killed, check to see if there is already an explosion on that location
    def CheckDupe(posX,posY):  
        for boom in explosion.allExplosions:
            if boom.posX == posX and boom.posY == posY:
                return True
            else:
                continue
        return False

#check the player location for collisions with robits.  if there is a collision, restart new game
def PlayerCollision():
    for A in range(len(robit.liveRobits)):
        if robit.liveRobits[A].posX == thisGuy.posX and robit.liveRobits[A].posY == thisGuy.posY:
            print("Game Over")
            scores.gameOver = True #prevents the rest of game loop from happening after game over
            NewLevel()
            return True
    return False
            
 #compare all pairs of bots and see if A is on the same tile as B or an explosion
 #returns number of bots killed each turn, used for HeroWait()
def RobitCollisions() -> int:
    count = 0
    graveyard = []

    for A in range(len(robit.liveRobits)):#check bot A
        for B in range(A+1,len(robit.liveRobits)): 
            count+=1
            if robit.liveRobits[A].posX == robit.liveRobits[B].posX and robit.liveRobits[A].posY == robit.liveRobits[B].posY: #check bot A against bot B
                if robit.liveRobits[A] not in graveyard:
                    graveyard.append(robit.liveRobits[A])
                if robit.liveRobits[B] not in graveyard:
                    graveyard.append(robit.liveRobits[B])

        for boom in explosion.allExplosions: #check bot A against all explosions
            count+=1
            if robit.liveRobits[A].posX == boom.posX and robit.liveRobits[A].posY == boom.posY:
                if robit.liveRobits[A] not in graveyard:
                    graveyard.append(robit.liveRobits[A])

    #print("checks: " + str(count))
    # clear up live and dead robit lists, remove sprite of dead bots 
    for dead in graveyard:
        if dead in robit.liveRobits:
            robit.liveRobits.remove(dead)
        if dead not in robit.deadRobits:
            robit.deadRobits.append(dead)
        dead.gameSprite.undraw()

        #check if an explosion should be created on this location
        if explosion.CheckDupe(dead.posX,dead.posY) == False:
            boom = explosion(dead.posX,dead.posY)
            explosion.allExplosions.append(boom)
            boom.gameSprite.setFill(explosion.color)
            boom.gameSprite.draw(thisWindow)

    count = len(graveyard)
    graveyard.clear()
    return count #

#draw grid for game and border
def DrawGame(thisWindow):
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

#reset robits, explosions, and hero and start a new level
def NewLevel():
    if scores.gameOver == True:
        scores.currentLevel = 0
        scores.safeTeleports = 0

    scores.gameOver = False
    scores.currentLevel +=1

    #existing instances of explosions are undrawn and deleted
    for i in range(len(explosion.allExplosions)):
        explosion.allExplosions[0].gameSprite.undraw()
        del explosion.allExplosions[0]

    #remove all robits from live and Dead lists.  
    for thisRobit in robit.allRobits:
        thisRobit.gameSprite.undraw()
        if thisRobit in robit.deadRobits:
            robit.deadRobits.remove(thisRobit)
        if thisRobit in robit.liveRobits:
            robit.liveRobits.remove(thisRobit)

    #spawn new robits
    robit.SpawnRobits(scores.currentLevel*3 + 20)
    #draw new robits 
    for thisRobit in robit.allRobits:
        thisRobit.gameSprite.setFill(robit.color)
        thisRobit.gameSprite.draw(thisWindow)

    #reset hero
    thisGuy.gameSprite.undraw()
    thisGuy.posX = 250
    thisGuy.posY = 250
    thisGuy.gameSprite = Circle(Point(thisGuy.posX,thisGuy.posY),5)
    thisGuy.gameSprite.setFill(hero.color)
    thisGuy.gameSprite.draw(thisWindow)

    scores.updateScoreboard()
 
 #stats and rendering of right side of screen with game info
class scores:
    currentLevel = 0
    scoreboard = Text(Point(650,50),str(currentLevel))
    safeTeleports = 10
    gameOver = False

    def updateScoreboard():
        scores.scoreboard.setText("Current Level: " + str(scores.currentLevel) + '\nLiving Robits: ' + str(len(robit.liveRobits)) + '\nDead Robits: ' + str(len(robit.deadRobits)) + '\nSafe Teleports: ' + str(scores.safeTeleports))

    def drawRules():
        rules = Text(Point(630,250),"Controls: \nMove Directions: \nQ W E \nA S D \nZ X C\n\nT - Teleport\n Y - Safe Teleport\n G - Wait\n\n\n\n use wait when you are safe\nfrom robits to earn\nmore safe teleports")

        rules.draw(thisWindow)

def main():
    global thisWindow
    global thisGuy

    thisWindow = GraphWin('Robits',750,550)
    DrawGame(thisWindow)
    scores.drawRules()
    scores.scoreboard.draw(thisWindow)

    thisGuy = hero()
    thisGuy.gameSprite.setFill(hero.color)
    thisGuy.gameSprite.draw(thisWindow)

    while True:
        if len(robit.liveRobits) == 0:
            NewLevel()
        scores.updateScoreboard()
        thisGuy.MoveInput()
        robit.MoveRobits()
        PlayerCollision()
        RobitCollisions()



if __name__ == "__main__":
    main()
