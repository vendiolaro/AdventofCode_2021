f = open("2021_9.txt", "r")
data = []
for x in f:
    data.append(x)
f.close()

ansList = []
for i in range(1):
    if i == 0:
        for j in range(len(data[i])-1):
            if j == 0:
                if data[i][j] < data[i+1][j] and data[i][j] < data[i][j+1]:
                    ansList.append(data[i][j])

            elif j == len(data[i])-2:
                if data[i][j] < data[i + 1][j] and data[i][j] < data[i][j - 1]:
                    ansList.append(data[i][j])
            else:
                if data[i][j] < data[i + 1][j] and data[i][j] < data[i][j - 1] and data[i][j] < data[i][j+1]:
                    ansList.append(data[i][j])
                    #print(j)


    elif i == (len(data)-1):
        for j in range(len(data[i])-1):
            if j == 0:
                if data[i][j] < data[i-1][j] and data[i][j] < data[i][j+1]:
                    ansList.append(data[i][j])

            elif j == len(data[i])-2:
                if data[i][j] < data[i - 1][j] and data[i][j] < data[i][j - 1]:
                    ansList.append(data[i][j])

            else:
                if data[i][j] < data[i][j - 1] and data[i][j] < data[i][j+1] and data[i][j] < data[i - 1][j]:
                    ansList.append(data[i][j])

    else:
        for j in range(len(data[i])-1):
            if j == 0:
                if data[i][j] < data[i-1][j] and data[i][j] < data[i][j+1] and data[i][j] < data[i+1][j]:
                    ansList.append(data[i][j])

            elif j == len(data[i])-2:
                if data[i][j] < data[i - 1][j] and data[i][j] < data[i][j-1] and data[i][j] < data[i+1][j]:
                    ansList.append(data[i][j])


            else:
                if data[i][j] < data[i][j - 1] and data[i][j] < data[i][j+1] and data[i][j] < data[i - 1][j] and data[i][j] < data[i + 1][j]:
                    ansList.append(data[i][j])



ans = 0
n = 0
for num in ansList:
    n = int(num)+1
    ans += n

print(ans)

heightmap = data.copy()

heightmap = [[0 if num !="9" else 9 for num in line.strip() ] for line in heightmap ]
width = len(heightmap[0])
height = len(heightmap)

def floodfill(matrix, x, y):
    score = 0
    if matrix[y][x] == 0:
        matrix[y][x] = 1
        score = 1
        if x > 0:
            score += floodfill(matrix,x-1,y)
        if x < len(matrix[0]) - 1:
            score += floodfill(matrix,x+1,y)
        if y > 0:
            score += floodfill(matrix,x,y-1)
        if y < len(matrix) - 1:
            score += floodfill(matrix,x,y+1)
    return score

scores = []
for idx in range(width):
    for jdx in range(height):
        scores.append(floodfill(heightmap, idx, jdx))

scores = sorted(scores, reverse=True)[:3]

print(f"Total: {scores[0] * scores[1] * scores[2]}")


