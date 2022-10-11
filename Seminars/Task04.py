# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа

#мой вариант

number_start = float(input('Введите дробное число: '))
number2 = int(number_start/1)
print(number2)
number3 = number_start-number2
print(number3)
number4 = int(number3*10.0)
print(number4)


#вариант одногруппников

number1 = input('Введите дробное число: ')
if '.' not in number1:
    print('no')
else:
    num = (float(number1)*10)%10
    print(int(num))


#вариант преподавателя

n = float(input('Введите дробное число: '))
if n %1==0:
    print('no')
else:
    print((int(n*10)%10))

#Второй вариант от преподавателя. НАходим индекс точки и сделующий элемент после точки выводим на экран

n2 = input('Введите дробное число: ')
if '.' in n2:
    index_t = n2.find('.')
    print(n2[index_t+1])
else:
    print('нет')