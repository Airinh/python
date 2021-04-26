# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 15
MIN_ITEM = -5
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

count_num = {}
k = 1
num = None
for item in array:
    if item in count_num:
        count_num[item] += 1
    else:
        count_num[item] = 1
    if count_num[item] > k:
        k = count_num[item]
        num = item

if num is not None:
    print(f'Число {num} встречется чаще всего ({k} раз)')
else:
    print('В списке нет одинаковых чисел')