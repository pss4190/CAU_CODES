from collections import deque

maze_row, maze_col = map(int, input().split())
maze_matrix = []
for i in range(maze_row) :
    maze_matrix.append(list(map(int, input())))

print("start calculation")

mov_dirt = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def search_maze_way(current) :
    visit_counter = 0
    # insert initial coordinate
    bfs_queue = deque([current])

    while bfs_queue :
        print("queue :", bfs_queue)
        current = bfs_queue.popleft()
        current_x = current[0]
        current_y = current[1]

        print("current position :", current)
        if current_x == maze_row - 1 and current_y == maze_col - 1 :
            break

        for i in range(4) :
            next_x = current_x + mov_dirt[i][0]
            next_y = current_y + mov_dirt[i][1]

            try :
                if next_x >= 0 and next_y >= 0 and maze_matrix[next_x][next_y] == 1 :
                    bfs_queue.append((next_x, next_y))
                    maze_matrix[next_x][next_y] = maze_matrix[current_x][current_y] + 1 # visited
            except Exception :
                continue
    print("maze :")
    for i in range(len(maze_matrix)) :
        print(maze_matrix[i])
    return maze_matrix[current_x][current_y]

print("shortest length :", search_maze_way((0,0)))