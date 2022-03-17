f = open("2021_12.txt","r")
data = []
for line in f:
    data.append(line.strip())
f.close()
dataIn = []
for line in data:
    dataIn.append(line.split('-'))
data = dataIn.copy()

startList = []
endList = []

for i in range(len(data)):
    if 'start' in data[i]:
        if data[i][1] == 'start':
            data[i][1] = data[i][0]
            data[i][0] = 'start'
        startList.append(i)
    elif 'end' in data[i]:
        if data[i][0] == 'end':
            data[i][0] = data[i][1]
            data[i][1] = 'end'
        endList.append(i)

print(data)
print(startList)
myStack = []
resList = []
def find_pair(data,str):
    for i in range(len(data)):
        if str == data[i][1]:
            return data[i][0]
        elif str == data[i][0]:
            return data[i][1]
        else:
            return 0
while len(startList) != 0:
    #resList.append(startList[len(startList)-1])
    #while len(myStack) != 0:






