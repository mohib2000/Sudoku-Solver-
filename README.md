
## Sudoku Solver Project

This project is centered on solving Sudoku puzzles using two primary algorithms: backtracking and exhaustive search. Implemented in Python, the project leverages object-oriented principles and the numpy library for efficient grid management and manipulation.
Core Objectives:

    Backtracking Algorithm: The solver uses backtracking to efficiently navigate through the Sudoku grid, filling in numbers and retracting steps when a number placement leads to an invalid state. This method is designed to find a solution by exploring valid possibilities and abandoning paths that do not lead to a solution.

    Exhaustive Search: As a contrast to backtracking, the exhaustive search approach attempts every possible number in every cell until the puzzle is solved. This method is thorough but less efficient, serving as a brute-force technique to solve the puzzle.

Key Components:

    Sudoku Class:
        Initialization (__init__): Creates an empty Sudoku grid (default is 9x9), represented as a 2D numpy array where zeros denote empty cells.
        Grid Management Methods:
            set_grid(grid): Sets a new grid and adjusts the grid size.
            get_row(row_id), get_col(col_id), get_block(row, col): Retrieves specific rows, columns, or blocks (sub-grids).
        Validation and Search Methods:
            possible_entries(row, col): Identifies valid numbers for a specific cell.
            next_cell(): Determines the next empty cell to process.
            step(row, col, backtracking=False): Implements the recursive step for solving the puzzle using either backtracking or exhaustive search.
            clean_up(row, col): Resets a cell when no valid numbers can be placed, facilitating the backtracking process.

    solve(backtracking=False) Method:
        The main method that drives the Sudoku-solving process, using either backtracking or exhaustive search based on the specified parameter.

Project Highlights:

    Focus on Algorithmic Solutions: The primary goal of this project is to compare and implement backtracking and exhaustive search techniques for solving Sudoku puzzles.
    Efficiency Through Backtracking: By incorporating backtracking, the solver intelligently avoids futile paths, significantly improving the time to find a solution compared to exhaustive search.
    Comprehensive Grid Management: Utilizing numpy arrays, the project ensures efficient handling and manipulation of the Sudoku grid, making it scalable for various grid sizes.

This project is a strong demonstration of how algorithmic approaches like backtracking can be effectively applied to solve complex problems like Sudoku, providing both a practical solution and insights into different algorithmic strategies.
