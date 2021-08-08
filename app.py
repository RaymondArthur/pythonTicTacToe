# def valueFixedInstrument(ttm,fv,couponRate,y):
#     pv = 0
#     for i in range(1,ttm+1):
#         if(i == ttm):
#             pv += (fv*couponRate + fv) / ((1+y)**i)
#         else:
#             pv += (fv*couponRate) / ((1+y)**i)

#     return round(pv,6)

# print(valueFixedInstrument(10,10000000,.1,.09))

def printBoard():
    print('\n'*100)
    print('-' + ' ' +'-' + ' ' +'-' + ' ' +'-' + ' ' +'-' + ' '+'\n', end ='')
    print(theBoard['top-L'] + ' | ' + theBoard['top-M'] + ' | ' + theBoard['top-R']+'\n',end ='')
    print('-' + ' ' +'-' + ' ' +'-' + ' ' +'-' + ' ' +'-' + ' '+'\n',end ='')
    print(theBoard['mid-L'] + ' | ' + theBoard['mid-M'] + ' | ' + theBoard['mid-R']+'\n',end ='')
    print('-' + ' ' +'-' + ' ' +'-' + ' ' +'-' + ' ' +'-' + ' '+'\n',end ='')
    print(theBoard['low-L'] + ' | ' + theBoard['low-M'] + ' | ' + theBoard['low-R']+'\n',end ='')
    print('-' + ' ' +'-' + ' ' +'-' + ' ' +'-' + ' ' +'-' + ' '+'\n',end ='')
    

def updateBoard(playerInput, playerSelected):
    if(playerInput == str(7)):
        theBoard['top-L'] = 'X' if(playerSelected == 'Player 1') else 'O'
    elif(playerInput == str(8)):
        theBoard['top-M'] = 'X' if(playerSelected == 'Player 1') else 'O'
    elif(playerInput == str(9)):
        theBoard['top-R'] = 'X' if(playerSelected == 'Player 1') else 'O'
    elif(playerInput == str(4)):
        theBoard['mid-L'] = 'X' if(playerSelected == 'Player 1') else 'O'
    elif(playerInput == str(5)):
        theBoard['mid-M'] = 'X' if(playerSelected == 'Player 1') else 'O'
    elif(playerInput == str(6)):
        theBoard['mid-R'] = 'X' if(playerSelected == 'Player 1') else 'O'
    elif(playerInput == str(1)):
        theBoard['low-L'] = 'X' if(playerSelected == 'Player 1') else 'O'
    elif(playerInput == str(2)):
        theBoard['low-M'] = 'X' if(playerSelected == 'Player 1') else 'O'
    elif(playerInput == str(3)):
        theBoard['low-R'] = 'X' if(playerSelected == 'Player 1') else 'O' 

def checkForWinner(playerSelected):
    if(
        (
            #checking top row equality
            (list(theBoard.values())[0] == list(theBoard.values())[1])
            & (list(theBoard.values())[0] == list(theBoard.values())[2])
            & (list(theBoard.values())[0] != ' ')
        )
        |
        (
            #checking middle row equality
            (list(theBoard.values())[3] == list(theBoard.values())[4])
            & (list(theBoard.values())[3] == list(theBoard.values())[5])
            & (list(theBoard.values())[3] != ' ')
        )
        |
        (
            #checking bottom row equality
            (list(theBoard.values())[6] == list(theBoard.values())[7])
            & (list(theBoard.values())[6] == list(theBoard.values())[8])
            & (list(theBoard.values())[6] != ' ')
        )
        | 
        (
            #checking left column equality
            (list(theBoard.values())[0] == list(theBoard.values())[3])
            & (list(theBoard.values())[0] == list(theBoard.values())[6])
            & (list(theBoard.values())[0] != ' ')
        )
        |
        (
            #checking middle column equality
            (list(theBoard.values())[1] == list(theBoard.values())[4])
            & (list(theBoard.values())[1] == list(theBoard.values())[7])
            & (list(theBoard.values())[1] != ' ')
        )
        |
        (
            #checking right column equality
            (list(theBoard.values())[2] == list(theBoard.values())[5])
            & (list(theBoard.values())[2] == list(theBoard.values())[8])
            & (list(theBoard.values())[2] != ' ')
        )
        |
        (
            #checking top left to bottom right diagonal equality
            (list(theBoard.values())[0] == list(theBoard.values())[4])
            & (list(theBoard.values())[0] == list(theBoard.values())[8])
            & (list(theBoard.values())[0] != ' ')
        )
        |
        (
            #checking bottom left to top right diagonal equality
            (list(theBoard.values())[6] == list(theBoard.values())[4])
            & (list(theBoard.values())[6] == list(theBoard.values())[2])
            & (list(theBoard.values())[6] != ' ')
        )
        ) :
            
            printBoard()
            print(playerSelected + ' wins, well done!!!')
            playAgain = input('Would you like to play again? (y/n)')
            if(playAgain == 'y'):
                clearBoard()
                playerTurn()
            else:
                exit()

def checkForDraw():
    print(' ' in theBoard.values())
    if((' ' in theBoard.values()) == False):
        printBoard()
        print('The game is a draw!')
        playAgain = input('Would you like to play again? (y/n)')
        if(playAgain == 'y'):
            clearBoard()
            playerTurn()
        else:
            exit()


def playerTurn():
    gameStatus = 'Continue'
    player1 = True
    
    while(gameStatus != 'exit'):
     
        #print the board
        printBoard()

        #toggle the selected player automatically
        playerSelected = ('Player 1') if (player1 == True) else ('Player 2')

        #get desired cell from players
        playerInput = input(playerSelected + ': Toggle which cell? \n')

        if(playerInput == 'exit'):
            print('Thanks for playing, bye!')
            exit()
        elif((playerInput != 'exit') & (list(theBoard.values())[int(playerInput)-1] != ' ')):
            print('That cell already has a value, please pick another cell')
            continue   
        else:
            updateBoard(playerInput,playerSelected)
        
        checkForDraw()
        checkForWinner(playerSelected)
        gameStatus = playerInput
        player1 = not player1

def clearBoard():
    for i in theBoard: 
        theBoard[i] = ' '

def game():
    playerTurn()

#global variables

theBoard = {
    'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'top-L': ' ', 'top-M': ' ', 'top-R': ' '
}
p1='player1'
p2='player2'
game()
