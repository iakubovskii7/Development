from typing import List, Tuple

PATH = "ererer/erer"

filepath = PATH + "/" + "eojket"
filepath = f"{PATH}/sdgsgeg"


def my_func(a, b):
    """
    Function is
    :param a:
    :param b:
    :return:
    """
    c = a + b
    return c

list = [1,2,3]

list[0]
list[-1]


for i in range(5):
    print(i)


list = [1,2,3]
list.remove(1)
print(list)

a: int = 1
a = 5.124

import pandas as pd

def my_func(a: int, b: List[int]) -> Tuple:
    c = a + b
    return c

a = 1
print(a)
a = 1
b = a + 2
print(a)

[1,2,3, 'sfsdf', 'arawr', 2.9, 2.99234]

list1 = [1, 2, 3]

list1.append(10)
print(list1[1])
print(list1)


list1[1]
list1
my_list = [1, 2, 3]
my_tuple = tuple([1, 2, 3])

print(my_list)
print(my_tuple)

my_set = set([1, 2, 3, 2, 3, 1, 10])
print(my_set)

len(set(my_list))

my_list = [1,2,3,123123123,213123123,325252352,2352351,12,12,12]

my_dict = {"key1": 1, "key2": 2}

my_dict['key1']

my_dict['key2']

list_fio = ['Олег Олегович', "Антон Антоныч"]
dict_fio = {i: len(i) for i in list_fio}

[i for i in range(10)]

dict_fio.values()
dict_fio.items()

my_list_classic = []
for i in range(10):
    if i % 2 == 0:
        my_list_classic.append(i + 1)
    else:
        my_list_classic.append(i - 1)

my_list_pythonic = [i+1 if i % 2 == 0 else i-1 for i in range(10)]

assert my_list_classic == my_list_pythonic

my_new_dict = {'key1': 1,
               'key2': [1,23,3],
               "key3": {
                   "key31": {
                       "key311": 1
                   },
                   "key32": 2
               }}

my_new_dict['key3']['key31']['key311']

squares = {x: x*x for x in range(6)}

{x: x*x for x in range(11) if x % 2 == 1}
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
{k: v for k, v in a_dict.items() if v <= 2}

my_list = [1,2,3,10,1.0, 2]

[i*2 for i in my_list]


new_my_list = list(map(lambda x: x * 2 if x % 2 == 0 else x, my_list))
new_list = []
for i in new_my_list:
    if i % 2 == 0:
        new_list.append(i*2)
    else:
        new_list.append(i)


def my_func(i):
    if i % 2 == 0:
        new_list.append(i * 2)
    else:
        new_list.append(i)
    return i


list(map(my_func, my_list))





