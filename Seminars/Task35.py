# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] -1= A[i-1]. Найдите это число

# path = 'C:/Users/Admin/Desktop/GeekBrains/IntroduceToPython/file35.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# with open ('C:/Users/Admin/Desktop/GeekBrains/IntroduceToPython/Seminars/file35.txt', 'r', encoding='utf-8') as f:
#     s = f.readline().split()

# for i in range(len(s)-1):
#     if int(s[i])+1 != int(s[i+1]):
#         print (int(s[i])+1)
    

# def func(list, element):
#     return (int(s[i])+1)

#Вариант преподавателя

n=8
with open('C:/Users/Admin/Desktop/GeekBrains/IntroduceToPython/Seminars/file35.txt', 'r', encoding = 'utf-8') as k:
    some_list = list(map(int, k.read().split()))
    for i in range(n-1):
        if some_list[i] != some_list[i+1] -1:
            print(some_list[i+1] - 1)

