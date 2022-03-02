f = open("2020_2.txt", "r")
data = ""
for x in f:
    data+=x
f.close()

dataIn = []
dataIn = data.split('\n')

txt = dataIn[0].partition(' ')
#print(txt)
txt1 = txt[0].split('-')
#print(txt1)


min = 0
max = 0
counter = 0
char = ""
string = ""
temp = ""
temp1 = ""
pos1 = 0
pos2 = 0
counter1 = 0

for i in range(len(dataIn)):
    temp = dataIn[i].partition(' ')
    temp1 = temp[0].partition('-')
    min = int(temp1[0])
    max = int(temp1[2])
    temp1 = temp[2].partition(': ')
    char = temp1[0]
    string = temp1[2]
    pos1 = min
    pos2 = max
    if string.count(char) >= min and string.count(char) <= max:
        counter+=1
    if string[pos1-1] == char and string[pos2-1] != char:
        counter1+=1
    elif string[pos1-1] != char and string[pos2-1] == char:
        counter1+=1


print("Count of valid passwords with number of chars within range is: {}".format(counter))
print("Count of valid passwords with one of two correct position is {}.".format(counter1))



