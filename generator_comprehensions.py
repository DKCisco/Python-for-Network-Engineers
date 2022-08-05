my_list = []

for num in range(5, 100):
    my_list.append(num * num)

print(my_list)

my_list_comp = [num * num for num in range(5, 100)]

print(my_list)

my_gen_comp = (num * num for num in range(5, 100))

print(my_gen_comp)

import sys

print(sys.getsizeof(my_list_comp))
print(sys.getsizeof(my_gen_comp))

my_list_comp2 = [num * num for num in range(1, 5000000)]

print(my_list_comp2)
print(sys.getsizeof(my_list_comp2))

my_gen_comp2 = (num * num for num in range(1, 5000000))
print(my_gen_comp2)
print(sys.getsizeof(my_gen_comp2))

for num in my_gen_comp2:
    print(num)