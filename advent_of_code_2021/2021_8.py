f = open("2021_8.txt","r")
data = []
for x in f:
    data.append(x)
f.close()
dataIn = []
temp = []
counter = 0
ans = ""
temp1 = []
val = 0
num = 0
x = {}
y = {}
z = {}
a = []
b ={}
c = {}
d = {}
e = {}
charSet = {}
ansList = [' ']*7
for i in range(len(data)):
    dataIn = data[i].split('|')
    temp = dataIn[1].split()
    temp1 = dataIn[0].split()
    for j in temp:
        if len(j) == 3 or len(j) == 2 or len(j) == 4 or len(j) == 7:
            counter+=1
    for k in temp1:
        if len(k) == 3:
            y = set(k)
        elif len(k) == 2:
            x = set(k)
        elif len(k) == 4:
            z = set(k)
        elif len(k) == 5:
            a.append(k)
        elif len(k) == 7:
            e = set(k)
    charSet = y.difference(x)
    charSet = list(charSet)
    ansList[0] = charSet[0]
    charSet = set(charSet)
    charSet = z.difference(y)
    charSet = list(charSet)
    x = list(x)
    ansList[1] = x[0]
    ansList[2] = x[1]
    ansList[5] = charSet[0]
    ansList[6] = charSet[1]
    x = set(x)
    charSet = {}
    charSet = z.union(y)

    for string in a:
        if string.count(ansList[5]) == 1 and string.count(ansList[6]) == 1: #this represents 5
            b = set(string)
            #print(b)
        elif string.count(ansList[1]) == 1 and string.count(ansList[2]) == 1: #this represents 3
            c = set(string)
            #print(c)
        else:
            d = set(string)
    a.clear()
    charSet = b.difference(z.union(y))
    charSet = list(charSet)
    ansList[3] = charSet[0]
    charSet = {}
    charSet = b.difference(c)
    charSet = list(charSet)
    ansList[5] = charSet[0]
    charSet = {}
    charSet = c.difference(b)
    charSet = list(charSet)
    ansList[1] = charSet[0]
    charSet = {}
    charSet = d.difference(b.union(c))
    charSet = list(charSet)
    ansList[4] = charSet[0]
    charSet = {}
    charSet = c.difference(d)
    charSet = list(charSet)
    ansList[2] = charSet[0]
    charSet = {}
    charSet = list(y)
    charSet.append(ansList[5])
    charSet.append(ansList[4])
    charSet.append(ansList[3])
    charSet = set(charSet)
    charSet = e.difference(charSet)
    charSet = list(charSet)
    ansList[6] = charSet[0]
    charSet = {}

    for blurb in temp:
        if len(blurb) == 2:
            ans += '1'
        elif len(blurb) == 3:
            ans += '7'
        elif len(blurb) == 4:
            ans += '4'
        elif len(blurb) == 7:
            ans += '8'
        elif len(blurb) == 6 and blurb.count(ansList[6]) == 0:
            ans += '0'
        elif len(blurb) == 6 and blurb.count(ansList[1]) == 0:
            ans += '6'
        elif len(blurb) == 6 and blurb.count(ansList[4]) == 0:
            ans += '9'
        elif len(blurb) == 5 and blurb.count(ansList[1]) == 0 and blurb.count(ansList[4]) == 0:
            ans += '5'
        elif len(blurb) == 5 and blurb.count(ansList[5]) == 0 and blurb.count(ansList[2]) == 0:
            ans += '2'
        elif len(blurb) == 5 and blurb.count(ansList[5]) == 0 and blurb.count(ansList[4]) == 0:
            ans += '3'

    val = int(ans)
    ans = ""
    num += val

print("The number of 1,4,7,8 in input is {}".format(counter))
print("The sum of decoded 4 digit num is {}".format(num))