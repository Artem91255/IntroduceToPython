# Напишите программу, удаляющую из текста все слова, содержащие "абв"


text = input()
text = text.split()# теперь текст мы преобразовали в список
# new_text = ''
# for i in text:
#     if 'abc' not in i:
#         new_text +=i + ' '
# print(new_text)

def x(i):
    return 'абв' not in i

#три равнозначные записи
new_text = list(filter(lambda x: 'abc' not in x, text))
print(new_text)
# new_text = list(filter(x, text))
# print(new_text)
# new_text = list(filter(lambda i:'abc' not in i, text))

print(new_text)


