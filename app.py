#prints the board to the console with some white space
def printBoard():
    print('\n'*100)
    print('-' + ' ' +'-' + ' ' +'-' + ' ' +'-' + ' ' +'-' + ' '+'\n', end ='')
    print(theBoard['top-L'] + ' | ' + theBoard['top-M'] + ' | ' + theBoard['top-R']+'\n',end ='')
    print('-' + ' ' +'-' + ' ' +'-' + ' ' +'-' + ' ' +'-' + ' '+'\n',end ='')
    print(theBoard['mid-L'] + ' | ' + theBoard['mid-M'] + ' | ' + theBoard['mid-R']+'\n',end ='')
    print('-' + ' ' +'-' + ' ' +'-' + ' ' +'-' + ' ' +'-' + ' '+'\n',end ='')
    print(theBoard['low-L'] + ' | ' + theBoard['low-M'] + ' | ' + theBoard['low-R']+'\n',end ='')
    print('-' + ' ' +'-' + ' ' +'-' + ' ' +'-' + ' ' +'-' + ' '+'\n',end ='')
    
#updates the board dictionary object based on player input
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

#function to clear the board dictiobary object in the event the game is restarted
def clearBoard():
    for i in theBoard: 
        theBoard[i] = ' '
        
#checks for 'win' conditions
#if a 'win' condition exists, the game ends and the players are asked if they want to play again 
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
            playAgain = ''
            while(playAgain not in allowedInputsRestart):
                playAgain = input('Would you like to play again? (y/n)')
            if(playAgain == 'y'):
                clearBoard()
                playerTurn()
            elif(playAgain == 'n'):
                exit()


#checks for a drawn game (i.e. no ' ' (i.e. space) values exist in the dictionary = a draw, since the board is full and no more moves are possible)
def checkForDraw():
    print(' ' in theBoard.values())
    if((' ' in theBoard.values()) == False):
        printBoard()
        print('The game is a draw!')
        playAgain = ''
        while(playAgain not in allowedInputsRestart):        
            playAgain = input('Would you like to play again? (y/n)')
        if(playAgain == 'y'):
            clearBoard()
            playerTurn()
        else:
            exit()

#a while loop that asks for player input, checks if the players want to exit, and checks for winning conditions or a draw
def playerTurn():
    gameStatus = 'Continue'
    player1 = True
    
    while(gameStatus != 'exit'):
     
        #print the board
        printBoard()

        #toggle the selected player automatically
        playerSelected = ('Player 1') if (player1 == True) else ('Player 2')

        #get desired cell from players
        playerInput = ''
        while(playerInput not in allowedInputs):
            playerInput = input(playerSelected + ': Toggle which cell? \n')
        
        #check if player(s) want to exit the game. If yes, the game is exited.
        if(playerInput == 'exit'):
            print('Thanks for playing, bye!')
            exit()
        elif((playerInput != 'exit') & (list(theBoard.values())[int(playerInput)-1] != ' ')):
            print('That cell already has a value, please pick another cell')
            continue   
        else:
            updateBoard(playerInput,playerSelected)
        
        #checks for 'win' condition by calling checkForWinner() function and passing in the currently selected player
        checkForWinner(playerSelected)
        
        #checks for a draw by calling checkForDraw() function
        checkForDraw()
        
        player1 = not player1

#game() is the entry point to the game
def game():
    playerTurn()

###global variables###

#the dictionary used to track values in the tic-tac-toe board
theBoard = {
    'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'top-L': ' ', 'top-M': ' ', 'top-R': ' '
}

allowedInputs = ('1','2','3','4','5','6','7','8','9','exit')
allowedInputsRestart = ('y','n')

#running the game through the game() function
game()
