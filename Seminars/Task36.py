# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
# # Порядок элементов менять нельзя


# s = [1, 4, 5, 2, 3, 9, 8, 11,0]
# s.sort()
# begin = s[0]
# end = s[0]
# some_list = ""
# for i,j in enumerate(s):
#     if s[i]+ 1 != a[i+1]:
#         end = s[i]


# дан список интов. 
# Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны

# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"


int_list = [0, 1, 2, 3, 4, 5, 8, 9, 11]
int_list.sort()
idx = 0
new_list=[]

while idx < len(int_list):
    some_list = [int_list[idx]]
    new_idx = idx
    while new_idx + 1 != len(int_list) and int_list[new_idx] == int_list[new_idx+1] - 1:
        some_list.append(int_list[new_idx+1])
        new_idx+=1
    new_list.append(some_list)
    idx+=len(some_list)
print(new_list)
a = []
for i in new_list:
    if len(i) !=1:
        a.append(f'{i[0]}-{i[-1]}')
    else:
        a.append(f'{i[0]}')
print(*a, sep=',') #* - распаковка списка
    



