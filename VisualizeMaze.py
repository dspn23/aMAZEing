import matplotlib.pyplot as plt

def view_binary_maze(maze):
    col, row = len(maze), len(maze[0])
    plt.figure(figsize=(row, col))
    plt.imshow(maze, cmap='binary', interpolation='nearest')
    plt.axis("off")
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.show()


if __name__ == '__main__':
    A = [[1,1,1], 
         [0,1,0], 
         [1,0,1]]
    print(view_binary_maze(A))

