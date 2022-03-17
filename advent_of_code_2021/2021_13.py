f = open("2021_12.txt", "r")
data =[]
for x in f:
    data.append(x)
f.close()

dataIn = []
for line in data:
    dataIn.append(line.split(','))


row = int(dataIn[0][1])
col = int(dataIn[0][0])

for i in range(len(dataIn)):
    if int(dataIn[i][0]) > col:
        col = int(dataIn[i][0])
    if int(dataIn[i][1]) > row:
        row = int(dataIn[i][1])

rows,cols = (row+1,col+1)
print(row)
print(col)

def verticalFold(matrix,index):
    col2 = len(matrix[0])
    for i in range(len(matrix)):
        matrix[i][index] = 'X'
    for i in range(len(matrix)):
        for j in range(0, index + 1, 1):
            if matrix[i][ (col2 - 1) - j] == '#':
                matrix[i][j] = '#'
            matrix[i].pop()
def horizontalFold(matrix,index):
    row2 = len(matrix)
    for i in range(len(matrix[0])):
        matrix[index][i] = 'X'
    for i in range(0,index+1,1):
        for j in range(len(matrix[0])):
            if matrix[(row2-1)-i][j] == '#':
                matrix[i][j] = '#'
        matrix.pop()
def count(matrix):
    counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '#':
                counter+=1
    return counter



matrix = [['.' for i in range(cols)] for j in range(rows)]
for i in range(len(dataIn)):
    col1 = int(dataIn[i][0])
    row1 = int(dataIn[i][1])
    matrix[row1][col1] = '#'
print(len(matrix[0]))
fold = 655
verticalFold(matrix,fold)
print(count(matrix))
horizontalFold(matrix,447)
verticalFold(matrix,327)
horizontalFold(matrix,223)
verticalFold(matrix,163)
horizontalFold(matrix,111)
verticalFold(matrix,81)
horizontalFold(matrix,55)
verticalFold(matrix,40)
horizontalFold(matrix,27)
horizontalFold(matrix,13)
horizontalFold(matrix,6)

for line in matrix:
    print(line)






