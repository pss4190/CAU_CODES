array_init = [i for i in range(1, 10)]
result_exclution = [3,5,6,7]
print(array_init)
result = [i for i in array_init if i not in result_exclution]
print(result)

firm_tuple = (i for i in range(1,10))
firm_tuple_print_test = (1,2,3)
print(firm_tuple_print_test)
print(firm_tuple)

test_dictionary = dict()
test_dictionary["사과"] = 'apple'
test_dictionary["포도"] = 'grape'
test_dictionary["바나나"] = 'banana'

print(test_dictionary)
print(test_dictionary.keys())
print(test_dictionary.values())

set_test = {1,2,3,4,5}
set_test.add(100)
set_test.remove(2)
set_test.update([12,15])

def accumulation(start, end) :
    result = 0
    for i in range(start, end+1) :
        result += i
    return result

print(accumulation(1, 10))
print((lambda a, b : a * b)(1, 10))

a = "global_a"

def globalization_test(local_a, local_b) :
    global a
    print(a)
    print(local_b)

globalization_test("local_a", "local_b")