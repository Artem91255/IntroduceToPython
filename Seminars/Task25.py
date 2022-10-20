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
prefix = "-"
comb=""
while number>0:
    y=str(number%2)
    bin_number=y+bin_number
    number = int(number/2)
print(bin_number)






