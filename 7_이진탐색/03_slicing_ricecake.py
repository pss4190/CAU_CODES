def calc_slice_cake(data_array, target, start, end) :
    if start > end :
        return None
    left_cake = 0
    mid = (start + end) // 2
    for element in data_array :
        if element > mid :
            left_cake += element - mid
    if left_cake == target :
        return mid
    elif left_cake < target :
        return calc_slice_cake(data_array, target, start, mid - 1)
    else :
        return calc_slice_cake(data_array, target, mid + 1, end)
    

def solution(n, m, array) :
    result = 0
    max_length = max(array)
    result = calc_slice_cake(array, m, 0, max_length)
    return result

print(solution(4, 6, [19,15,10,17]))