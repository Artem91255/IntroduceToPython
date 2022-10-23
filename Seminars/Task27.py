# # Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# # В качестве символа-разделителя используйте пробел

# numbers = input('Введите строку из набора чисел: ')
# list = numbers.split()
# list2=[]
# for i in range(len(list)):
#     num = int(list[i])
#     list2.append(num)
# print(list2)

# min = list2[0]
# max = list2[0]

# for i in range(len(list2)):
#     if list2[i]<min:
#         min = list2[i]
#     if list2[i]>max:
#         max = list2[i]
# print(min)
# print(max)

# #Вариант одногруппников

# a = list(map(int, input().split()))# метод мар применяет инт к каждому из частей, на которые делит сплит
# print(max(a), min(a))


# вариант преподавателя

some_str = input()
some_str = some_str.split() #динамическая типизация
maxx = int(some_str[0])
minn = int(some_str[0])

for i in some_str:
    if int(i) > maxx:
        maxx = int(i)
    elif int(i) < minn:
        minn = int(i)
print(minn, maxx)

