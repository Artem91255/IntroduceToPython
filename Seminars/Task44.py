# Дан список, содержащий искажённые данные с должностями и именами сотрудников: \
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
# Подумать, как получить имена сотрудников из элементов списка,
# как привести их к корректному виду. Можно ли при этом не создавать новый список?


# list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# new_list=[]
# for i in range(0,len(list)):
#     list2 = list[i].split(" ")
#     new_list.append(list2[len(list2)-1])
#
# print(new_list)
#
# for i in range(0, len(new_list)):
#     new_list[i] = new_list[i].capitalize()
#
# print(new_list)
# for i in range(0, len(new_list)):
#     print("Привет "+ new_list[i] + "!")








test_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(test_list)
print()
# удаляем лишние слова
def del_words(test_string):
    for i in range(len(test_string), 0, -1):
        if test_string[i - 1] == " ":
            res_str = test_string[:0] + test_string[i:]
            break
    return res_str

for i in range(0, len(test_list)):
    test_list[i]=del_words(test_list[i])
    test_list[i]=test_list[i].capitalize()
    print("Привет, "+ test_list[i] + "!")







