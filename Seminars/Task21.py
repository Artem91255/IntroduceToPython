# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит,что ее нет

# str.count(sub[, start[, end]])
# Параметры:
# sub - str, строка или символ;
# start - int, индекс начала поиска, по умолчанию 0, необязательно;
# end - int, конец, индекс конца поиска, по умолчанию len(str), необязательно.

a=[]
n=int(input())
for i in range(n):
    a.append(input())
find_str = input()
count=0
for el in range(len(a)):
    if a[el] == find_str:
        count+=1
    if count==2:
        print(el)
        break
else:
    print(-1)


first = a.index(find_str)
second = a.index(find_str, first+1)
print(second)
#find работает только со строчкой. Если мы ищем элемент в строке, а не в списке
