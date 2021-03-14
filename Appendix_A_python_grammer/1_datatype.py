# 1. float round function
print("1. float round function")

a = 0.3 + 0.6
print(round(a, 3)) # round about 2nd float point 
# shows 0.9

# 2. special calculation
print("2. special calculation")

b = 2
c = 12

print(c // b) # only quotient
# shows 6
print(c ** b) # 12 ^ 2
# shows 144

# 3. List
print("3. list")

d = [1,2,3,4]
# about empty initializing
e = list()
f = []
# about 0 initializing
g = [0] * b

print(d)
print(e)
print(f)
print(g)

# 4. indexing and slicing of List
print("4. indexing and slicing of List")

h = [i for i in range(1, 10)]

print(h)
print(h[-1]) # shows 10

# indexing from 1st to (4-1)th position
print(h[1:4]) # shows [2, 3, 4]

# 5. list comprehention (initializing)
print("5. list comprehention (initializing)")

i = [ num * num for num in range(1, 10)]
print(i) # shows [1, 4, 9, 16, 25, 36, 49, 64, 81]

j = [ num for num in range(20) if num % 2 == 1]
print(j) # shows [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

array_row = 3
array_column = 4
# use '_' in iteration if not need auto incresement variable
k = [[0] * array_column for _ in range(array_row)] # shows 3 * 4 dimension array list
print(k)

l = [1, 5, 3, 2]
print("regular : ", l)

# append : O(1)
l.append(2)
print("append : ", l)

l.sort()
print("ascending : ", l)

l.sort(reverse=True)
print("decending : ", l)

l.reverse()
print("reverse : ", l)

# insert : O(n)
l.insert(2, 12)
print("insert 12 into index 2 : ", l)

print("number of \'3\' in list : ", l.count(3))

# remove : O(n)
l.remove(3)
print("remove value which is \'3\' : ", l)

# 6. 