
def getMove():
    player_choice = input("Where would you like to move? ")
    if player_choice == "Q":
        return 0
    if player_choice == "W":
        return 1
    if player_choice == "E":
        return 2
    if player_choice == "A":
        return 3
    if player_choice == "S":
        return 4
    if player_choice == "D":
        return 5
    if player_choice == "Z":
        return 6
    if player_choice == "X":
        return 7
    if player_choice == "C":
        return 8
    return -1

def makeMove(index,turn,board):
    if turn:
        board[index] = "O"
    else:
        board[index] = "X"
    

def printBoard(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def main():
    board = [" "," "," "," "," "," "," "," "," "]
    turn = False
    
    should_continue = True
    while should_continue:
        printBoard(board)
        move = getMove()
        if move == -1:
            should_continue = False
        else:
            if board[move] == " ":
                makeMove(move,turn,board)
                turn = not turn
    

if __name__ == "__main__":
    main()


