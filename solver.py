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

        self.last_accessed_cell = [0,0]

        try:
            if not self.construct_maps():
                raise Exception
        except Exception as err:
            print("EXCEPTION: <INPUT ERROR>")
            print("input puzzle is unsolvable.")
            return -1

    def solve(self):
        '''
        Construct a solution to the input puzzle.

        Idea: Use a selection algorithm to pick an empty cell and assign a valid candidate number to that cell.
        Continually do this until all cells are filled or we reach an unsolvable state. In the latter case, undo the
        most recent decisions until the game becomes solvable again, and continue.
        '''
        pass

    def select_in_order(self):
        '''
        Simple algorithm for determining which cell to choose next. Reads board from left to right, top to bottom and
        returns the next empty cell after a maintained class pointer
        '''
        [cur_row, cur_col] = self.last_accessed_cell
        for col in range(cur_col, 10):
            # first (possibly partial) row has a slightly different loop
            if self.input_board[cur_row, col] == ".":
                self.last_accessed_cell = [cur_row, col]
                return self.last_accessed_cell
        for row in range(cur_row, 10):
            for col in range(10):
                if self.input_board[row][col] == ".":
                    self.last_accessed_cell = [row, col]
                    return self.last_accessed_cell
        return [-1, -1]
    
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
