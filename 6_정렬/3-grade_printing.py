num_students = int(input())
students = []

for i in range(num_students) :
    input_data = input().split()
    students.append( (input_data[0], input_data[1]) )

students.sort(key = lambda data : data[1])

print("students :", students)

for i in students :
    print(i[0], end= '\n')