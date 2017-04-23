import random
board = [" "," "," "," "," "," "," "," "," "]

def drawX():
    print(" X       X ")
    print("  X     X  ")
    print("   X   X   ")
    print("    X X    ")
    print("     X     ")
    print("    X X    ")
    print("   X   X   ")
    print("  X     X  ")
    print(" X       X ")
    print("       O   ")
    print("       OO  ")
    print("       O O ")
    print("O      O  O")
    print("OO        O")
    print("O O       O")
    print(" O       O ")
    print("  O     O  ")
    print("   OOOOO   ")
    exit
def drawO():
    print("   OOOOO   ")
    print("  O     O  ")
    print(" O       O ")
    print("O         O")
    print("O         O")
    print("O         O")
    print(" O       O ")
    print("  O     O  ")
    print("   OOOOO   ")
    print(" X             ")
    print("  X          X  ")
    print("   X     X    X")
    print("    X   X    ")
    print("     X     ")
    print("    X      ")
    print("   X        ")
    print("  X         ")
    print(" X       X X X X ")
    exit
def drawBoard(board):
    print("   0   1   2")
    print(" 0 {} | {} | {} ".format(board[0], board[1], board[2]))
    print(" ------------")
    print(" 1 {} | {} | {} ".format(board[3], board[4], board[5]))
    print(" ------------")
    print(" 2 {} | {} | {} ".format(board[6], board[7], board[8]))

def checkWin3(i1, i2, i3):
    if board[i1] == "O" and board[i3] == "O":
        return i2
    elif board[i2] == "O" and board[i3] == "O":
        return i1
    elif board[i1] == "O" and board[i2] == "O":
        return i3
    return True
def checkWin():
    if checkWin3(0, 1, 2) != True:
        return checkWin3(0, 1, 2)
    elif checkWin3(3, 4, 5) != True:
        return checkWin3(3, 4, 5)
    elif checkWin3(6, 7, 8) != True:
        return checkWin3(6, 7, 8)
    elif checkWin3(0, 3, 6) != True:
        return checkWin3(0, 3, 6)
    elif checkWin3(1, 4, 7) != True :
        return checkWin3(1, 4, 7)
    elif checkWin3(2, 5, 8) != True:
        return checkWin3(2, 5, 8)
    elif checkWin3(0, 4, 8) != True:
        return checkWin3(0, 4, 8)
    elif checkWin3(2, 4, 6) != True:
        return checkWin3(2, 4, 6)
    return False

def checkBlock3(i1, i2, i3):
    if board[i1] == "X" and board[i3] == "X":
        return i2
    elif board[i2] == "X" and board[i3] == "X":
        return i1
    elif board[i1] == "X" and board[i2] == "X":
        return i3
    return True
    
def checkBlock():
    if checkBlock3(0, 1, 2) != True:
        return checkBlock3(0, 1, 2)
    elif checkBlock3(3, 4, 5) != True:
        return checkBlock3(3, 4, 5)
    elif checkBlock3(6, 7, 8) != True:
        return checkBlock3(6, 7, 8)
    elif checkBlock3(0, 3, 6) != True:
        return checkBlock3(0, 3, 6)
    elif checkBlock3(1, 4, 7) != True :
        return checkBlock3(1, 4, 7)
    elif checkBlock3(2, 5, 8) != True:
        return checkBlock3(2, 5, 8)
    elif checkBlock3(0, 4, 8) != True:
        return checkBlock3(0, 4, 8)
    elif checkBlock3(2, 4, 6) != True:
        return checkBlock3(2, 4, 6)
    return False
def check3(i1, i2, i3, Player):
    if board[i1] == Player and board[i2] == Player and board[i3] == Player:
        return True
def check(player):
    if check3(0, 1, 2, player) == True:
        return True
    elif check3(3, 4, 5, player) == True:
        return True
    elif check3(6, 7, 8, player) == True:
        return True
    elif check3(0, 3, 6, player) == True:
        return True
    elif check3(1, 4, 7, player) == True:
        return True
    elif check3(2, 5, 8, player) == True:
        return True
    elif check3(0, 4, 8, player) == True:
        return True
    elif check3(2, 4, 6, player) == True:
        return True
drawBoard(board)

def Move(playerR):
    print("Player {} it is your turn".format(playerR))
    if playerR == "X":
        Y = int(input("Y: "))
        X = int(input("X: "))
        SquareNum = (3 * Y) + X
    else:   
        if checkWin() != False:
            SquareNum = checkWin()
            if board[SquareNum] == "X":
                if checkBlock() != False:
                    SquareNum = checkBlock()
            if board[SquareNum] == "X":
                SquareNum = random.randint(0, 8)
            if board[SquareNum] == "X":
                SquareNum = random.randint(0, 8)
            if board[SquareNum] == "X":
                Move(playerR)
        elif checkBlock() != False:
            SquareNum = checkBlock()
            if board[SquareNum] == "X":
                SquareNum = random.randint(0, 8)
            if board[SquareNum] == "X":
                SquareNum = random.randint(0, 8)
            if board[SquareNum] == "X":
                Move(playerR)
        else:
            SquareNum = random.randint(0, 8)
            if board[SquareNum] == "X":
                Move(playerR)
            
    if board[SquareNum] == "O":
        if playerR == "X":
            print("that spot is taken")
        Move(playerR)
    board[SquareNum] = playerR
    drawBoard(board)
    if check(playerR) == True:
        print("player {}, you won".format(playerR))
        if playerR == "X":
            drawX()
        else:
            drawO()
    
    elif playerR == "X":
        Move("O")
    else:
        Move("X")
Move("X")

    
