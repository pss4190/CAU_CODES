from collections import deque

maze_row, maze_col = map(int, iinput().split())
maze_matrix = []
for i in range(maze_row) :
    maze_matrix.append(list(map(int, input())))

def search_maze_way(start) :
    bfs_queue = deque([start])
    