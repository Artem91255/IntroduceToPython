# Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:\
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#разделяем элемент списка на символы
def str_to_chars(start_str):
    chars1=[]
    for i in range(0, len(start_str)):
        if len(start_str)>1:
            if start_str[i].__contains__('+')or start_str[i].__contains__('-'):
                for j in range(0, len(start_str[i])):
                    chars1 = [char for s in start_str[i] for char in s]

        elif start_str[i].isdigit()==True:
            for j in range(0, len(start_str[i])):
                chars1 = [char for s in start_str[i] for char in s]

        else:
            for j in range(0, len(start_str[i])):
                chars1 = [char for s in start_str[i] for char in s]

    return chars1
#добавляем ноль
def add_null(chars):
    chars2=[]
    for i in range(0, len(chars)):
        if len(chars)==2:
            if chars[i]=="+" or chars[i]=="-":
                chars2.append(chars[i])
                chars2.append("0")
            else:
                chars2.append(chars[i])

        elif len(chars)==1:
            chars2.append("0")
            chars2.append(chars[i])
        else:
            chars2.append(chars[i])

    final_str ="".join(chars2)

    return final_str


list = ['в', '12', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


list2=[]

for i in range (0, len(list)):

    for k in range(0,10):
        if list[i].__contains__(str(k)):
            list2.append("\"")
            temp = [list[i]]
            res1 = str_to_chars(temp)
            res2 = add_null(res1)
            list2.append(res2)
            list2.append("\"")
            break
    else:
        list2.append(list[i])

print(list2)




