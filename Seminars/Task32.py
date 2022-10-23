# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list=[1,2,3,4,5,5,4,6,8,1]
list2=[]
for i in range(len(list)):
    count=0
    for j in range(len(list)):
        if list[i]==list[j]:
            count+=1
    if count==1:
        list2.append(list[i])
        
print('list2 is: '+str(list2))




some_list =[]
for i in range(len(list)): #проходимся по списку
    if list.count(i) == True: # 1означает, что элемент в списке уникален
        some_list.append(i)
print(some_list)
