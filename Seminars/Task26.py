# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# числа фибоначчи - первые два числа равны 0 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
# F−n = (−1)**n+1*Fn.
# Fn = F(n+2)−F(n+1).
# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# size = int(input("Задайте размер списка: "))

# list1=[]
# list2=[]
# for i in range(2):
#     list1.append(i)
#     list2.append(i)
    
# temp_number = 0
# temp_number2 = 0
# for i in range(1,size):
#     temp_number = list1[i]+ list1[i-1]
#     temp_number2 = list2[i-1] - list2[i]
#     list1.append(temp_number)
#     list2.append(temp_number2)

# list3=[]
# for i in range(size,0,-1):
#     list3.append(list2[i])
# for i in range(size+1):
#     list3.append(list1[i])

# print(list3)

# Вариант преподавателя

k = int(input())
some_list = [0] *(k*2+1) #список заполняется указанным количеством нулей
some_list[k+1] = 1
for idx in range(k+2, k*2+1):
    some_list[idx] = some_list[idx-1]+some_list[idx-2]
print(some_list)
for idx in range(k, -1, -1):
    some_list[idx] = some_list[idx+2] -some_list[idx+1]
print(some_list)




