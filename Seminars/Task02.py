#Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них

numbers = []
print('Введите 5 чисел')
size = 5
for i in range(size):
    a=int(input())
    numbers.append(a) # добавление элемента в список

max_number1 = 0
for i in range(len(numbers)): # Для указания конечного числа счетчика нужно обязательно писать range и в скобках указывать число
    if numbers[i] >max_number1:
        max_number1 = numbers[i]
    
#Второй вариант
max_number2 = max(numbers)
#

print(f'Первый вариант нахождения максимального числа в списке: {max_number1}')
print(f'Второй вариант нахождения максимального числа в списке:', max_number2)

#Более лаконичный вариант записи. метод split делает из строки список

list1 = map(int, input('Введите числа через пробел: ').split()) # map - приводить к определенному типу данных вводимые символы. Тип данных указывается в скобках
max_number3 = max(list1)
print(f'Третий вариант нахождения максимального числа в списке:', max_number3)

# Вариант преподавателя номер 1
print('Вариант от преподавателя номер 1. Введи числа через enter: ')
teacher_number = int(input())
maxx = teacher_number
for _ in range(4): # Нижнее подчеркивание мы ставим тогда, когда в цикле эта переменная никак не используется. 
    temp_number = int(input())
    if temp_number>maxx:
        maxx = temp_number

print('Четверный вариант нахождения максимального числа: '+str(maxx))

# Вариант от преподавателя номер 2

some_list = []
for _ in range(5):
    number = int(input())
    some_list.append(number)
max_number_in_list = some_list[0]
for element in some_list: #переменная element при каждой итерации принимает определенное значени указанного списка
    if element > max_number_in_list:
        max_number_in_list = element
print('Пятый вариант нахождения максимального числа: '+str(max_number_in_list))


# Вариант от преподавателя номер 3

print(max(map(int, input('Самый короткий код \n Введи последовательность чисел через пробел: ').split())))
