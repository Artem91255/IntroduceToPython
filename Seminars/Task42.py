# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
with open('file42_input.txt', 'r', encoding = 'utf-8') as k:
    string_of_elements = list(map(str,k.read()))
count = 1

with open('file42_output.txt', 'w', encoding = 'utf-8') as h:
    for i in range(len(string_of_elements)-1):
        if string_of_elements[i]==string_of_elements[i+1]:
            count+=1
        else:
            with open('file42_output.txt', 'a', encoding = 'utf-8') as j:
                j.writelines(str(count) + str(string_of_elements[i]))
            count = 1
    with open('file42_output.txt', 'a', encoding = 'utf-8') as j:
        j.writelines(str(count) + str(string_of_elements[i]))
