#Для натурального n создать словать индекс значение, состоящий из последовательности 3n+1

n = int(input('Введите число: '))

for i in range(1,n-1):
    print('{}:{}'.format(i,3*i+1), end= ", ")
else:
    print('{}:{}'.format(n,3*n+1))

#Вариант одногруппников

N = int(input('Введите число: '))
array = []
for i in range(1,N+1):
    array.append(f'{i}: '+ str(3*i+1))

print(array)


#Вариант от преподавателя

a = int(input('Введите число: '))
print('{', end='')
for i in range(1,n):
    print(f'{i}:{3*i+1}', end=', ')
print(f'{a}:{3*n+1}',end='}')
