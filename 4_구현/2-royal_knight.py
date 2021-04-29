import time
start_time = time.time()

place = str(input())
field_col = int(ord(place[0])-97)
field_row = int(place[1])

col_mov = [2, -2, 2, -2, 1, -1, 1, -1]
row_mov = [1, 1, -1, -1, 2, 2, -2, -2]

result = 0

for i in range(8) :
    if 0 <= field_col + col_mov[i] <= 7 and 0 <= field_row + row_mov[i] <= 7 :
        result += 1
    else : 
        continue

print(result)

end_time = time.time()

print("time : ", str((end_time - start_time)), "s")