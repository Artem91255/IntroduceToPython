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

price=[57.8, 46.51, 97, 20, 18.8, 24.12, 55.55, 70.5, 99.99, 100]


def add_null_and_currency(elements):
    temp_list = []
    for i in range(0, len(elements)):
        list_test_element = str(elements[i]).split(".")
        if len(list_test_element)>1:
            if int(list_test_element[1])<10:
                list_test_element[1]="0"+list_test_element[1]
                list_test_element = '.'.join(list_test_element)
                temp_list.append(list_test_element)
            else:
                temp_list.append(str(elements[i]))
        else:
            list_test_element.append("00")
            list_test_element='.'.join(list_test_element)
            temp_list.append(list_test_element)
    for i in range(0, len(elements)):
        temp_list[i] = temp_list[i].replace(".", " руб ") + " коп"

    return temp_list

def price_up(elements):
    temp_list=elements
    length = len(temp_list)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if temp_list[j] > temp_list[j + 1]:
                temp = temp_list[j]
                temp_list[j] = temp_list[j + 1]
                temp_list[j + 1] = temp

    return temp_list

print(*add_null_and_currency(price), sep = ", ")
price = price_up(price)
print(*add_null_and_currency(price), sep = ", ")
price.reverse()
print(*add_null_and_currency(price), sep = ", ")

