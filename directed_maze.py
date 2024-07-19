from random import randint
from utils import evaluate_type


class DirectedMaze:
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
    def create_starting_maze(cls, rows, cols):
        if not evaluate_type(int, rows, cols):
            raise TypeError("both rows and cols should be int")
        assert rows > 0, f'rows is expected to be greater then 0, got: {rows}'
        assert cols > 0, f'cols is expected to be greater then 0, got: {cols}'

        maze = [[cls.create_starting_directions(row+1, col+1, rows, cols) for col in range(cols)] for row in range(rows)]
        return maze

    def __init__(self, rows, cols):
        self.list = self.create_starting_maze(rows, cols)
        self.rows = rows
        self.cols = cols
        self.root = (rows, cols)
        self.valid_values = ["N", "W", "E", "S", "R"]
    def __repr__(self):
        return 'Maze({!r}, {!r})'.format(self.rows, self.cols)
    def __str__(self):
        msg = ""
        for row in self.list:
            msg = msg + ''.join(row) + "\n"
        return msg
    def __len__(self):
        return self.rows * self.cols
    
    def col(self, x): #wrong
        return [row[x-1] for row in self.list]
    def row(self, x):
        return self.list[x-1]
    
    def is_cell_in_range(self, row, col):
        return (0 < row <= self.rows) and (0 < col <= self.cols)
    def move_in_direction(self, row, col, direction):
        if direction not in self.valid_values:
            raise ValueError(f"direction {direction} not supported by move_in_direction")
        new_row, new_col = row, col
        if direction == "N": new_row = row-1
        if direction == "S": new_row = row+1
        if direction == "W": new_col = col-1
        if direction == "E": new_col = col+1
        return (new_row, new_col)
    def is_move_valid(self, row, col, direction):
        if direction not in self.valid_values:
            return False
        new_row, new_col = self.move_in_direction(row, col, direction)
        return self.is_cell_in_range(new_row, new_col)
    
    def change_cell(self, row, col, new_value):
        if not self.is_cell_in_range(row, col):
            raise ValueError(f"Can not change cell ({row}, {col}) for it is out of bounds")
        if new_value not in self.valid_values:
            raise ValueError(f"{new_value} is not a valid value. choose between {self.valid_values}")
        self.list[row-1][col-1] = new_value
    def change_root(self, direction):
        row, col = self.root
        assert self.list[row-1][col-1] == "R", f'the root has: {self.list[row-1][col-1]} instead of R'
        if not self.is_move_valid(row, col, direction):
            raise ValueError(f"can't change root in that direction. row={row}, col={col}, direction={direction}")
        new_row, new_col = self.move_in_direction(row, col, direction)
        self.root = (new_row, new_col)
        self.change_cell(row, col, direction)
        self.change_cell(new_row, new_col, "R")
    def randomize_root(self, times):
        for _ in range(times):
            cardinal_choice = self.valid_values[:-1]
            valid_cardinal_choices = []
            row, col = self.root
            for direction in cardinal_choice:
                if self.is_move_valid(row, col, direction):
                    valid_cardinal_choices.append(direction)
            assert len(valid_cardinal_choices) > 0, "there is no path the root can take?!?"
            #print(valid_cardinal_choices)
            choosen_path = valid_cardinal_choices[randint(0, len(valid_cardinal_choices)-1)]
            #print(choosen_path)
            self.change_root(choosen_path)
    def convert_maze_to_binary(self):
        def is_border(row, col):
            return 1-col%2 or 1-row%2
        def break_wall(row, col, direction):
            new_row, new_col = self.move_in_direction(row, col, direction)
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
    


