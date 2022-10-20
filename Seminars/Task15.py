# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

b = int(input('Введите число: '))
mult = 1
list=[]
for i in range(1,b+1):
    mult = mult*i
    list.append(mult)
print(list)

#вариант от преподавателя

n = int(input())
some_list = [1]
fact =1
for i in range(2,n+1):
    fact *=i
    some_list.append(fact)
print(some_list)



  
    
