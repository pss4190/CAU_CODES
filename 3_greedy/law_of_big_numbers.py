# get input values
n, m, k = map(int, input().split())
addition_array = list(map(int, input().split()))

#sort data array so that can use greedy
addition_array.sort(reverse=True)
print(addition_array)

addition_result = 0
# for i in addition_array :
