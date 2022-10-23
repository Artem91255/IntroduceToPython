# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


number = int(input('Enter number: '))
#короткая запись
print(format(number, 'b'))
#Вариант с использованием цикла
y = 0
bin_number = ""
while number>0:
    y=str(number%2)
    bin_number=y+bin_number
    number = int(number/2)
print(bin_number)


# Вариант преподавателя

a = int(input())
print(bin(a)[2:]) #Это срез

#Второй вариант
a = int(input())
b = ''
while a !=0:
    b=str(a%2)+b
    a //=2
print(b)









