#Задайте список из N элементов, заполненных числами из промежутка [-N,N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
# Реализуйте алгоритм перемешивания списка



import random


count_of_elements = int(input('Какое количество элементов будет в списке: '))
elements = []
for i in range(count_of_elements*2+1):
    temp_number = count_of_elements * -1
    elements.append(temp_number)
    count_of_elements -=1
print(elements)



mult = 1

f2 = open('C:\\Users\\Admin\\Desktop\\GeekBrains\\IntroduceToPython\\Seminars\\file.txt', 'r')
l = [line.strip() for line in f2]
f2.close

result = [int(item) for item in l]





#Второй вариант чтения данных из файла и внесением из в список
# data=[]
# with open("C:\\Users\\Admin\\Desktop\\GeekBrains\\IntroduceToPython\\Seminars\\file.txt") as f:
#     for line in f:
#         data.append([int(x) for x in line.split()])
# print(data)

for i in range(len(result)):
   x = result[i]
   mult = mult* elements[x]

print(mult)


#Реализуем алгоритм перемешивания списка


shuffle_elements =elements
for i in range(len(shuffle_elements)):
    temp = 0
    random_number = random.randint(0,len(shuffle_elements)-1)
    temp = shuffle_elements[i]
    shuffle_elements[i] = shuffle_elements[random_number]
    shuffle_elements[random_number] = temp
print(shuffle_elements)

    

