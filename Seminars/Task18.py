# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)



first_list = [1, 2, 3, 2, 0]
second_list = [5, 1, 2, 7, 3, 2]
third_list = []
for i in range(0, len(first_list)):
    for k in range(0, len(second_list)):
        if first_list[i] == second_list[k]:
            third_list.append(first_list[i])
            k+=1
            break
print(third_list)

