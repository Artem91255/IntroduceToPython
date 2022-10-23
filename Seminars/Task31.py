# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input())
list = []
for i in range(2, n+1):
    if n % i == 0:
        for k in range(2, i // 2 +1):
            if i%k ==0:
                break
                
        else:
            list.append(i)
print(list)


b = int(input())
some_list = []
a = 2
while a * a <= b:
    if n % a == 0:
        some_list.append(a)
        b //= a
    else:
        a += 1
if b > 1:
    some_list.append(b)

print(some_list)
  
