f = open("2021_16.txt", "r")
data = ""
for line in f:
    data += line
f.close()
import math
def binaryToDecimal(n):
    return int(n,2)

# Code to convert hex to binary
res = "{0:08b}".format(int(data, 16))
res = str(res)
print(res)

def decode(string,i):
    binary = ""
    counter = 0
    for i in range(0,len(string),5):
        counter+=1
        if string[i] == '1':
            binary += string[i+1:i+5]
        elif string[i] == '0':
            binary += string[i + 1:i + 5]
            break
    return counter,binary


i = 0
while i < len(res):
    print(i)
    version = binaryToDecimal(res[i:i+3])
    i += 3
    ID = binaryToDecimal(res[i:i+3])
    i += 3
    if ID == 4:
        ansList = []
        ansList = decode(res[i:],i)
        ans = binaryToDecimal(ansList[1])
        i += ansList[0]*5
        continue
    elif ID != 4:
        type = binaryToDecimal(res[i])
        i += 1
        if type == 1:
            num = binaryToDecimal(res[i:i+11])
            i += 11
            print("subpack 1 {}".format(num))
            continue
        elif type == 0:
            num = binaryToDecimal(res[i:i+15])
            i += 15
            print("subpack 2 {}".format(num))
            continue






