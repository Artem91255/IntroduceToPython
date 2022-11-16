print('hello world')
value = None
print(type(value))
a = 3
b = 1.23
print(a)
print(b)
print(type(a))
print(type(b))
value = 12345
print(value)

s = 'hello world'
print(s)
# - это знак комментария
s1 = "hello 'world"
print(s1)
s2 = 'hello "world'
print(s2)
s3 = 'hello \'world'
print(s3)
print(a,'-',b,'-',s)
print('{} - {} - {}'.format(a,b,s))
print('{1} - {2} - {0}'.format(a,b,s))
print(f'{a} - {b} - {s}')

f=True
print(f)

list = ['1','2','3']
col = ['hello', 1,2,3.5,True]
print(list)
print(col)


print('Введите а')
a = int(input())
print('Введите b')
b = int(input())
print(a, ' + ' ,b ,' = ', a+b)
print('{} {}'.format(a,b))
print(f'{a} {b}')
# Арифметические операции
# +, -, *, /, %, //, **
# **, 
# (), Сокращенные операции
# / - деление и ответ будет с дробной частью
# // - деление и ответ будет без дробной части
# ** - возведение в степень
a=123
b=321
c=a+b
print(c)
d= 1.325458
e = 3
f = round(a*b) # ответ 3.9 будет округлен до числа 4
g = round(a*b, 5) # 5 - это то количество знаков после запятой, которое требуется вывести на экран

i=3
i+=5
print(i)#Ответ - 8

a=1<4
print(a) # False

a='qwe'
b='qwe'
print(a==b) # True

a=[1,2]
b=[1,2]
print(a==b) # True

a=1<3<5<10
print(a) # True

func = 1
T = 4
x = 123

print(func<T>(x)) # False

f= 1>2 or 4<6
print(f) # True

f=[1,2,3,4]
print(f)
print(2 in f)# True - 2 есть в списке
print(not 2 in f)

is_odd = f[0] %2 ==0
# Равнозначное выражение. Предпочтительный вариант
is_odd = not f[0] % 2
print(is_odd) # False- единица число не четное

a = int(input('a = '))
b = int(input('b = '))

if a>b:  
    print(a)
else:
    print(b)

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Привет, Ильнар')
else:
    print('Привет, ', username)

# Цикл while
original = 23
inverted = 0
while original !=0:
    invertered = invertered *10 + (original %10)
    original //=10
print(invertered)


original = 23
inverted = 0
while original !=0:
    inverted = inverted *10 +(original %10)
    original //=10
else:
    print('Пожалуй')
    print('Хватит')
print(inverted)

#Цикл For

for i in 1,2,3,4,5:
    print(i**2)

list=[1,2,3,4,5]
for i in list:
    print(i**2)


# Получаем значения от нуля до девятки. 
r = range(10)
for i in r:
    print(i)


# Значения от нуля до девятки. Шаг приращения 2
for i in range(2, 10, 2):
    print(i)

# Вывод строки побуквенно
for i in 'qwe - rty':
    print(i)

#Работа со строками

text = 'съешь еще этиъ мягких французских булок'

help(text.istitle) #Получение подсказки. Чтобы выйти из блока - нажать q
print(len(text))  #Получить количество символов
print('еще' in text)  # Проверить наличие подстроки
print(text.isdigit()) # Проверить, являются ли все символы строки числами
print(text.isLower())  #Являются ли символами нижнего регистра
print(text.replace('еще', 'ЕЩЁ'))  #Замена подстроки

for c in text:
    print(c)

# text = 'съешь еще этих мягких французских булок'
# print(text[0])                c   
# print(text[1])                ъ
# print(text[len(text)])        IndexError
# print(text[len(text)-1])      к
# print(text[-5])               б
# print(text[:]), т.е (text[0:len(text)-1])               print(text)
# print(text[:2])                съ
# print(text[len(text)-2:])     ок
# print(text[2:9])              ешь ещё
# print(text[6:-18])            ещё этих мягких
# print(text[0:len(text):6])    сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

#Списки
numbers = [1,2,3,4,5]
print(numbers) # [1, 2 ,3 ,4 ,5 ]

numbers = list(range(1,6))
print(numbers) # [1, 2 ,3 ,4 ,5 ]

numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]

for i in numbers:
    i*=2
    print(i)    # [20, 4, 6, 8, 10]
print(numbers)  # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']

for e in color:
    print(e)    # red green blue

for e in colors:
    print(e*2)  # redred greengreen blueblue

colors.append('gray')
print(colors == ['red', 'greed', 'blue', 'gray'])   # True
colors.remove('red')    #del colors[0]  # удалить элемент

# Функции

def f(x):
    return x**2


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

    print(f(1))             # Целое
    print(f(2.3))           # 23
    print(f(28))            # None
    print(type(f(1)))       # str
    print(type(f(2.3)))     # int
    print(type(f(28)))      # NoneType


    