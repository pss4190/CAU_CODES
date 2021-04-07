number_of_inputs = int(input())
array = []
for _ in range(number_of_inputs) :
    array.append(int(input()))

array.sort(reverse=True)

for i in array :
    print(i, end=' ')