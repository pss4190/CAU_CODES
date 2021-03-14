def array_print(value) :
    for i in range(0, len(input_value)) :
        print(chr(65 + value[i]), end='')

alphabet = [i for i in range(0,26)]
input_value = [22, 8, 6, 24, 21, 12, 23, 2]
print("length of input : ", len(input_value))
for i in range(1, 26) :
    result_vaule = [0 for _ in range(0, len(input_value))]
    for j in range(0, len(input_value)) :
        result_vaule[j] = (input_value[j] - i) % 26
    print(result_vaule)
    print(i, " = ", end='')
    array_print(result_vaule)
    print()