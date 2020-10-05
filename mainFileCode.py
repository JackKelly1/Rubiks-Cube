# Any function unique to Processing has a comment detailing its usage

add_library('peasycam')

import os
from Cubie import Cubie

dim = 3 #dimensions
cube = [[[0 for k in range(dim)] for j in range(dim)] for i in range(dim)]

# Create the list that will hold the scramble
scramble = []
# Create the list that will hold the solve obtained from theSolution.txt
solve = []


# Set the paths for the scramble and solve text files
scramblePath = os.path.join(r"C:\Users\jackk\OneDrive - University of Bristol\3rd Year", "theScramble.txt")
solvePath = os.path.join(r"C:\Users\jackk\OneDrive - University of Bristol\3rd Year", "theSolution.txt")



# Initial state of the cube
cubies = []
def initialCube(lenc):
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                x = lenc*(i-1)
                y = lenc*(j-1)
                z = lenc*(k-1)
                # colours = [red, orange, yellow, white, green, blue]
                colours = ['#FF0000','#FFA500','#FFFF00','#FFFFFF',
                '#00FF00','#0000FF']
                cubies.append(Cubie(x, y, z, lenc, colours)) # creates a list of the instances



# move functions
def rightTurn():
    
    temp_corner = cubies[18]
    
    cubies[18] = cubies[20]
    cubies[18].z -= 100
    
    cubies[20] = cubies[26]
    cubies[20].y -= 100
    
    cubies[26] = cubies[24]
    cubies[26].z += 100
    
    cubies[24] = temp_corner
    cubies[24].y += 100
    

    temp_edge = cubies[19]
    
    cubies[19] = cubies[23]
    cubies[19].z -= 50
    cubies[19].y -= 50
    
    cubies[23] = cubies[25]
    cubies[23].z += 50
    cubies[23].y -= 50
    
    cubies[25] = cubies[21]
    cubies[25].z += 50
    cubies[25].y += 50
    
    cubies[21] = temp_edge
    cubies[21].z -= 50
    cubies[21].y += 50
            
    for i in range(18, 27):
        if i != 22:
            # colours = [red, orange, yellow, white, green, blue]
            holder = cubies[i].colours[4]
            cubies[i].colours[4] = cubies[i].colours[2]
            cubies[i].colours[2] = cubies[i].colours[5]
            cubies[i].colours[5] = cubies[i].colours[3]
            cubies[i].colours[3] = holder



def backTurn():
    
    temp_corner = cubies[0]
    
    cubies[0] = cubies[18]
    cubies[0].x -= 100
    
    cubies[18] = cubies[24]
    cubies[18].y -= 100
    
    cubies[24] = cubies[6]
    cubies[24].x += 100
    
    cubies[6] = temp_corner
    cubies[6].y += 100


    temp_edge = cubies[3]
    
    cubies[3] = cubies[9]
    cubies[3].x -= 50
    cubies[3].y += 50
    
    cubies[9] = cubies[21]
    cubies[9].y -= 50
    cubies[9].x -= 50
    
    cubies[21] = cubies[15]
    cubies[21].y -= 50
    cubies[21].x += 50
    
    cubies[15] = temp_edge
    cubies[15].x += 50
    cubies[15].y += 50
    
    for i in range(0, 27, 3):
        if i != 12: # centre square
            # colours = [red, orange, yellow, white, green, blue]
            holder = cubies[i].colours[2]
            cubies[i].colours[2] = cubies[i].colours[1]
            cubies[i].colours[1] = cubies[i].colours[3]
            cubies[i].colours[3] = cubies[i].colours[0]
            cubies[i].colours[0] = holder
    


def leftTurn():
    
    temp_corner = cubies[2]
    
    cubies[2] = cubies[0]
    cubies[2].z += 100
    
    cubies[0] = cubies[6]
    cubies[0].y -= 100
    
    cubies[6] = cubies[8]
    cubies[6].z -= 100
    
    cubies[8] = temp_corner
    cubies[8].y += 100
    
    
    temp_edge = cubies[5]
    
    cubies[5] = cubies[1]
    cubies[5].z += 50
    cubies[5].y += 50
    
    cubies[1] = cubies[3]
    cubies[1].z += 50
    cubies[1].y -= 50
    
    cubies[3] = cubies[7]
    cubies[3].y -= 50
    cubies[3].z -= 50
    
    cubies[7] = temp_edge
    cubies[7].y += 50
    cubies[7].z -= 50

    for i in range(0, 9):
        if i != 4: # centre square
            # colours = [red, orange, yellow, white, green, blue]
            holder = cubies[i].colours[5]
            cubies[i].colours[5] = cubies[i].colours[2]
            cubies[i].colours[2] = cubies[i].colours[4]
            cubies[i].colours[4] = cubies[i].colours[3]
            cubies[i].colours[3] = holder



def frontTurn():
    
    temp_corner = cubies[20]
    
    cubies[20] = cubies[2]
    cubies[20].x += 100
    
    cubies[2] = cubies[8]
    cubies[2].y -= 100
    
    cubies[8] = cubies[26]
    cubies[8].x -= 100
    
    cubies[26] = temp_corner
    cubies[26].y += 100
    
    
    temp_edge = cubies[11]
    
    cubies[11] = cubies[5]
    cubies[11].x += 50
    cubies[11].y -= 50
    
    cubies[5] = cubies[17]
    cubies[5].x -= 50
    cubies[5].y -= 50
    
    cubies[17] = cubies[23]
    cubies[17].x -= 50
    cubies[17].y += 50
    
    cubies[23] = temp_edge
    cubies[23].x += 50
    cubies[23].y += 50
    
    for i in range(2, 27, 3):
        if i != 14: # centre square
            # colours = [red, orange, yellow, white, green, blue]
            holder = cubies[i].colours[1]
            cubies[i].colours[1] = cubies[i].colours[2]
            cubies[i].colours[2] = cubies[i].colours[0]
            cubies[i].colours[0] = cubies[i].colours[3]
            cubies[i].colours[3] = holder



def upTurn():
    
    temp_corner = cubies[0]
    
    cubies[0] = cubies[2]
    cubies[0].z -= 100
    
    cubies[2] = cubies[20]
    cubies[2].x -= 100
        
    cubies[20] = cubies[18]
    cubies[20].z += 100
    
    cubies[18] = temp_corner
    cubies[18].x += 100
    
    
    temp_edge = cubies[19]
    
    cubies[19] = cubies[9]
    cubies[19].z += 50
    cubies[19].x += 50
    
    cubies[9] = cubies[1]
    cubies[9].z -= 50
    cubies[9].x += 50
    
    cubies[1] = cubies[11]
    cubies[1].x -= 50
    cubies[1].z -= 50

    cubies[11] = temp_edge
    cubies[11].x -= 50
    cubies[11].z += 50

    # need a list as no discernable pattern to the numbers
    upList = [0, 1, 2, 9, 11, 18, 19, 20]
    for i in upList:
            # colours = [red, orange, yellow, white, green, blue]
            holder = cubies[i].colours[5]
            cubies[i].colours[5] = cubies[i].colours[1]
            cubies[i].colours[1] = cubies[i].colours[4]
            cubies[i].colours[4] = cubies[i].colours[0]
            cubies[i].colours[0] = holder
            


def downTurn():
    
    temp_corner = cubies[8]
    
    cubies[8] = cubies[6]
    cubies[8].z += 100
    
    cubies[6] = cubies[24]
    cubies[6].x -= 100
    
    cubies[24] = cubies[26]
    cubies[24].z -= 100
    
    cubies[26] = temp_corner
    cubies[26].x += 100


    temp_edge = cubies[15]
    
    cubies[15] = cubies[25]
    cubies[15].z -= 50
    cubies[15].x -= 50
    
    cubies[25] = cubies[17]
    cubies[25].x += 50
    cubies[25].z -= 50
    
    cubies[17] = cubies[7]
    cubies[17].x += 50
    cubies[17].z += 50
    
    cubies[7] = temp_edge
    cubies[7].z += 50
    cubies[7].x -= 50

    downList = [6, 7, 8, 15, 16, 17, 24, 25, 26]
    for i in downList:
            # colours = [red, orange, yellow, white, green, blue]
            holder = cubies[i].colours[0]
            cubies[i].colours[0] = cubies[i].colours[4]
            cubies[i].colours[4] = cubies[i].colours[1]
            cubies[i].colours[1] = cubies[i].colours[5]
            cubies[i].colours[5] = holder


# function called whenever a key is pressed
def keyPressed():
    global scramble
    # checking the start button has been pressed
    if startClick == 1:
        if key == 'r':
            # add the move to the scramble list
            scramble.append("R")
        elif key == 'R':
            scramble.append("R'")
        elif key == 'l':
            scramble.append("L")
        elif key == 'L':
            scramble.append("L'")
        elif key == 'b':
            scramble.append("B")
        elif key =='B':
            scramble.append("B'")
        elif key == 'u':
            scramble.append("U")
        elif key == 'U':
            scramble.append("U'")
        elif key == 'f':
            scramble.append("F")
        elif key == 'F':
            scramble.append("F'")
        elif key == 'd':
            scramble.append("D")
        elif key == 'D':
            scramble.append("D'")
        else:
            return
        # turns prime moves into 3 quarter turns
        scramble = converter(scramble)
        # write to the .txt file
        writeScramble()
    


# function called whenever the mouse is clicked
startClick = 0
def mouseClicked():
    global startClick, cubies
    if startClick == 0:
        if (mouseX > width/2 - 50) and (mouseX < width/2 + 50):
            if (mouseY > height/2 - 50) and (mouseY < height/2 + 50):
                # make a new, larger cube
                cubies = []
                initialCube(50)
                # 1/6 - 1/10 as 1/10 is a good starting angle
                peasy.rotateX(-PI/15)
                # allow for zooming
                peasy.setWheelScale(1)
                peasy.setMinimumDistance(300)
                peasy.setMaximumDistance(600)
                startClick = 1
    else:
        # 360 is the width of 'Click to import ASCII file'
        if (mouseX > width/8) and (mouseX < width/8 + (360)):
            if (mouseY > (height/2 - 75) and mouseY < (height/2 - 50)):
                selectInput("Select a file to process:", "fileSelected")
            elif (mouseY > (height/2 + 25) and mouseY < (height/2 + 150)):
                randomGenerator()



# randomly generate 18 moves
def randomGenerator():
    global scramble
    moveList = ["U","U'","D","D'","L","L'","R","R'","F","F'","B","B'"]
    # 18 moves
    for i in range(18):
        n = int(random(len(moveList)))
        scramble.append(moveList[n])
    scramble = converter(scramble)
    # write the random moves to theScramble.txt file
    writeScramble()



# sets the data to 0, 0, 0 to avoid modifyCube() errors
def initialScrambleFile():
    data = ['0\n', '0\n', '0']
    # write the data back to the file
    with open(scramblePath, 'w') as file:
        file.writelines(data)        



def initialSolutionFile():
    data = ['0\n', '0\n', '0']
    # write the data to the file
    with open(solvePath, 'w') as file:
        file.writelines(data)
    
    

def writeScramble():
    with open(scramblePath, 'r') as file:
        data = file.readlines()
    data[0] = '' + str(scramble) + '\n'
    # no need to change data[1]
    data[2] = '' + str(len(scramble))
    with open(scramblePath, 'w') as file:
        file.writelines(data)
        


# function is run when a file is selected
def fileSelected(selection):
    global scramble
    if selection != None:
        holder = []
        print(selection)
        # splits the string after every /
        for i in selection.getAbsolutePath().split('/'):
            holder.append(str(i))
        # checks that the final item in the list ends in .txt
        if holder[-1].endswith('.txt'):
            with open(selection.getPath()) as f:
                a = [word for line in f for word in line.split()]
            # takes the first line of the .txt file, normally only one line
            a = str(a[0])
            # extend() iterates over its argument and adds each element to the list and extends the list
            scramble.extend(list(a))
            # used to create appropriate list for modifyCube(), removes numbers and primes
            scramble = converter(scramble)
            # write to the .txt file
            writeScramble()
        else:
            print('Please choose a text file (.txt)')
 
       

# used to replace primes and 2s with 3 or 2 'regular' moves respectively
def converter(arg):
    asciiCounter = 0
    for i in arg:
        if (i == "'") or (i=='2'):
            arg[asciiCounter-1] = arg[asciiCounter-1] + i
            arg.remove(i)
        asciiCounter += 1
    output = []
    for i in arg:
        if i.endswith("'"):
            for j in range(3):
                # change 1 prime rotation for 3 regular rotations
                output.append(i[:-1])
        elif i.endswith('2'):
            for j in range(2):
                output.append(i[:-1])
        else:
            output.append(i)
    return output



# converts list -> string for the HUD
def scrambleTextOutput():
    scrambleText = ' '.join(scramble)
    return scrambleText



# called by HUD()
scrambleCount = 0
solveCount = 0
change = 0
move = ''
totalTime = 0
firstTime1 = 0
def modifyCube():
    global scrambleCount, solveCount, change, solve, move, totalTime, firstTime1
    solveText = ''
    with open(scramblePath, 'r') as file:
        file.seek(0)
        data = file.readlines()
    if int(data[1]) > scrambleCount:
        move = scramble[scrambleCount]
        if move == "R":
            rightTurn()
        elif move == "L":
            leftTurn()
        elif move == "B":
            backTurn()
        elif move == "U":
            upTurn()
        elif move == "F":
            frontTurn()
        elif move == "D":
            downTurn()
        else:
            print('Not a valid scramble')
        scrambleCount += 1
    elif (len(scramble) == int(data[1])) and (int(data[1]) == int(data[2])) and (len(scramble) > 0):
        # 7 as a digit contributes 1 and a newline character contributes 2, therefore 3 + 3 + 1 = 7
        if os.stat(solvePath).st_size > 7:
            with open(solvePath, 'r') as file:
                file.seek(0)
                data = file.readlines()
            if change == 0:
                solveText = data[0]
                # remove the blank spaces as kociemba outputs spaced string e.g. "D2 R' D' F2 B D R2 D2 R'"
                solve = solveText.replace(' ', '')
                # turn kociemba string output into a list
                solve = list(solve)
                # remove primes and 2s
                solve = converter(solve)
                # pop() used to remove newline character
                solve.pop()
                # data = [0, 0, 0]
                data[0] = str(solve) + '\n'
                # data[1] already equa to '0\n'
                data[2] = str(len(solve))
                # write the solve length and solve length back to the text file
                with open(solvePath, 'w') as file:
                    file.writelines(data)
                change = 1
            else: 
                with open(solvePath, 'r') as file:
                    file.seek(0)
                    data = file.readlines()
                # print(data)
                if int(data[1]) > solveCount:
                    move = solve[int(solveCount)]
                    if move == "R":
                        rightTurn()
                    elif move == "L":
                        leftTurn()
                    elif move == "B":
                        backTurn()
                    elif move == "U":
                        upTurn()
                    elif move == "F":
                        frontTurn()
                    elif move == "D":
                        downTurn()
                    else:
                        print('Not a valid scramble')
                    solveCount += 1
                # to get the finish time
                elif (len(solve) == int(data[1])) and (len(solve) > 0) and (firstTime1 == 0):
                    totalTime = millis()
                    firstTime1 = 1
            solveText = ' '.join(solve)
    return solveText
                    


# used to display title, scrambleText, solveText and 'buttons'
firstTime = 0
startTime = 0
def HUD():
    global scramble, firstTime, startTime, solve
    scrambleText = scrambleTextOutput()
    solveText = modifyCube()
    
    # begin creating the HUD
    peasy.beginHUD()
    
    # set the title text size
    textSize(80)
    # set the text colour to black
    fill(0)
    title = "RUBIK'S CUBE SOLVER"
    textAlign(CENTER)
    text("RUBIK'S CUBE SOLVER", width/2, height/6)
    
    textSize(50)
    timing = text("TIME: ", (15*width/20), height/2 - 15)
    if change == 0:
        # show 0 as the solution has not yet been computed
        timing1 = text((str(0)), (15*width/20)+(width/12), height/2 - 15)
    else:
        # firstTime used to record the startTime
        if firstTime == 0:
            startTime = millis()
            firstTime = 1
        elif totalTime == 0:
            timing1 = text(str((millis()-startTime)/1000), (15*width/20)+(width/12), height/2 - 15)
        elif totalTime != 0:
            timing1 = text(str((totalTime - startTime)/1000), (15*width/20)+(width/12), height/2 - 15)

    textSize(30)
    textAlign(LEFT)
    scrambleTextWidth = textWidth(scrambleText)
    scrambleSignWidth = textWidth('Scramble: ')
    text("Scramble: " + scrambleText, (width/2) - (scrambleTextWidth + scrambleSignWidth)/2, height*17/20)
    solveTextWidth = textWidth(solveText)
    solveSignWidth = textWidth("Solve: ")
    text("Solve: " + solveText, (width/2) - (solveTextWidth + solveSignWidth)/2, height*18/20)
    
    textAlign(LEFT)
    textSize(40)
    # chcek if the scramble and solve lists are empty
    if not scramble and not solve:
        text("Current Move: ", 3*width/4 - 75, height/2 + 100)
    else:
        text("Current Move: " + str(move), 3*width/4 - 75, height/2 + 100)
    
    textSize(30)
    textAlign(LEFT)
    ascii = "Click to import ASCII file"
    text(ascii, width/11, height/2 - 50)
    
    textSize(30)
    randomText = "Click to generate a\nrandom sequence of\nmoves"
    text(randomText, width/11, height/2 + 50)
    
    # end creating the HUD
    peasy.endHUD()



def startScreenHUD():
    
    # begin creating the start screen HUD
    peasy.beginHUD()
    
    textSize(80)
    fill(0)
    textAlign(CENTER)
    text("RUBIK'S CUBE SOLVER", width/2, height/2 - 100)
    fill(255)
    # circle(x-coord, y-coord, radius)
    circle(width/2, height/2, 100)
    fill(0)
    # triangle(940, 510, 940, 570, 995, 540)
    textSize(30)
    text("Click the cube to begin", width/2, height/2 + 100)
    
    # end creating the start screen HUD
    peasy.endHUD()



# setup called once at the beginning
def setup():
    global peasy
    #P3D is a 3D renderer
    size(1500, 1000, P3D)
    fullScreen()
    #'this' sets the parent class and 400 is the zoom distance
    peasy = PeasyCam(this, 400)
    peasy.setRotations(0, PI/4, 0)
    peasy.rotateX(PI/6)
    peasy.setWheelScale(0)
    # Empty theScramble.txt and theSolution.txt files
    initialScrambleFile()
    initialSolutionFile()



# draw called 60 times a second (controlled by frameRate() which has a default value of 60)
def draw():
    # Set the background colour
    background(200)
    if startClick == 0:
        # Set the heads up display for the start screen
        startScreenHUD()
        initialCube(8)
    else:
        # Set the main heads up display
        HUD()
    # Make the cube visible
    for i in range(dim**3):
        cubies[i].show()
