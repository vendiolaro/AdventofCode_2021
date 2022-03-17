f = open("2021_11.txt","r")
data = []
for line in f:
    data.append(line)
f.close()
dataIn = []

for i in range(len(data)):
    data[i] = data[i].strip()

for line in data:
    dataIn.append(list(line))

for i in range(len(dataIn)):
    for k in range(len(dataIn[0])):
        dataIn[i][k] = int(dataIn[i][k])

data = dataIn.copy()

for line in dataIn:
    print(line)
print()
part2 = dataIn.copy()

def flash(data,x,y):
    '''up = data[y-1][x]
    down = data[y+1][x]
    right = data[y][x+1]
    left = data[y][x-1]
    upright = data[y-1][x+1]
    upleft = data[y-1][x-1]
    downright = data[y+1][x+1]
    downleft =data[y+1][x-1]'''
    if y == 0 and x == 0: #up left corner
        data[y][x + 1] += 1 #right
        data[y + 1][x] += 1 #down
        data[y + 1][x + 1] += 1 #downright


    elif y == 0 and x == len(data[0])-1: #up right corner
        data[y][x - 1] += 1 #left
        data[y + 1][x] += 1 #down
        data[y + 1][x - 1] += 1 #downleft


    elif y == len(data)-1 and x == 0: #low left corner
        data[y - 1][x] += 1 #up
        data[y][x + 1] += 1 #right
        data[y - 1][x + 1] += 1 #upright


    elif y == len(data)-1 and x == len(data[0])-1: #low right corner
        data[y - 1][x] += 1  # up
        data[y][x - 1] += 1  # left
        data[y - 1][x - 1] += 1 #upleft


    elif y-1 == -1: #upper border
        #print("upper border ran with {} {}".format(y, x))
        data[y][x - 1] += 1  # left
        data[y][x + 1] += 1  # right
        data[y + 1][x] += 1  # down
        data[y + 1][x + 1] += 1  # downright
        data[y + 1][x - 1] += 1  # downleft


    elif y+1 == len(data): #low border
        #print("low border ran with {} {}".format(y, x))
        data[y - 1][x] += 1  # up
        data[y][x - 1] += 1  # left
        data[y][x + 1] += 1  # right
        data[y - 1][x + 1] += 1  # upright
        data[y - 1][x - 1] += 1  # upleft


    elif x-1 == -1: #left border
        #print("left border ran with {} {}".format(y, x))
        data[y][x + 1] += 1  # right
        data[y - 1][x] += 1  # up
        data[y - 1][x + 1] += 1  # upright
        data[y + 1][x] += 1  # down
        data[y + 1][x + 1] += 1  # downright


    elif x+1 == len(data[0]): #right border
        #print("right border ran with {} {}".format(y, x))
        data[y][x - 1] += 1  # left
        data[y - 1][x] += 1  # up
        data[y - 1][x - 1] += 1  # upleft
        data[y + 1][x] += 1  # down
        data[y + 1][x - 1] += 1  # downleft


    else:
        #print("else ran with {} {}".format(y,x))
        data[y][x - 1] += 1  # left
        data[y - 1][x] += 1  # up
        data[y - 1][x - 1] += 1  # upleft
        data[y + 1][x] += 1  # down
        data[y + 1][x - 1] += 1  # downleft
        data[y][x + 1] += 1  # right
        data[y + 1][x + 1] += 1  # downright
        data[y - 1][x + 1] += 1  # upright

    data[y][x] = 1000
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] >= 10 and data[y][x] < 1000:
                flash(data,x,y)

def checkBoard(data):
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] != 0:
                return False
    return True

flashNum = 0

for step in range(100):
    for y in range(len(data)):
        for x in range(len(data[0])):
            data[y][x] += 1
            if data[y][x] == 10:
                flash(data,x,y)
                #data[y][x] = 1000
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] >= 1000:
                data[y][x] = 0
                flashNum += 1

for line in data:
    print(line)
print()
print("Number of flashes is {} after 100 steps.".format(flashNum))
print()
print()


############################ PART TWO ############################

stepBool = True
step = 0
while(stepBool):

    for y in range(len(part2)):
        for x in range(len(part2[0])):
            part2[y][x] += 1
            if part2[y][x] == 10:
                flash(part2,x,y)
                #data[y][x] = 1000
    for y in range(len(part2)):
        for x in range(len(part2[0])):
            if part2[y][x] >= 1000:
                part2[y][x] = 0

    step += 1

    if checkBoard(part2) == True:
        step = step + 100
        print("First step where all flashed: {}.".format(step))
        '''for line in part2:
            print(line)'''
        break