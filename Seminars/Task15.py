# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

b = int(input('Введите число: '))
mult = 1
list=[]
for i in range(1,b+1):
    mult = mult*i
    list.append(mult)
print(list)

  
    
