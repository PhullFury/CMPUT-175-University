# ----------------------------------------------------
# Lab 3: Numerical Tic Tac Toe class
# 
# Author: Harmanpreet Singh Phull
# Collaborators: None
# References: https://www.geeksforgeeks.org/sum-function-python/ and https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/
# ----------------------------------------------------

class NumTicTacToe:
    def __init__(self):
        """
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        """
        self.board = []  # list of lists, where each internal list represents a row
        self.size = 3  # number of columns and rows of board

        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)

    def drawBoard(self):
        """
        Displays the current state of the board, formatted with column and row
        indices shown.
        Inputs: none
        Returns: None
        """
        print("   0   1   2 ")
        # loops the board
        for m in range(self.size):
            temp = []  # temporary list for printing the board
            for n in range(self.size):
                if (self.board[m][n] == 0):
                    temp.append(" ")
                else:
                    temp.append(self.board[m][n])
                if (len(temp) == self.size):  # prints when temp has gotten all the entries of a given row
                    print(f"{m}  {temp[0]} | {temp[1]} | {temp[2]} ")
                    if (not m == self.size - 1):  # only prints if it's not the last row of the board
                        print("  -----------")

    def squareIsEmpty(self, row, col):
        """
        Checks if a given square is empty, or if it already contains a number
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        """
        # returns true if the requested square has the value 0
        if (self.board[row][col] == 0):
            return True
        else:
            return False

    def update(self, row, col, num):
        """
        Assigns the integer, num, to the board at the provided row and column, but
        only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        """
        Dupes = False
        # checks if the entered number is a duplicate or not
        for i in self.board:
            if (num in i):
                Dupes = True

        #checks if the requested square is empty and if the entered number is within the acceptable range
        if (self.squareIsEmpty(row, col) and not num > 9 and not num < 0 and not Dupes):
            self.board[row][col] = num
            self.drawBoard()
            return True
        else:
            return False

    def boardFull(self):
        """
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        """
        BoardFull = True
        # loops every square in the board and makes BoardFull false if there is a zero in any square
        for m in self.board:
            for n in m:
                if (n == 0):
                    BoardFull = False

        return BoardFull

    def isWinner(self):
        """
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move;
                 False otherwise
        """
        Win = False
        # checks if any horizontal row had the sum 15
        for i in self.board:
            if (0 not in i and sum(i) == 15):
                Win = True

        # used to store values on the diagonals
        Diag1 = []
        Diag2 = []
        for n in range(self.size):
            temp = []
            Diag1.append(self.board[n][n])  # gets the left to right diagonal
            Diag2.append(self.board[n][self.size-1-n])  # gets the right to left diagonal
            # checks if any vertical row had the sum 15
            for m in range(self.size):
                temp.append(self.board[m][n])
            if (0 not in temp and sum(temp) == 15):
                Win = True
            if (Win):
                break
        # checks if any diagonal row had the sum 15
        if (0 not in Diag1 and sum(Diag1) == 15):
            Win = True
        if (0 not in Diag2 and sum(Diag2) == 15):
            Win = True

        if (Win):
            return True
        else:
            return False


if __name__ == "__main__":
    ContPlay = True
    # continues to loops until player(s) request to stop
    while ContPlay:
        print()
        Title = "Starting new Numerical Tic Tac Toe game"
        print("-"*len(Title))
        print(Title)
        print("-"*len(Title))
        GameBoard = NumTicTacToe()  # initializes a board
        GameBoard.drawBoard()
        SomeWin = False
        while not SomeWin:
            # asks player 1 for input
            num = int(input("\nPlayer 1, please enter an odd number (1-9): "))
            row = int(input("Player 1, please enter a row: "))
            col = int(input("Player 1, please enter a column: "))
            # loops until the input is correct
            while (not GameBoard.update(row, col, num)):
                print("\nInvalid Move.\nPlease try again.")
                num = int(input("\nPlayer 1, please enter an odd number (1-9): "))
                row = int(input("Player 1, please enter a row: "))
                col = int(input("Player 1, please enter a column: "))
            # checks if the player 1 won
            if (GameBoard.isWinner()):
                print("\nPlayer 1 wins. Congrats!")
                SomeWin = True
            # checks if the game tied
            if (GameBoard.boardFull()):
                print("\nThe board is full. It's a tie!")
                break
            # this exists so player 2 doesn't get asked for input after losing
            if (not SomeWin):
                # same as player 1 but for the player 2
                num = int(input("\nPlayer 2, please enter an even number (2-8): "))
                row = int(input("Player 2, please enter a row: "))
                col = int(input("Player 2, please enter a column: "))
                while (not GameBoard.update(row, col, num)):
                    print("\nInvalid Move.\nPlease try again.")
                    num = int(input("\nPlayer 2, please enter an even number (2-8): "))
                    row = int(input("Player 2, please enter a row: "))
                    col = int(input("Player 2, please enter a column: "))
                if (GameBoard.isWinner()):
                    print("\nPlayer 2 wins. Congrats!")
                    SomeWin = True
        Opt = input("\nDo you want to play another game? (Y/N): ")
        if (Opt.lower() == "n"):
            ContPlay = False