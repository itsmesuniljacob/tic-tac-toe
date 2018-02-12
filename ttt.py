from IPython.display import clear_output
def drawBoard(board):
    #global s
    #s=board
    #clear_output()
    print(' ' + board[1] + ' | ' + board[2] +' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    #return s

def welcomeScreen():
    print('Welcome to TIC TAC TOE game')

board = [' '] * 10
#welcomeScreen()

def playerInput():
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        letter = input('Player 1, select your symbol "X" or "O" ').upper()
    
    if letter == 'X':
        return('X','O')
    else:
        return('O','X')
def boardWhenPlay(number,symbol,board):
#     for i in range(10):
#         if(board[i] != ' '):
#             print('Game is over')
    if(board[number] == ' '):
        board[number]=symbol
        if checkForWinPattern(symbol,board):
            print('Player has won the game')
        else:   
            print('Moving on...')
    else:
        print("Move not possible")
        #selectPosition()

def checkForWinPattern(mark,board):
    print('mark -->' +  mark)
    print(board[7] + ' ' + board[8] + ' ' + board[9])
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def nextPlayer(turn):
    global t
    if(turn == 'P1'):
        print('Player 2 turn')
        t='P2'
        print('---> ' + turn)
        return turn
    else:
        print('Player 1 turn')
        t = 'P1'
        print('---> ' + turn)
        return turn
def selectPosition():
    number = input("Enter your position: ")
    n = int(number)
    sym = input("Enter your symbol: ").upper()
    playerTurn(n,sym,board)

def playerTurn(player):
    global t
    if player == 'p1':
        print('P1 turn')
        position = int(input('Enter position you want to play: '))
        pos = int(position)
        sym = input('Enter your assigned symbol: ').upper()
        boardWhenPlay(pos,sym,board)
        t = 'p2'
        return t
    else:
        print('P2 turn')
        pos = int(input('Enter position you want to play: '))
        sym = input('Enter your assigned symbol: ').upper()
        boardWhenPlay(pos,sym,board)
        t = 'p1'
        return t

 def check_free_space(board, position):
    
    return board[position] == ' '    

def rotate_turn():
    t = whoPlaysFirst()
    print(t)
    gamePlaying = True
    while gamePlaying:
        for i in range(1,10):
            if i == 9:
                print('in Break',i)
                gamePlaying = False
            else:
                print(i)
                t = playerTurn(t)
                #print('In rotate Turn: ' +t)
                #playerTurn(t)         
        clear()
 
import random
def whoPlaysFirst():

    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def full_board_check(board):
    for i in range(1,10):
        if check_free_space(board, i):
            return False
    return True

def main():
    welcomeScreen()
    while True:
        board = [' '] * 10
        print()
        pl_sym,p2_sym = playerInput()
        turn = whoPlaysFirst()
        print(turn + ' will go first')
        gamePlaying = True
        while gamePlaying:
            if turn == 'Player 1':
                drawBoard(board)
                #position = getPosition(board)
                position = getPosition()
                boardWhenPlay(position,pl_sym,board)
                if checkForWinPattern(pl_sym,board):
                    drawBoard(board)
                    print()
                    print('Player 1 has won the game')
                    gamePlaying = False
                else:
                    if full_board_check(board):
                        drawBoard(board)
                        print()
                        print('The game is draw')
                        break
                    else:    
                        turn = 'Player 2'
            else:
                print()
                drawBoard(board)
                print()
                position = getPosition()
                boardWhenPlay(position,p2_sym,board)
                
                if checkForWinPattern(p2_sym,board):
                    drawBoard(board)
                    print('Player 2 has won the game')
                    gamePlaying = False
                else:
                    if full_board_check(board):
                        drawBoard(board)
                        print()
                        print('The game is draw')
                        break
                    else:    
                        turn = 'Player 1'
        break            
#         print()
#         rotate_turn()

def getPosition():
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split():
        position = input('Choose your next position: (1-9) ')
    return int(position)

main()
