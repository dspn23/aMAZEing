"""
Feel free to change the config parameters 
Then just run this module to generate your maze
"""

from directed_maze import DirectedMaze
import VisualizeMaze

# config parameters
MAZE_ROWS = 7
MAZE_COLS = 20


if __name__ == '__main__':
    A = DirectedMaze(MAZE_ROWS, MAZE_COLS)
    A.randomize_root(30*A.rows*A.cols)
    VisualizeMaze.view_binary_maze(A.convert_maze_to_binary())
