"""
This module defines the DirectedMaze Class.
Note that most of the methods of this Class are just auxiliar.
    the only 2 functions you might actually need to call are:
        > randomize_root
        > convert_maze_to_binary        
"""
from random import randint
from utils import evaluate_type


class DirectedMaze:
    """
    This class holds a 2D object (list of lists)
        each point in that 2D matrix is a single letter from:
            N for north
            S for south
            E for east
            W for west
            R for the root of the maze
        and by following those letters you will eventually reach R
            ex:
                [["E", "S"],
                 ["E", "R"]]
                from R0C0 you would travel East to R0C1 "S", from there you would
                travel South to R1C1 "R" and arrive at the root
    with this format, there is always a single 'right' way to procede 
    to reach the root of the maze, even if said way merges with others
    """
    @staticmethod
    def create_starting_directions(row: int, col: int, rows: int, cols: int) -> str:
        """
        Parameters
        ----------
        row : int
            the row of the cell
        col : int
            the column of the cell
        rows : int
            how many total rows are there
        cols : int
            how many total columns are there

        Returns
        -------
        str: E for East, S for South, R for root
        """
        if not evaluate_type(int, row, col, rows, cols):
            raise TypeError("All arguments (row, col, rows, cols) should be integers")

        assert row > 0, f'row is expected to be greater then 0, got: {row}'
        assert col > 0, f'col is expected to be greater then 0, got: {col}'
        assert rows > 0, f'rows is expected to be greater then 0, got: {rows}'
        assert cols > 0, f'cols is expected to be greater then 0, got: {cols}'
        assert row <= rows, f'row is expected to be smaller then rows, got: {row} row, {rows} rows'
        assert col <= cols, f'col is expected to be smaller then cols, got: {col} col, {cols} cols'

        if col < cols:
            return "E"
        if col == cols and row < rows:
            return "S"
        if col == cols and row == rows:
            return "R"
        assert False, "Create directions error"

    @classmethod
    def create_starting_maze(cls, rows: int, cols: int):
        """
        Run by __init__ method
        Parameters
        ----------
        rows : int
            how many rows should the maze have?
        cols : int
            how many cols should the maze have?
        
        Returns
            a simple maze to be used by this class
        -------
        maze : list of lists
            check on DirectedMaze docstring
        """
        if not evaluate_type(int, rows, cols):
            raise TypeError("both rows and cols should be int")
        assert rows > 0, f'rows is expected to be greater then 0, got: {rows}'
        assert cols > 0, f'cols is expected to be greater then 0, got: {cols}'

        maze = [[
            cls.create_starting_directions(row+1, col+1, rows, cols)
            for col in range(cols)]
            for row in range(rows)]
        return maze

    def __init__(self, rows, cols):
        self.list = self.create_starting_maze(rows, cols)
        self.rows = rows
        self.cols = cols
        self.root = (rows, cols)
        self.valid_values = ["N", "W", "E", "S", "R"]
    def __repr__(self):
        return f'Maze({self.rows}, {self.cols})'
    def __str__(self):
        msg = ""
        for row in self.list:
            msg = msg + ''.join(row) + "\n"
        return msg
    def __len__(self):
        return self.rows * self.cols

    def col(self, x: int) -> list:
        """returns the desired column"""
        if x <= 0:
            raise ValueError("col parameter should be a positive integer")
        if not isinstance(x, int):
            raise TypeError("col parameter should be a positive integer")
        return [row[x-1] for row in self.list]
    def row(self, x: int) -> list:
        """returns the desired row"""
        if x <= 0:
            raise ValueError("col parameter should be a positive integer")
        if not isinstance(x, int):
            raise TypeError("col parameter should be a positive integer")
        return self.list[x-1]

    def __is_cell_in_range(self, row, col):
        return (0 < row <= self.rows) and (0 < col <= self.cols)
    def __move_in_direction(self, row, col, direction):
        if direction not in self.valid_values:
            raise ValueError(f"direction {direction} not supported by __move_in_direction")
        new_row, new_col = row, col
        if direction == "N": new_row = row-1
        if direction == "S": new_row = row+1
        if direction == "W": new_col = col-1
        if direction == "E": new_col = col+1
        return (new_row, new_col)
    def __is_move_valid(self, row, col, direction):
        if direction not in self.valid_values:
            return False
        new_row, new_col = self.__move_in_direction(row, col, direction)
        return self.__is_cell_in_range(new_row, new_col)

    def __change_cell(self, row, col, new_value):
        if not self.__is_cell_in_range(row, col):
            raise ValueError(f"Can not change cell ({row}, {col}) for it is out of bounds")
        if new_value not in self.valid_values:
            raise ValueError(
                f"{new_value} is not a valid value. choose between {self.valid_values}")
        self.list[row-1][col-1] = new_value
    def __change_root(self, direction):
        row, col = self.root
        assert self.list[row-1][col-1] == "R", (
            f'the root has: {self.list[row-1][col-1]} instead of R')
        if not self.__is_move_valid(row, col, direction):
            raise ValueError(
                f"can't change root in that direction. row={row}, col={col}, direction={direction}")
        new_row, new_col = self.__move_in_direction(row, col, direction)
        self.root = (new_row, new_col)
        self.__change_cell(row, col, direction)
        self.__change_cell(new_row, new_col, "R")
    def randomize_root(self, times: int):
        """
        changes the root ("R") of the maze 
        in one random valid direction several times
        does not output anything, it just changes the object itself
        """
        for _ in range(times):
            cardinal_choice = self.valid_values[:-1]
            valid_cardinal_choices = []
            row, col = self.root
            for direction in cardinal_choice:
                if self.__is_move_valid(row, col, direction):
                    valid_cardinal_choices.append(direction)
            assert len(valid_cardinal_choices) > 0, "there is no path the root can take?!?"
            #print(valid_cardinal_choices)
            choosen_path = valid_cardinal_choices[randint(0, len(valid_cardinal_choices)-1)]
            #print(choosen_path)
            self.__change_root(choosen_path)
    def convert_maze_to_binary(self) -> list:
        """
        This is usefull to vizualize the maze as a binary map
        Creates a 2D (list of lists) containing only 0's (path) and 1's. (wall)
        Note that the resulting maze is of larger size (rows and cols)
        when compared to the original one
        """
        def is_border(row, col):
            return 1-col%2 or 1-row%2
        def break_wall(row, col, direction):
            new_row, new_col = self.__move_in_direction(row, col, direction)
            new_maze[new_row][new_col] = 0
        col, row = self.cols, self.rows
        maze = self.list
        new_row, new_col = row*2+1, col*2+1
        new_maze = [[is_border(row, col) for col in range(new_col)] for row in range(new_row)]
        for i, row in enumerate(maze):
            for col, direction in enumerate(row):
                #print(direction, col*2+1)
                break_wall(i*2+1, col*2+1, direction)
        return new_maze



if __name__ == '__main__':
    A = DirectedMaze(10,10)
    A.randomize_root(30*A.rows*A.cols)
    print(A)
