f = open("2020_1.txt", "r")

data = ""
for x in f:
    data+=x
f.close()

dataIn = []
dataIn = data.split()
for i in range(len(dataIn)):
    dataIn[i] = int(dataIn[i])

diff = 0
diffar = []
for i in range(len(dataIn)):
    diff = 2020-(dataIn[i])
    diff = abs(diff)
    if diff in dataIn:
        print("Detected: {} * {} = {}".format(diff,dataIn[i],diff*dataIn[i]))
        break

temp = 0
num = 0
numList = []
ans = False
product = 0
for i in range(len(dataIn)):
    if ans == True:
        break
    for j in range(len(dataIn)):
        if ans == True:
            break
        num = dataIn[i] + dataIn[j]
        for k in range(len(dataIn)):
            if num+dataIn[k] == 2020:
                ans = True
                product = dataIn[i] * dataIn[j] * dataIn[k]
                print("Detected: {} * {} * {} = {}".format(dataIn[i], dataIn[j], dataIn[k], product))
                break

