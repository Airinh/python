# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

SIZE = 15
MIN_ITEM = -100
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

i = 0
index = -1
for i in range(len(array)):
    if array[i] < 0 and index == -1:
        index = i
    elif array[index] < array[i] < 0:
        index = i

if index != -1:
    print(f'Максимальное отрицательное число {array[index]}, позиция в массиве - {index + 1}')
