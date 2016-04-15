import sys, os, random


def makeMove(move):
    if move > 9 or move < 1:
        print "Please choose a valid number"
        sys.exit()
    move = move - 1
    if board[move] is not " ":
        print "place already taken"
        sys.exit()
    board[move] = "X"
    pcRoll = random.randrange(0,8)
    while " " in board and board[pcRoll] is not " ":
        pcRoll =  random.randrange(0,8)

    board[pcRoll] = "O"
    print board[0] +  "|" + board[1] + "|" + board[2]
    print board[3] +  "|" + board[4] + "|" + board[5]
    print board[6] +  "|" + board[7] + "|" + board[8]

    checkWin(board)

def checkWin(b):
    if b[0] is  b[1] is b[2] is "X":
        print "You won!"
        sys.exit()
    if b[3] is  b[4] is b[5] is "X":
        print "You won!"
        sys.ext()
    if b[6] is  b[7] is b[8] is "X":
        print "You won!"
        sys.exit()
    if b[0] is  b[3] is b[6] is "X":
        print "You won!"
        sys.exit()
    if b[1] is  b[4] is b[7] is "X":
        print "You won!"
        sys.exit()
    if b[2] is  b[5] is b[8] is "X":
        print "You won!"
        sys.exit()
    if b[0] is  b[4] is b[8] is "X":
        print "You won!"
        sys.exit()
    if b[2] is  b[4] is b[6] is "X":
        print "You won!"
        sys.exit()
    if b[0] is  b[1] is b[2] is "O":
        print "You lost!"
        sys.exit()
    if b[3] is  b[4] is b[5] is "O":
        print "You lost!"
        sys.ext()
    if b[6] is  b[7] is b[8] is "O":
        print "You lost!"
        sys.exit()
    if b[0] is  b[3] is b[6] is "O":
        print "You lost!"
        sys.exit()
    if b[1] is  b[4] is b[7] is "O":
        print "You lost!"
        sys.exit()
    if b[2] is  b[5] is b[8] is "O":
        print "You lost!"
        sys.exit()
    if b[0] is  b[4] is b[8] is "O":
        print "You lost!"
        sys.exit()
    if b[2] is  b[4] is b[6] is "O":
        print "You lost!"
        sys.exit()
    if not " " in b:
        print "Its a tie!"
        sys.exit()








board = [" "," "," "," "," "," "," "," "," "]
userMove = ''
while userMove is not 'quit':
    userMove = int(raw_input("Move:"))
    makeMove(userMove)

