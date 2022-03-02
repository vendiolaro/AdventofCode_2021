rows, cols = (10, 2)
board = [["" for i in range(cols)] for j in range(rows)]

di = 1
score1 = 0
score2 = 0
board[4][0] = "player1"
board[5][1] = "player2"
k = 0

def findIndex(player):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == player:
                return i
counter = 0
#while score1 < 1000 and score2 < 1000
while score1 < 1000 and score2 < 1000:
    di += 3
    move1 = di-3 + di-2 + di -1
    counter += 3
    current1 = findIndex("player1") + 1
    update1 = (move1 + current1) % 10
    board[current1-1][0] = ""
    board[update1-1][0] = "player1"
    if update1 == 0:
        score1 += 10
    else:
        score1 += update1
    if score1 >= 1000:
        break
    print("Player 1 rolls {} and moves to space {} for a total score of {}".format(move1,update1,score1))
    di += 3
    move2 = di-3 + di-2 + di -1
    counter += 3
    current2 = findIndex("player2") + 1
    update2 = (move2 + current2) % 10
    board[current2-1][1] = ""
    board[update2-1][1] = "player2"
    if update2 == 0:
        score2 += 10
    else:
        score2 += update2
    if score2 >= 1000:
        break
    print("Player 2 rolls {} and moves to space {} for a total score of {}".format(move2, update2, score2))


print("score1: {} score2: {} counter: {}".format(score1,score2,counter))
print(score1*counter)
print(board)




