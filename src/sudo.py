#!/usr/bin/python3
import sys

class Solver():
    
    def display(self, grid) -> None:
        """
        Draws numbers from Sudoku array onto their respective board positions in command line
        """
        for i in range(len(grid)):
            if i % 3 == 0 and i != 0:
                print() 
            for j in range(len(grid[0])):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                print(grid[i][j], end = " ")
            print()


    def get_empty_square(self, grid) -> tuple:
        """
        Finds the first empty entry on Sudoku board and return row, col
        """
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0:
                    return (i, j)


    def is_valid(self, grid, square, num) -> bool:
        """
        Checks if a number being placed in Sudoku board follows the rules of the game
        """

        # Compare square with current column
        for i in range(len(grid)):
            if grid[i][square[1]] == num:
                return False

        # Compare square with current row
        for i in range(len(grid)):
            if grid[square[0]][i] == num:
                return False
        
        # Get the x and y coordinates for the 3x3 box the square is located in
        squareX = int(square[1] / 3) * 3
        squareY = int(square[0] / 3) * 3

        # Loop and compare numbers through the box containing square being tested
        for i in range(squareY, squareY + 3):
            for j in range(squareX, squareX + 3):
                if grid[i][j] == num:
                    return False
        return True

    def recursive_solve(self,grid) -> bool:
        """
        Solve Sudoku using Recursive Backtracking 
        """
        # Find the first empty entry on Sudoku board and return row, col
        empty = self.get_empty_square(grid)
        if empty is None:
            return True
        else:
            row, col = empty

        for i in range(1, 10):
            # If number i is valid so far
            if self.is_valid(grid, empty, i):
                grid[row][col] = i

                # Try solving rest of puzzle after filling in new value
                if self.recursive_solve(grid):
                    return True
                # If the rest of puzzle was not solved with position using index then reset that square
                grid[row][col] = 0
            
        return False


if __name__ == "__main__":
    board = []
    if (len(sys.argv) > 1):
        fileName = sys.argv[1]
    else:
        print("No file found in executable command")
        exit()

    # Reads Sudoku board file and store each number in a 2D list
    with open(fileName, "r") as file:
            line = []
            while True:
                comp = file.read(1)
                if not comp:
                    break
                if (comp == '\n'):
                    board.append(line)
                    line = []
                else:
                    line.append(int(comp))
    
    solve = Solver()
    print("Sudoku Grid from file:")
    print("-"*25)
    solve.display(board)
    solve.recursive_solve(board)
    print("\n\nSudoku Grid Solved:")
    print("-"*25)
    solve.display(board)
    print()
