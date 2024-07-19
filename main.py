from directed_maze import DirectedMaze
import VisualizeMaze


if __name__ == '__main__':
    A = DirectedMaze(10,10)
    A.randomize_root(30*A.rows*A.cols)
    VisualizeMaze.view_binary_maze(A.convert_maze_to_binary())
    

