import time

map_row, map_col = map(int, input().split())
my_row, my_col, dirt = map(int, input().split())
game_map = []
for i in range(map_row) :
    game_map.append(list(map(int, input().split())))

visited = [[0] * map_col for _ in range(map_row)]

visited[my_row][my_col] = 1

dirt_movement = [(-1,0), (0, 1), (1, 0), (0, -1)]
dirt_count = 0
result = 0
while True :
    temp_dirt = (dirt - 1) % 4
    temp_row_mov = my_row + dirt_movement[temp_dirt][0]
    temp_col_mov = my_col + dirt_movement[temp_dirt][1]

    # not sea
    if game_map[temp_row_mov][temp_col_mov] == 0 :
        # if there is way, move to there
        if visited[temp_row_mov][temp_col_mov] == 0 :
            my_row = temp_row_mov
            my_col = temp_col_mov
            dirt = temp_dirt
            dirt_count = 0
            result += 1
            visited[my_row][my_col] = 1
            continue
        # turn to next dirt
        else :
            back_mov_row = my_row - dirt_movement[dirt][0]
            back_mov_col = my_col - dirt_movement[dirt][1]
            if dirt_count == 4 :
                # if there is way to go back
                if visited[back_mov_row][back_mov_col] == 0 :
                    my_row = back_mov_row
                    my_col = back_mov_col
                    dirt_count = 0
                    result += 1
                    visited[my_row][my_col] = 1
                    continue
                # if there is no way to go back
                else :
                    break
            # change dirt
            dirt = (dirt - 1) % 4
            dirt_count += 1
            continue
    # sea
    else :
        if dirt_count == 4 :
            if visited[back_mov_row][back_mov_col] == 1 or game_map[back_mov_row][back_mov_col] :
                break
        dirt = (dirt - 1) % 4
        dirt_count += 1
        continue

print("result :", result)