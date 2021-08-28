class Solver:
    '''
    Class that solves a puzzle given an input board

    Input board is formatted as a 2D list with integers representing solved tiles and "."
    representing an empty cell. Example shown below:
    input_board =
    [[1,".","."],[7,".","."]
    '''
    def __init__(self, board):
        self.input_board = board
        self.candidate_map = {(x,y):set([i for i in range(1,10)]) for x in range(9) for y in range(9)}

        try:
            if not self.construct_maps():
                raise Exception
        except Exception as err:
            print("EXCEPTION: <INPUT ERROR>")
            print("input puzzle is unsolvable.")

    def solve(self):
        '''
        Construct a solution to the input puzzle.
        '''
        pass
    def construct_maps(self):
        '''
        Given an input board, construct hash maps to store list of possible solutions for each tile.
        '''
        for row in range(9):
            for col in range(9):
                if self.input_board[row][col] != ".":
                    self.candidate_map[(row,col)] = {self.input_board[row][col]}
                    if not self.remove_row_candidates(row, col, self.input_board[row][col]) or \
                    not self.remove_col_candidates(row, col, self.input_board[row][col]) or \
                    not self.remove_square_candidates(row, col, self.input_board[row][col]):
                        return False
        return True

    def remove_row_candidates(self, row, col, num):
        '''
        Given a row and column number as well as a number, remove the num from all the candidate sets in that row
        with the exception of the cell located at the column number.

        Return: False if a solution becomes impossible, else True
        '''
        for i in range(9):
            if i != col:
                if num in self.candidate_map[(row, i)]:
                    self.candidate_map[(row, i)].remove(num)
                    if not self.candidate_map[(row, i)]:
                        return False
        return True

    def remove_col_candidates(self, row, col, num):
        '''
        Given a row and column number as well as a number, remove the num from all the candidate sets in that column
        with the exception of the cell located at the row number.

        Return: False if a solution becomes impossible, else True
        '''
        for i in range(9):
            if i != row:
                if num in self.candidate_map[(i, col)]:
                    self.candidate_map[(i, col)].remove(num)
                    if not self.candidate_map[(i, col)]:
                        return False
        return True

    def remove_square_candidates(self, row, col, num):
        '''
        Given a row and column number as well as a number, remove the num from all the candidate sets in that square
        with the exception of the cell located at the row and column number.

        Return: False if a solution becomes impossible, else True
        '''
        square_row,square_col = row//3, col//3
        for r in range(square_row*3, square_row*3+3):
            for c in range(square_col*3, square_col*3+3):
                if (r != row or c != col) and num in self.candidate_map[(r,c)]:
                    self.candidate_map[(r,c)].remove(num)
                    if not self.candidate_map[(r,c)]:
                        return False
        return True
