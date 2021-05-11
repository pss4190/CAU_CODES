def binary_search (start, end, target, data_array) :
    if start > end :
        return None
    mid = (start + end) // 2
    if data_array[mid] == target :
        return data_array[mid]
    elif data_array[mid] < target :
        return binary_search(mid + 1, end, target, data_array)
    else :
        return binary_search(start, mid - 1, target, data_array)
        

def solution(n, n_arr, m, m_arr) :
    result = []
    n_arr.sort()
    for element in m_arr :
        searched = binary_search(0, n-1, element, n_arr)
        if searched : # if searched != None
            result.append("yes")
        else :
            result.append("no")
    
    return result

print(solution(5, [8,3,7,9,2], 3, [5,7,9]))