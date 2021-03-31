import time

dirt_movement = [(0,1), (-1,0), (0,-1), (1, 0)]
# dirt_movement = [(-1,0), (0, 1), (1, 0), (0, -1)]

frame_row, frame_col = map(int, input().split())
frame_matrix = []
for i in range(frame_row) :
    frame_matrix.append(list(map(int, input())))

result = 0

start_time = time.time()

def check_frame(dirt, current) :
    frame_matrix[current[0]][current[1]] = 1
    temp_row = current[0] + dirt_movement[dirt][0]
    temp_col = current[1] + dirt_movement[dirt][1]
    
    if temp_row >= 0 and temp_col >= 0 :
        try :
            # if there is way to go
            if frame_matrix[temp_row][temp_col] == 0 :
                for i in range(4) :
                    check_frame(i, (temp_row, temp_col))
            # if there is no way to go foward
            else :
                return 0
        except IndexError : # can't handle negative number due to the list indexing on python.
            return 1
    # if above all done (means, all sequences are done), return 1 so can add to result.
    return 1

def making_icecream() :
    global result
    for row_num in range(frame_row) :
        for col_num in range(frame_col) :
            if frame_matrix[row_num][col_num] == 0 :
                result += check_frame(0, (row_num, col_num))

making_icecream()
print(result)

end_time = time.time()
print("response time :", str((end_time-start_time)), "ms")
