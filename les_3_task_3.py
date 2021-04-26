# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 15
MIN_ITEM = -150
MAX_ITEM = 150
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

array_1 = array
i_min = 0
i_max = 0
for i in range(len(array_1)):
    if array_1[i] < array_1[i_min]:
        i_min = i
    elif array_1[i] > array_1[i_max]:
        i_max = i

array_1[i_min], array_1[i_max] = array_1[i_max], array_1[i_min]
print(array_1)
