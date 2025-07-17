import pygame

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
row_size = SCREEN_HEIGHT//3
col_size = SCREEN_WIDTH//3

BACKGROUND_COLOR = [220,220,220]
BOARD_COLOR = [10,10,10]
X_COLOR = [240,10,10]
O_COLOR = [10,10,240]

key_Q = pygame.K_q
key_W = pygame.K_w
key_E = pygame.K_e
key_A = pygame.K_a
key_S = pygame.K_s
key_D = pygame.K_d
key_Z = pygame.K_z
key_X = pygame.K_x
key_C = pygame.K_c
key_Esc = pygame.K_ESCAPE
keys_to_board = {key_Q:0,key_W:1,key_E:2,key_A:3,key_S:4,key_D:5,key_Z:6,key_X:7,key_C:8}

def convertScreenPosToRowCol(pos):
    #TODO: convert from a position [x,y] on the screen
    # to a row number and column number
    row = 0  #fix this
    col = 0  #fix this
    return row,col  #leave this

def convertIndexToRowCol(index):
    #TODO: convert an index in the board state list
    # into a row number and column number
    row = 0  #fix this
    col = 0  #fix this
    return row,col  #leave this

def convertRowColToIndex(row,col):
    #TODO: convert a row number and column number
    # into an index in the board state list
    index = 0  #fix this
    return index  #leave this

def handleInput(index,turn,board):
    #TODO: based on the index the player decided to move in and whose turn it is,
    # modify board as needed
    # e.g.  board[index] = "X"    
    # return True if it's now player 1's turn, False otherwise
    pass

def handleMouse(pos,turn,board_state):
    row,col = convertScreenPosToRowCol(pos)
    index = convertRowColToIndex(row,col)
    return handleInput(index,turn,board_state)

def handleKey(key,turn,board_state):
    index = keys_to_board[key]
    return handleInput(index,turn,board_state)

def drawX(screen,row,col):
    #TODO: draw an X on the screen at the specified row and column
    pass

def drawO(screen,row,col):
    #TODO: draw an O on the screen at the specified row and column
    pass 

def drawMoves(screen,board_state):
    #TODO: draw the moves in the board state onto the screen
    # e.g. draw Xs and Os in the correct rows/columns
    pass

def drawBoard(screen):
    #TODO: draw 4 criss-crossing lines  
    # to make the boxes where the moves go
    pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    
    turn = True
    board_state = [" "," "," "," "," "," "," "," "," "]
    
    while running:
        # handle inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in keys_to_board:
                    player1_turn = handleKey(event.key,turn,board_state)
                if event.key == key_Esc:
                    #TODO: reset the game to a blank board and player1's turn
                    pass
            if event.type == pygame.MOUSEBUTTONUP:
                turn = handleMouse(event.pos,turn,board_state)
        
        #draw stuff
        screen.fill(BACKGROUND_COLOR)
        drawBoard(screen)
        drawMoves(screen,board_state)
        
        pygame.display.flip()
        
        #go to next frame
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()