array_length, max_change = map(int, input().split())
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

print("start")

array_A.sort()
array_B.sort(reverse=True)

for i in range(max_change) :
    if(array_A[i] < array_B[i]) :
        # use swap function of python
        array_A[i], array_B[i] = array_B[i], array_A[i]

summation = 0
for num in array_A :
    summation += num

print(summation)