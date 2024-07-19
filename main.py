from directed_maze import DirectedMaze
import VisualizeMaze

# config parameters
maze_rows = 7
maze_cols = 20


if __name__ == '__main__':
    A = DirectedMaze(maze_rows, maze_cols)
    A.randomize_root(30*A.rows*A.cols)
    VisualizeMaze.view_binary_maze(A.convert_maze_to_binary())
    

