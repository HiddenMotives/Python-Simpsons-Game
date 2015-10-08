# Author: basprohop

# Description: This is a game where you control Homer (H) and guide him to his home Springfield (S). 
# Functionality: 
#    [*] The game is easily playable along with extensive error checking and response messages to guide the user.
#    [*] Displays and introduction to the user everytime the program is run.
#    [*] Displays conclusion of the game whether the user has won or lost.
#    [*] To guide the user the program displays a directional menu after every turn and when a game file is loaded. 
#    [*] Ability to load custom game files/maps into the program (start positions)
#    [*] Homer can move in 4 compass directions (N, S, E, W)
#    [*] Error message displayed if player tries to move Homer in 4 inter-cardinal directions
#    [*] Error message is displayed if player enters in a value higher than 9. 
#    [*] Player can easily quit the anytime by entering '0' at the directional menu.
#    [*] Debugging mode implemented to toggle debug messages.
#    [*] EPA agents are able to move in all directions (1 square at a time).
#    [*] Prevention of moving Homer into an occupied area.
#    [*] Lose game condition: Drowning (in contact with water)
#    [*] Lose game condition: Freezing (if homer is in alaska for more than 10 turns)
#    [*] Lose game condition: Captured (if homer is captured by the EPA)
#    [*] Win game condition: Win (homer reaches springfield
#    [*] Addition of Homer's personality (chance of him getting distracted)
# Limitations: You will lose your current game status if the program unexpectedly crashes.

import random

ROWS = 20
COLUMNS = 30
AGENTS = 6

#Homer's default positions
START_ROW = 1
START_COLUMN = 1

#Game Blocks
BUILDING = "#"
EMPTY = " "
EPA_AGENT = "E"
HOMER = "H"
SPRINGFIELD = "S"
WATER = "~"

#Game Messages
WIN = ("You've brought Homer back to Springfield. You've won the game...woohoo!")
DROWN = ("Homer is too fat to swim! He drowned. Game Over.")
CAPTURED = ("Homer was captured by the EPA. You lost the game...doh!")
FREEZE = ("Homer Froze to death in the Artic. You failed to bring Homer back to Springfield safely. Game Over.")
BLOCKED = ("A building is no safe haven for Homer, he needs to get back to Springfield!")
DISTRACTED = ("Homer becomes distracted and ignores your command to move.")
QUIT = ("You have abandoned Homer. You lose! Game Over.")
SPACER = ("================================================================")

#Debug mode is On/[Off] (default)
debug = False

def debugHomer(distraction):
    if (debug):
        print ("<<< Number randomly generated =", distraction, ">>>")
        if (distraction > 25) and (distraction <= 100):
            print ("<<< Number = 26 to 100, Homer follows the player's movement instructions >>>")
        elif (distraction >= 1) and (distraction <=25):
            print ("<<< Number = 1 - 25, Homer is distracted >>>")
            print ("<<< Homer becomes distracted and refuses to move >>>")

def debugEPA(agentLocation, EPApos):
#<<< Agent direction: 2, Agent source (r/c): (8/9), Agent destination (r/c): (9/9) >>>
    if (debug):
        i = 0
        while i < AGENTS:
            print ("<<< Agent direction:", EPApos, end="")
            print ("Agent source (r/c): x/x", end="")
            print ("Agent destination (r/c):", agentLocation[0][i],"",agentLocation[1][i], ">>>")
            i = i + 1

def computerTurn(aMaze, agentLocation, articTime):
    i = 0
    while i < AGENTS:
        #Generate a unique moving direction integer for each agent.
        # 1 = EPA move left and down one square, 2 = EPA move down one square, 3 = EPA move right and down one square,
        # 4 = EPA move left one square, 5 = EPA stay put, 6 = EPA move right one square,
        # 7 = EPA move left and up one square, 8 = EPA move up one square, 9 = EPA move right and up one square. 		
        EPApos = random.randint(1,9)
        if EPApos == 1:
            if (aMaze[(agentLocation[0][i])+1][(agentLocation[1][i])-1]) in (SPRINGFIELD, WATER, EPA_AGENT, BUILDING): #Validate if EPA can move.
                pass
            elif (aMaze[(agentLocation[0][i])+1][(agentLocation[1][i])-1]) == HOMER:
                exit (CAPTURED) #Exit program provide proper conclusion.
            else:
                aMaze[(agentLocation[0][i])][(agentLocation[1][i])] = EMPTY
                aMaze[(agentLocation[0][i])+1][(agentLocation[1][i])-1] = EPA_AGENT
                agentLocation[0][i] += 1
                agentLocation[1][i] -= 1
        elif EPApos == 2:
            if (aMaze[(agentLocation[0][i])+1][(agentLocation[1][i])]) in (SPRINGFIELD, WATER, EPA_AGENT, BUILDING):
                pass
            elif (aMaze[(agentLocation[0][i])+1][(agentLocation[1][i])]) == HOMER:
                exit (CAPTURED)
            else:
                aMaze[(agentLocation[0][i])][(agentLocation[1][i])] = EMPTY
                aMaze[(agentLocation[0][i])+1][(agentLocation[1][i])] = EPA_AGENT
                agentLocation[0][i] += 1
        elif EPApos == 3:
            if (aMaze[(agentLocation[0][i])+1][(agentLocation[1][i])+1]) in (SPRINGFIELD, WATER, EPA_AGENT, BUILDING):
                pass
            elif (aMaze[(agentLocation[0][i])+1][(agentLocation[1][i])+1]) == HOMER:
                exit (CAPTURED)
            else:
                aMaze[(agentLocation[0][i])][(agentLocation[1][i])] = EMPTY
                aMaze[(agentLocation[0][i])+1][(agentLocation[1][i])+1] = EPA_AGENT
                agentLocation[0][i] += 1
                agentLocation[1][i] += 1
        elif EPApos == 4:
            if (aMaze[(agentLocation[0][i])][(agentLocation[1][i])-1]) in (SPRINGFIELD, WATER, EPA_AGENT, BUILDING):
                pass
            elif (aMaze[(agentLocation[0][i])][(agentLocation[1][i])-1]) == HOMER:
                exit (CAPTURED)
            else:
                aMaze[(agentLocation[0][i])][(agentLocation[1][i])] = EMPTY
                aMaze[(agentLocation[0][i])][(agentLocation[1][i])-1] = EPA_AGENT
                agentLocation[1][i] -= 1
        elif EPApos == 5:
            pass
        elif EPApos == 6:
            if (aMaze[(agentLocation[0][i])][(agentLocation[1][i])+1]) in (SPRINGFIELD, WATER, EPA_AGENT, BUILDING):
                pass
            elif (aMaze[(agentLocation[0][i])][(agentLocation[1][i])+1]) == HOMER:
                exit (CAPTURED)
            else:
                aMaze[(agentLocation[0][i])][(agentLocation[1][i])] = EMPTY
                aMaze[(agentLocation[0][i])][(agentLocation[1][i])+1] = EPA_AGENT
                agentLocation[1][i] += 1
        elif EPApos == 7:
            if (aMaze[(agentLocation[0][i])-1][(agentLocation[1][i])-1]) in (SPRINGFIELD, WATER, EPA_AGENT, BUILDING):
                pass
            elif (aMaze[(agentLocation[0][i])-1][(agentLocation[1][i])-1]) == HOMER:
                exit (CAPTURED)
            else:
                aMaze[(agentLocation[0][i])][(agentLocation[1][i])] = EMPTY
                aMaze[(agentLocation[0][i])-1][(agentLocation[1][i])-1] = EPA_AGENT
                agentLocation[1][i] -= 1
                agentLocation[0][i] -= 1
        elif EPApos == 8:
            if (aMaze[(agentLocation[0][i])-1][(agentLocation[1][i])]) in (SPRINGFIELD, WATER, EPA_AGENT, BUILDING):
                pass
            elif (aMaze[(agentLocation[0][i])-1][(agentLocation[1][i])]) == HOMER:
                exit (CAPTURED)
            else:
                aMaze[(agentLocation[0][i])][(agentLocation[1][i])] = EMPTY
                aMaze[(agentLocation[0][i])-1][(agentLocation[1][i])] = EPA_AGENT
                agentLocation[0][i] -= 1
        elif EPApos == 9:
            if (aMaze[(agentLocation[0][i])-1][(agentLocation[1][i])+1]) in (SPRINGFIELD, WATER, EPA_AGENT, BUILDING):
                pass
            elif (aMaze[(agentLocation[0][i])-1][(agentLocation[1][i])+1]) == HOMER:
                exit (CAPTURED)
            else:
                aMaze[(agentLocation[0][i])][(agentLocation[1][i])] = EMPTY
                aMaze[(agentLocation[0][i])-1][(agentLocation[1][i])+1] = EPA_AGENT
                agentLocation[0][i] -= 1
                agentLocation[1][i] += 1
        i = i + 1
    playerTurn(aMaze,agentLocation,articTime) 
    print()

#Checks whether or not the player can move in the direction specified.
#Take proper action and either move HOMER or stay put.
def homerMove(aMaze, articTime, pos):
    homerRow,homerColumn = HomerPos(aMaze)
    if (pos == 2):
       if (aMaze[homerRow+1][homerColumn]) == SPRINGFIELD: #WIN Condition
           exit(WIN)
       elif (aMaze[homerRow+1][homerColumn]) == WATER: #Lose Condition
           exit(DROWN)
       elif (aMaze[homerRow+1][homerColumn]) == EPA_AGENT: #Lose Condition
           exit(CAPTURED)
       elif (aMaze[homerRow+1][homerColumn]) == BUILDING: #Lose TURN Condition
	       print (BLOCKED)
           #Player lost their turn.
       else:		   
           aMaze[homerRow][homerColumn] = EMPTY
           aMaze[homerRow+1][homerColumn] = HOMER
           #Player made valid move, pass turn to computer.
    elif (pos == 4):
       if (aMaze[homerRow][homerColumn-1]) == SPRINGFIELD:
           exit(WIN)
       elif (aMaze[homerRow][homerColumn-1]) == WATER:
           exit(DROWN)
       elif (aMaze[homerRow][homerColumn-1]) == EPA_AGENT:
           exit(CAPTURED)
       elif (aMaze[homerRow][homerColumn-1]) == BUILDING:
	       print (BLOCKED)
           #Player lost their turn.
       else:		   
           aMaze[homerRow][homerColumn] = EMPTY
           aMaze[homerRow][homerColumn-1] = HOMER
           #Player made valid move, pass turn to computer.
    elif (pos == 6):
       if (aMaze[homerRow][homerColumn+1]) == SPRINGFIELD:
           exit(WIN)
       elif (aMaze[homerRow][homerColumn+1]) == WATER:
           exit(DROWN)
       elif (aMaze[homerRow][homerColumn+1]) == EPA_AGENT:
           exit(CAPTURED)
       elif (aMaze[homerRow][homerColumn+1]) == BUILDING:
	       print (BLOCKED)
           #Player lost their turn.
       else:		   
           aMaze[homerRow][homerColumn] = EMPTY
           aMaze[homerRow][homerColumn+1] = HOMER
           #Player made valid move, pass turn to computer.
    elif (pos == 8):
       if (aMaze[homerRow-1][homerColumn]) == SPRINGFIELD:
           exit(WIN)
       elif (aMaze[homerRow-1][homerColumn]) == WATER:
           exit(DROWN)
       elif (aMaze[homerRow-1][homerColumn]) == EPA_AGENT:
           exit(CAPTURED)
       elif (aMaze[homerRow-1][homerColumn]) == BUILDING:
	       print (BLOCKED)
           #Player lost their turn.
       else:		   
           aMaze[homerRow][homerColumn] = EMPTY
           aMaze[homerRow-1][homerColumn] = HOMER
           #Player made valid move, pass turn to computer.

def playerTurn(aMaze,agentLocation,articTime):
    displayWorld(aMaze,articTime) #Display world to user.
    i = 0 #Main Loop control
    while (i == 0):
        while True:
            try:
                distraction = random.randint(1,100)
                print ("\nMovement options, the numbers correspond to the 4 compass directions (5 to not move). Or enter 0 to quit the game.")
                print ("  8\n4 5 6\n  2")
                pos = int(input("Enter movement direction: "))
                break
            except (ValueError):
                displayWorld(aMaze,articTime)
                print ()
                print (SPACER)
                print("Homer does not know how to move that direction! Supply a valid integer.")
                print (SPACER)
        if pos in (1, 3, 7, 9): #Player tries to move Homer in NE, SE, SW, NW direction.
            print ("Homer does not know how to move that direction!")
        elif (pos < 0):
            global debug
            if (debug is False):
                debug = True
                print ("Debug Mode [On]/Off")
                i = i + 1
                debugHomer(distraction)
                articTime = articTime + 1
                computerTurn(aMaze,agentLocation,articTime) #Toggling Debug Mode Passes Turn
            elif (debug):
                debug = False
                print ("Debug Mode On/[Off]")
                i = i + 1
                articTime = articTime + 1
                computerTurn(aMaze,agentLocation,articTime)
        elif (pos == 0):
            exit(QUIT)
        elif (pos == 5):
            i = i + 1
            articTime = articTime + 1
            debugHomer(distraction)
            computerTurn(aMaze,agentLocation,articTime) #Pass turn to Computer/EPA
        elif (distraction > 25) and (distraction <= 100):
            if (pos == 2):
                i = i + 1
                articTime = articTime + 1
                debugHomer(distraction)
                homerMove(aMaze, articTime, pos) #Player move command is further extrapolated and move determined.
                computerTurn(aMaze,agentLocation,articTime) #Pass turn to Computer/EPA
                print ()
            elif (pos == 4):
                i = i + 1
                articTime = articTime + 1
                debugHomer(distraction)
                homerMove(aMaze, articTime, pos)
                computerTurn(aMaze,agentLocation,articTime)
                print ()
            elif (pos == 6):
                i = i + 1
                articTime = articTime + 1
                debugHomer(distraction)
                homerMove(aMaze, articTime, pos)
                computerTurn(aMaze,agentLocation,articTime)
                print()
            elif (pos == 8):
                i = i + 1
                articTime = articTime + 1
                debugHomer(distraction)
                homerMove(aMaze, articTime, pos)
                computerTurn(aMaze,agentLocation,articTime)
                print()
            elif (pos >= 10):
                debugHomer(distraction)
                displayWorld(aMaze,articTime)
                print("Please enter a valid movement direction") #User inputs a integer value larger than or equal to 10.
        elif(distraction >= 1) and (distraction <= 25):
            if (pos >= 10):
                debugHomer(distraction)
                displayWorld(aMaze,articTime)
                print ("Please enter a valid movement direction")
            else:
                print (DISTRACTED)
                articTime = articTime + 1
                i = i + 1
                debugHomer(distraction)
                computerTurn(aMaze,agentLocation,articTime)
        else:
            exit ("Unexpected Error with Random Generator") #This should never occur.

# Author: James Tam
# function: displayWorld
# displayWorld(2Dlist,int,int,int)
# returns(nothing)
# Shows the current state of the world (location of Homer, the EPA agents)
def displayWorld(aMaze, articTime):
    print()
    #Determine if homer is still in the first 6 rows (Alaska/Artic) and display Turns.
    for r in range (0, 6, 1):
        for c in range (0, 30, 1):
            if (HOMER in aMaze[r][c]):
                print ("Current turns spent in the artic:", articTime)
                print ("Turns remaining in the artic:", (10 - articTime))
                if (articTime >= 10):
                    exit (FREEZE) #Too many turns in Alaska/Artic have elapsed Homer Freezes.
	#Display World
    for r in range (0, ROWS, 1):
         for c in range (0, COLUMNS, 1):
              print(aMaze[r][c], end="")
         print()

#Find Homer Simpsons Coordinates and record them.
def HomerPos(aMaze):
    for r in range (0, ROWS, 1):
        for c in range (0, COLUMNS, 1):
            if (aMaze[r][c] == HOMER):
                homerRow = r
                homerColumn = c
                return(homerRow,homerColumn)
               
def initializeHC():
    aMaze = []
    agentLocation = []
   
    #Asking for file input from user and input to list.
    while True:
        try:
            getFile = input("Please enter in the location of the game file: ")
            gameFile = open(getFile, "r")
            break
        except (FileNotFoundError):
            print ("File was not found. Try again.")
    for line in gameFile:
        aMaze.append([char for char in line.strip()])
    gameFile.close()
   
    #Initialize Agent List
    for r in range (0, 2, 1):
         agentLocation.append ([])
         for c in range (0, AGENTS, 1):
              agentLocation[r].append (0)
    agentid = 0
    for r in range (0, ROWS, 1):
        for c in range (0, COLUMNS, 1):
            if (aMaze[r][c] == EPA_AGENT): #Get Agent Locations and record them in 2D List
                agentLocation [0][agentid] = r
                agentLocation [1][agentid] = c
                agentid = agentid + 1
    return(aMaze,agentLocation)

def start():
    aMaze = []
    agentLocation = []
    articTime = 0
   
    print ("""
    
    Introduction: The goal of the game is to bring Homer (H) from Alaska/Artic (top 6 rows of the grid) 
    back to the town of Springfield (S).
    However if Homer takes too long to travel out of Alaska he will freeze and you will lose the game. 
    Also if Homer moves into the water (~) he drowns and the game is lost. 
    
    Finally the tireless agents of the EPA (E) will try to capture Homer and if that occurs the game is lost. 
    You will be playing against the computer who will control the EPA, the game is on a turn-to-turn bases.
    A turn elapses when: Homer moves or you (the player) try to move him 
    (Homer ignores the command or the player tries to move Homer onto a building), 
    Homer stays on the same square (direction 5), or the player toggles the debugging mode on or off.. 
    
    Good Luck!
    
    """)

    aMaze,agentLocation = initializeHC()
    playerTurn(aMaze,agentLocation, articTime) #Give first turn to player.
start()
