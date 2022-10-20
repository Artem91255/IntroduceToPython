# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора всевдослучайных чисел

import time

random_number = str(time.time()).split('.')[1]
random_list =[]

for _ in range(int(str(time.time()).split('.')[1])%10):
    item1= int((str(time.time()).split('.')[1]))%10
    random_list.append(item1)
    time.sleep(0.00001)
print(random_list)