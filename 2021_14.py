f = open("2021_14.txt","r")
data = []
for line in f:
    data.append(line.strip())
f.close()

dictionary = {}

for i in range(len(data)):
    res = data[i].split(" -> ")
    dictionary[res[0]] = res[1]

def polymer1(test):
    temp = ""
    ans = ""
    stringList = []
    for i in range(len(test)-1):
        temp = test[i:i+2]
        stringList = list(temp)
        if i < len(test)-2:
            stringList[1] = dictionary[temp]
        else:
            stringList.insert(1,dictionary[temp])
        ans += "".join(stringList)

    return ans


def polymer(test):
    test = list(test)
    testList = []
    toAppend = []
    ans = ""
    testString = ""
    for i in range(len(test)-1):
        testString = test[i] + test[i+1]
        testList.append(testString)
        testString = ""
    for i in range(len(testList)):
        toAppend.append(dictionary[testList[i]])
    for i in range(len(testList)):
        testList[i] = list(testList[i])
        testList[i].insert(1,toAppend[0])
        toAppend.pop(0)
        if i != len(testList)-1:
            testList[i].pop()
    for i in range(len(testList)):
        ans += "".join(testList[i])

    return ans

test = "CPSSSFCFOFVFNVPKBFVN"
test1 = "NNCB"

for i in range(40):
    test = polymer1(test)

#print(test)

check = []
valist = list(dictionary.values())
for char in valist:
    if char not in check:
        check.append(char)

score = {}

for char in check:
    score[char] = 0

for char in check:
    for ch in test:
        if char == ch:
            score[char] += 1

answer = max(score.values()) - min(score.values())
print(answer)
