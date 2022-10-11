# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# мой вариант

number = int(input('Введите число: '))
number_list=[]
for i in range(number*2+1):
    temp_number = number*-1
    number_list.append(temp_number)
    number-=1
print(number_list)

# Вариант одногруппников

number_classmates = int(input('Введите число: '))
for i in range(-number_classmates,number_classmates+1):
    print(i, end=' ')


#вариант преподавателя

n = int(input('вариант преподавателя.Введите число: '))
for i in range(-n, n):    
    print(i, end= ', ')
print(n)

#Второй вариант вывода
n2=int(input('Введите число: '))
print(*range(-n2,n2+1), sep=', ')
# знак * распаковывает range
# Второй вариант записи этой же команды
print(list(range(-n2,n2+1)), sep=', ')

