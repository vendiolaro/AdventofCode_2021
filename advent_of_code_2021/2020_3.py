f = open("2020_3.txt", "r")
data = []
for x in f:
    data.append(x)
f.close()

index = 0
numO = 0
numX = 0
string = []

for line in data:
    string.append(list(line))

for i in range(1,len(string),1):
        if index+3 < len(string[0])-1:
            index +=3
        else:
            index = 2
        if string[i][index] == ".":
            numO += 1
            string[i][index] = "O"
        elif string[i][index] == "#":
            numX += 1
            string[i][index] = "X"

print(numO)
print(numX)
for i in range(len(string)):
    print(string[i])







