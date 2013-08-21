#-------------------------------------------------------------------------------
# Name:        tictactoe.py
# Purpose:     This is a tic-tac-toe game I made from scratch in python in the
#              past few days. There may be some glitches in it, but it's pretty
#              stable. The board is a no-frills 2d array. The board numbers go
#              from left to right from 1-9. The user types in which number block
#              they want their piece to land on. The computer uses randrange
#              to determine which space it wants to land on, so it's a beginner-
#              friendly version of tic tac toe (haha). This game can be done
#              by using functions instead. I wanted to try OOP for fun.
#
#              NOTE: This is not up to par with python 3.x, works well in 2.7.
#              raw_input and print statements are based off 2.x python syntax.
#              there may be other non-py3-compatible lines here too.
#              raw_input() switched to input(), print switched to print().
#
# Author:      Monique Blake
#
# Created:     14/08/2013
# Copyright:   (c) Monique Blake 2013
# Licence:     None
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import random

class TicTacToe:

    # constructor
    def __init__(self):
        self.board = [] # blank board initialized
        self.pieces = ["x", "o"] # board pieces
        self.totalTurns = 0 # counter to get total turns in game
        self.isFirstTurnSet = False # did game designate who will go first?

    # selectPiece assigns user's raw input to a piece x or o.
    def selectPiece(self, userPiece):
        if userPiece.lower() == "x":
            self.userPiece, self.computerPiece = self.pieces[0], self.pieces[1]
        else:
            self.userPiece, self.computerPiece = self.pieces[1], self.pieces[0]

        # once that is all figured out...
        self.drawBoard()  # draw the board
        self.printBoard() # print the board
        self.nextTurn()   # get the turns, too

    #---------------------------------------------------------------------------
    # drawBoard draws a 2d, 3 x 3 blank board with tile numbers 1-9.
    #---------------------------------------------------------------------------
    def drawBoard(self):
        count = 1
        for i in range(3):
            self.board.append([]) # make 3 blank arrays for i
            for j in range(3):
                self.board[i].append(["_", count]) # append items into i
                count = count + 1

    #---------------------------------------------------------------------------
    # printboard does a loop inside drawBoard and prints it out then
    # adds a newline for every j array for formatting purposes.
    # should initially look like:
    # _ _ _
    # _ _ _
    # _ _ _
    #---------------------------------------------------------------------------
    def printBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print self.board[i][j][0], # get only the _'s not the numbers
            print
        print


    #---------------------------------------------------------------------------
    # chooseFirstTurn determines who will go first, the player or the computer
    # uses randrange on the pieces array to choose which one will do so.
    #---------------------------------------------------------------------------
    def chooseFirstTurn(self):
        firstPlayer = random.randrange(0, 2)
        if self.pieces.index(self.userPiece) == firstPlayer:
            print self.userPiece, "goes first. It's your turn."
            return self.userPiece
        else:
            print self.computerPiece, "goes first. It's the computer's turn."
            return self.computerPiece

    #---------------------------------------------------------------------------
    # nextTurn gets each turn of the players. chooseFirstTurn is initially
    # called once chooseFirstTurn is called, then the cycle begins
    # use of a counter and modulus determines who will go next
    # nextTurn also checks to see if the game state deems the game
    # as game over once the game state checks have been proven as true
    # this is whether it there is a tie or a 3 in a row.
    #---------------------------------------------------------------------------
    def nextTurn(self):
        # list of possible moves for computer
        compBoardlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # if first turn, designate the first player before getting their input
        if self.isFirstTurnSet == False:
            firstPlayer = self.chooseFirstTurn() # returns which player goes 1st
            self.isFirstTurnSet = True

            # here we set/designate our second player
            if firstPlayer == self.userPiece:
                secondPlayer = self.computerPiece
            else:
                secondPlayer = self.userPiece

        # once the game has a first player, start the game and check game state
        while self.checkStateOfGame() == False: # Run until game is over.

            # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
            # if the program designates the user as player # 1, get user input.
            # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
            if (self.totalTurns % 2 == 0) and (firstPlayer == self.userPiece):
                indexFound = False

                # try/catch block in case user types in non number character
                try:
                    boardInput = int(raw_input("Choose block to place piece. \
First tile = 1, Last tile = 9"))
                except ValueError:
                    boardInput = int(raw_input("Error, you need to type a number from 1-9."))

                # if boardinput num. is within the range of 1-9, get player move
                if (9 >= boardInput >= 1):
                    while indexFound == False: # loop until boardInput num is found
                        for i in range(len(self.board)): # looks for value in array
                            for j in range(len(self.board[i])):
                                # check for vacancy then append onto the space indicated
                                if (self.board[i][j][1] == boardInput) and \
                                (self.board[i][j][0] == "_"):
                                    self.board[i][j].pop(0)
                                    self.board[i][j].insert(0, self.userPiece)
                                    indexFound = True

                                # if the space is occupied but boardInput is found
                                elif (self.board[i][j][1] == boardInput) and (self.board[i][j][0] != "_"):
                                    # ask again
                                    boardInput = int(raw_input("That's occupied.\
 Choose blank block to place piece. First tile = 1, Last tile = 9"))

                    self.totalTurns += 1 # increment counter
                    self.printBoard() # re-display board

                else: # ask again
                    try:
                        boardInput = int(raw_input("Error, not in range. Choose\
 blank block to place piece. First tile = 1, Last tile = 9"))
                    except ValueError:
                        boardInput = int(raw_input("Error, you need to type a number from 1-9."))


            # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
            # the computer's version is based on randrange. Not as intelligent
            # as making an algorithm based on possible user moves.
            # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
            elif (self.totalTurns % 2 == 0) and (firstPlayer == self.computerPiece):
                # obtaining random number element in list
                boardInput = compBoardlist[random.randrange(0, len(compBoardlist))]
                indexFound = False

                while indexFound == False:
                    for i in range(len(self.board)):
                        for j in range(len(self.board[i])):
                            # check for vacancy then append onto the space indicated
                            if (self.board[i][j][1] == boardInput) and (self.board[i][j][0] == "_"):
                                self.board[i][j].pop(0)
                                self.board[i][j].insert(0, self.computerPiece)
                                # space is occupied by computer; no longer an option
                                compBoardlist.remove(boardInput)
                                indexFound = True # while loop will terminate

                            elif (self.board[i][j][1] == boardInput) and (self.board[i][j][0] != "_"):
                                # remove number from the board list; no longer an option
                                compBoardlist.remove(boardInput)
                                # get another random number
                                boardInput = compBoardlist[random.randrange(0, len(compBoardlist))]

                self.totalTurns += 1 # increment counter
                self.printBoard() # re-display board


            # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
            # now let's get second player's turn
            # assume that the user is the second player
            # user will go and place its piece onto the board on this turn.
            # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
            else:
                if (self.totalTurns % 2 == 1) and (secondPlayer == self.userPiece):
                    indexFound = False

                    # try/catch block if user types in non-number character
                    try:
                        boardInput = int(raw_input("Choose block to place piece.\
 First tile = 1, Last tile = 9"))
                    except ValueError:
                        boardInput = int(raw_input("Error, you need to type a number from 1-9."))

                    # if boardinput num. is within the range of 1-9, get player move
                    if (9 >= boardInput >= 1):
                        while indexFound == False:
                            for i in range(len(self.board)):
                                for j in range(len(self.board[i])):
                                    # check for vacancy then append onto the space indicated
                                    if (self.board[i][j][1] == boardInput) and (self.board[i][j][0] == "_"):
                                        self.board[i][j].pop(0)
                                        self.board[i][j].insert(0, self.userPiece)
                                        indexFound = True

                                    elif (self.board[i][j][1] == boardInput) and (self.board[i][j][0] != "_"):
                                        # ask again
                                        boardInput = int(raw_input("That's \
occupied. Choose blank block to place piece. First tile = 1, Last tile = 9"))

                        self.totalTurns += 1 # increment counter
                        self.printBoard() # re-display board

                    else: # ask again
                        try:
                            boardInput = int(raw_input("Error, not in range. \
Choose blank block to place piece. First tile = 1, Last tile = 9"))
                        except ValueError:
                            boardInput = int(raw_input("Error, you need to type a number from 1-9."))

                # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                # assume second player is the computer, get the computer's turn.
                # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                else:
                    # obtaining random number element in list
                    boardInput = compBoardlist[random.randrange(0, len(compBoardlist))]
                    indexFound = False

                    while indexFound == False:
                        for i in range(len(self.board)):
                            for j in range(len(self.board[i])):
                                if (self.board[i][j][1] == boardInput) and (self.board[i][j][0] == "_"):
                                    self.board[i][j].pop(0)
                                    self.board[i][j].insert(0, self.computerPiece)

                                    print "The computer has made its move, now it is your turn."
                                    # that space is occupied by computer; no longer an option
                                    compBoardlist.remove(boardInput)
                                    indexFound = True

                                elif (self.board[i][j][1] == boardInput) and (self.board[i][j][0] != "_"):
                                    # remove that number from the board list; no longer an option
                                    compBoardlist.remove(boardInput)
                                    # get another random number
                                    boardInput = compBoardlist[random.randrange(0, len(compBoardlist))]

                    self.totalTurns += 1 # increment counter
                    self.printBoard() # re-display the board

        replay = raw_input("Game Over. Press 'Y' or 'y' to play again. Any key to exit.")
        if replay.lower() == 'y':
            # call main function again and start game over.
            main()

    #---------------------------------------------------------------------------
    # checkStateOfGame: sees if game has no more tiles or 3 in a row is found
    # uses loops to check if vertical/horizontal 3 in a row exists.
    #---------------------------------------------------------------------------
    def checkStateOfGame(self):
        if(9 >= self.totalTurns > 0):
            # first check: find 3 in a row vertically/horizontally/diagonally
            for i in range(len(self.board)):
                for j in range(1):
                    # checks 3 in a horizontal row
                    if (self.board[i][j][0] != "_") and (self.board[i][j][0] ==
                    self.board[i][j+1][0] == self.board[i][j+2][0]):
                        print "3 in a row!"
                        return True

            for i in range(1):
                for j in range(len(self.board[i])):
                    # checks 3 in a vertical row
                    if (self.board[i][j][0] != "_") and (self.board[i][j][0] ==
                    self.board[i+1][j][0] == self.board[i+2][j][0]):
                        print "3 in a row!"
                        return True

        if ((self.board[0][0][0] == self.board[1][1][0] == self.board[2][2][0] == 'x')
             or (self.board[0][0][0] == self.board[1][1][0] == self.board[2][2][0] == 'o')):
                print "3 in a row!"
                return True

        if ((self.board[0][2][0] == self.board[1][1][0] == self.board[2][0][0] == 'x')
            or (self.board[0][2][0] == self.board[1][1][0] == self.board[2][0][0] == 'o')):
                print "3 in a row!"
                return True

        # second check: see if there is a tie, a tie will end the game
        if (self.totalTurns == 9): # if counter = 9, then game over
            print "It's a tie!"
            return True
        return False

#-------------------------------------------------------------------------------
# main() starts up the tictactoe game.
#-------------------------------------------------------------------------------
def main():

    myGame = TicTacToe() # creates instance of the TicTacToe class, aka: myGame
    myGame.selectPiece(raw_input("Welcome to Tic Tac Toe! Choose your piece (x or o)."))


main() # calls main() function which calls the TicTacToe class which starts game