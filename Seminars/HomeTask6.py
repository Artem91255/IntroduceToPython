# Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:\
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#разделяем элемент списка на символы
# def str_to_chars(start_str):
#     chars1=[]
#     for i in range(0, len(start_str)):
#         if len(start_str)>1:
#             if start_str[i].__contains__('+')or start_str[i].__contains__('-'):
#                 for j in range(0, len(start_str[i])):
#                     chars1 = [char for s in start_str[i] for char in s]
#
#         elif start_str[i].isdigit()==True:
#             for j in range(0, len(start_str[i])):
#                 chars1 = [char for s in start_str[i] for char in s]
#
#         else:
#             for j in range(0, len(start_str[i])):
#                 chars1 = [char for s in start_str[i] for char in s]
#
#     return chars1
# #добавляем ноль
# def add_null(chars):
#     chars2=[]
#     for i in range(0, len(chars)):
#         if len(chars)==2:
#             if chars[i]=="+" or chars[i]=="-":
#                 chars2.append(chars[i])
#                 chars2.append("0")
#             else:
#                 chars2.append(chars[i])
#
#         elif len(chars)==1:
#             chars2.append("0")
#             chars2.append(chars[i])
#         else:
#             chars2.append(chars[i])
#
#     final_str ="".join(chars2)
#
#     return final_str
#
#
# list = ['в', '12', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
#
# list2=[]
#
# for i in range (0, len(list)):
#
#     for k in range(0,10):
#         if list[i].__contains__(str(k)):
#             list2.append("\"")
#             temp = [list[i]]
#             res1 = str_to_chars(temp)
#             res2 = add_null(res1)
#             list2.append(res2)
#             list2.append("\"")
#             break
#     else:
#         list2.append(list[i])
#
# print(list2)

# ______________________________________________________________________________________________


# Дан список, содержащий искажённые данные с должностями и именами сотрудников: \
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
# Подумать, как получить имена сотрудников из элементов списка,
# как привести их к корректному виду. Можно ли при этом не создавать новый список?


# test_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# удаляем лишние слова
# def del_words(test_string):
#     for i in range(len(test_string), 0, -1):
#         if test_string[i - 1] == " ":
#             res_str = test_string[:0] + test_string[i:]
#             break
#     return res_str
#
# for i in range(0, len(test_list)):
#     test_list[i]=del_words(test_list[i])
#     test_list[i]=test_list[i].capitalize()
#     print("Привет, "+ test_list[i] + "!")

# ______________________________________________________________________________________________


# Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

# price=[57.8, 46.51, 97, 20, 18.8, 24.12, 55.55, 70.5, 99.99, 100]
#
#
# def add_null_and_currency(elements):
#     temp_list = []
#     for i in range(0, len(elements)):
#         list_test_element = str(elements[i]).split(".")
#         if len(list_test_element)>1:
#             if int(list_test_element[1])<10:
#                 list_test_element[1]="0"+list_test_element[1]
#                 list_test_element = '.'.join(list_test_element)
#                 temp_list.append(list_test_element)
#             else:
#                 temp_list.append(str(elements[i]))
#         else:
#             list_test_element.append("00")
#             list_test_element='.'.join(list_test_element)
#             temp_list.append(list_test_element)
#     for i in range(0, len(elements)):
#         temp_list[i] = temp_list[i].replace(".", " руб ") + " коп"
#
#     return temp_list
#
# def price_up(elements):
#     temp_list=elements
#     length = len(temp_list)
#     for i in range(0, length):
#         for j in range(0, length - i - 1):
#             if temp_list[j] > temp_list[j + 1]:
#                 temp = temp_list[j]
#                 temp_list[j] = temp_list[j + 1]
#                 temp_list[j + 1] = temp
#
#     return temp_list
#
# print(*add_null_and_currency(price), sep = ", ")
# price = price_up(price)
# print(*add_null_and_currency(price), sep = ", ")
# price.reverse()
# print(*add_null_and_currency(price), sep = ", ")


