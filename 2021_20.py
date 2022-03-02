f = open("sample.txt","r")
data = ""
for line in f:
    data+=line
f.close()
data = data.split()
algo = data[0]
matrix = []
for i in range(1,len(data),1):
    matrix.append(data[i])

"""for i in range(1,len(matrix),2):
    for j in range()"""
