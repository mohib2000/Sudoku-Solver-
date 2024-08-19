############ CODE BLOCK 0 ################
# DO NOT CHANGE THIS CELL.
# THESE ARE THE ONLY IMPORTS YOU ARE ALLOWED TO USE:

import numpy as np
import copy

RNG = np.random.default_rng()

############ CODE BLOCK 10 ################
class Sudoku():
    """
    This class creates sudoku objects which can be used to solve sudokus.
    A sudoku object can be any size grid, as long as the square root of the size is a whole integer.
    To indicate that a cell in the sudoku grid is empty we use a zero.
    A sudoku object is initialized with an empty grid of a certain size.

    Attributes:
        :param self.grid: The sudoku grid containing all the digits.
        :type self.grid: np.ndarray[(Any, Any), int]  # The first type hint is the shape, and the second one is the dtype.
        :param self.size: The width/height of the sudoku grid.
        :type self.size: int
    """
    def __init__(self, size=9):
        self.grid = np.zeros((size, size))
        self.size = size

    def __repr__(self):
        """
        This returns a representation of a Sudoku object.

        :return: A string representing the Sudoku object.
        :rtype: str
        """
        # Representation of the Sudoku grid for easier debugging.
        grid_str = "\n".join([" ".join(map(str, row)) for row in self.grid])
        return f"Sudoku({self.size}x{self.size}):\n{grid_str}"

############ CODE BLOCK 11 ################
    def set_grid(self, grid):
        """
        This method sets a new grid. This also can change the size of the sudoku.

        :param grid: A 2D numpy array that contains the digits for the grid.
        :type grid: ndarray[(Any, Any), int]
        """
        self.grid = grid
        self.size = grid.shape[0]

############ CODE BLOCK 12 ################
    def get_row(self, row_id):
        """
        This method returns the row with index row_id.

        :param row_id: The index of the row.
        :type row_id: int
        :return: A row of the sudoku.
        :rtype: np.ndarray[(Any,), int]
        """
        return self.grid[row_id]

    def get_col(self, col_id):
        """
        This method returns the column with index col_id.

        :param col_id: The index of the column.
        :type col_id: int
        :return: A row of the sudoku.
        :rtype: np.ndarray[(Any,), int]
        """
        return self.grid[:, col_id]

    def get_box_index(self, row, col):
        """
        This returns the box index of a cell given the row and column index.

        :param col: The column index.
        :type col: int
        :param row: The row index.
        :type row: int
        :return: This returns the box index of a cell.
        :rtype: int
        """
        box_size = int(np.sqrt(self.size))
        return (row // box_size) * box_size + (col // box_size)

    def get_box(self, box_id):
        """
        This method returns the "box_id" box.

        :param box_id: The index of the sudoku box.
        :type box_id: int
        :return: A box of the sudoku.
        :rtype: np.ndarray[(Any, Any), int]
        """
        box_size = int(np.sqrt(self.size))
        row_start = (box_id // box_size) * box_size
        col_start = (box_id % box_size) * box_size
        return self.grid[row_start:row_start + box_size, col_start:col_start + box_size]

############ CODE BLOCK 13 ################
    @staticmethod
    def is_set_correct(numbers):
        """
        This method checks if a set (row, column, or box) is correct according to the rules of a sudoku.
        In other words, this method checks if a set of numbers contains duplicate values between 1 and the size of the sudoku.
        Note, that multiple empty cells are not considered duplicates.

        :param numbers: The numbers of a sudoku's row, column, or box.
        :type numbers: np.ndarray[(Any, Any), int] or np.ndarray[(Any, ), int]
        :return: This method returns if the set is correct or not.
        :rtype: Boolean
        """
        # Remove zeros as they represent empty cells
        numbers = numbers[numbers != 0]
        return len(numbers) == len(set(numbers))

    def check_cell(self, row, col):
        """
        This method checks if the cell, denoted by row and column, is correct according to the rules of sudoku.

        :param col: The column index that is tested.
        :type col: int
        :param row: The row index that is tested.
        :type row: int
        :return: This method returns if the cell, denoted by row and column, is correct compared to the rest of the grid.
        :rtype: boolean
        """
        num = self.grid[row, col]
        if num == 0:
            return True  # Empty cells are always correct
        row_correct = self.is_set_correct(self.get_row(row))
        col_correct = self.is_set_correct(self.get_col(col))
        box_correct = self.is_set_correct(self.get_box(self.get_box_index(row, col)).flatten())
        return row_correct and col_correct and box_correct

    def check_sudoku(self):
        """
        This method checks, for all rows, columns, and boxes, if they are correct according to the rules of a sudoku.
        In other words, this method checks, for all rows, columns, and boxes, if a set of numbers contains duplicate values between 1 and the size of the sudoku.
        Note, that multiple empty cells are not considered duplicates.

        Hint: It is not needed to check if every cell is correct to check if a complete sudoku is correct.

        :return: This method returns if the (partial) Sudoku is correct.
        :rtype: Boolean
        """
        for i in range(self.size):
            if not self.is_set_correct(self.get_row(i)) or not self.is_set_correct(self.get_col(i)):
                return False
        box_count = int(np.sqrt(self.size))
        for i in range(box_count * box_count):
            if not self.is_set_correct(self.get_box(i).flatten()):
                return False
        return True

############ CODE BLOCK 14 ################
    def step(self, row=0, col=0, backtracking=False):
        """
        This is a recursive method that completes one step in the exhaustive search algorithm.
        A step should contain at least, filling in one number in the sudoku and calling "next_step" to go to the next step.
        If the current number for this step does not give a correct solution another number should be tried
        and if no numbers work the previous step should be adjusted.

        This method should work for both backtracking and exhaustive search.

        Hint 1: Numbers, that are already filled in should not be overwritten.
        Hint 2: Think about a base case.
        Hint 3: The step method from the previous jupyter notebook cell can be copy-paste here and adjusted for backtracking.

        :param col: The current column index.
        :type col: int
        :param row: The current row index.
        :type row: int
        :param backtracking: This determines if backtracking is used, defaults to False.
        :type backtracking: boolean, optional
        :return: This method returns if a correct solution can be found using this step.
        :rtype: boolean
        """
        if row == self.size:
            return True  # Reached the end of the grid successfully

        if col == self.size:
            return self.next_step(row, 0, backtracking)  # Move to the next row

        if self.grid[row, col] != 0:
            return self.next_step(row, col + 1, backtracking)  # Skip filled cells

        for num in range(1, self.size + 1):
            self.grid[row, col] = num
            if backtracking or self.check_cell(row, col):  # Check cell validity if backtracking is enabled
                if self.next_step(row, col + 1, backtracking):
                    return True
            self.clean_up(row, col)  # Reset cell and try next number

        return False  # No valid number found for this cell

    def next_step(self, row, col, backtracking):
        """
        This method calculates the next step in the recursive exhaustive search algorithm.
        This method should only determine which cell should be filled in next.

        This method should work for both backtracking and exhaustive search.

        :param col: The current column index.
        :type col: int
        :param row: The current row index.
        :type row: int
        :param backtracking: This determines if backtracking is used, defaults to False.
        :type backtracking: boolean, optional
        :return: This method returns if a correct solution can be found using this next step.
        :rtype: boolean
        """
        if col < self.size - 1:
            return self.step(row, col + 1, backtracking)
        else:
            return self.step(row + 1, 0, backtracking)


    def clean_up(self, row, col):
        """
        This method cleans up the current cell if no solution can be found for this cell.

        This method should work for both backtracking and exhaustive search.

        :param col: The current column index.
        :type col: int
        :param row: The current row index.
        :type row: int
        :return: This method returns if a correct solution can be found using this next step.
        :rtype: boolean
        """
        self.grid[row, col] = 0
        return False

    def solve(self, backtracking=False):
        """
        Solve the sudoku using recursive exhaustive search or backtracking.
        This is done by calling the "step" method, which does one recursive step.
        This can be visualized as a process tree, where "step" completes the functionality of of node.

        This method is already implemented and you do not have to do anything here.

        :param backtracking: This determines if backtracking is used, defaults to False.
        :type backtracking: boolean, optional
        :return: This method returns if a correct solution for the whole sudoku was found.
        :rtype: boolean
        """
        return self.step(backtracking=backtracking)


############ END OF CODE BLOCKS, START SCRIPT BELOW! ################
