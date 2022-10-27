# Напишите программу, удаляющую из текста все слова, содержащие "абв"


# text = input()
# text = text.split()

# def x(i):
#     return 'абв' not in i

# new_text = list(filter(lambda x: 'abc' not in x, text))
# print(new_text)

#______________________________________________________________________________________________________________________
# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом"" 

# import random
# import time

# sum = 2021
# print("ИГРА С КОНФЕТАМИ")
# time.sleep(1)
# print("Выбери, кто с тобой будет играть: человек или бот?")
# time.sleep(1)

# while(True):
#     player2_choose = input('Введи слово человек или бот: ')
#          #игра с человеком
        
#     if player2_choose =='человек':
#         while (True):
#     #Игрок 1
#             print('')
#             print('Ход игрока номер 1. Какое количество конфет ты возьмешь? Максимальное количество 28 шт:  ')
#             while (True):
#                 first_person_move = int(input('Напиши сколько конфет хочешь взять: '))
#                 if first_person_move<1 or first_person_move>28:
#                     print('Ты не можешь взять столько конфет. Ты можешь взять не больше 28 штук и не менее 1 штуки. Попробуй еще раз')
#                 else:
#                     break
#             sum-=first_person_move
#             print('Количество конфет, взятых игроком 1: ' + str(first_person_move) + ' Осталось конфет: ' + str(sum))
#             if sum<=0:
#                 print('Игра окончена. Победил игрок номер 1')
#                 break

#                 #Игрок 2
#             print('')
#             print('Ход игрока номер 2. Какое количество конфет ты возьмешь? Максимальное количество 28 шт:  ')
#             while(True):
#                 second_person_move = int(input('Напиши сколько конфет хочешь взять: '))
#                 if second_person_move<1 or second_person_move>28:
#                     print('Ты не можешь взять столько конфет. Ты можешь взять не больше 28 штук и не менее 1 штуки. Попробуй еще раз')
#                 else:
#                     break
#             sum-=second_person_move
#             print('Количество конфет, взятых игроком 2: ' + str(second_person_move) + ' Осталось конфет: ' + str(sum))
#             if sum<=0:
#                 print('Игра окончена. Победил игрок номер 2')
#                 break
#         break

#         #Игра с ботом
#     elif player2_choose== 'бот':
#         while(True):    
#             print('')
#             print('Ход игрока номер 1. Какое количество конфет ты возьмешь? Максимальное количество 28 шт:  ')
#             while (True):
#                 first_person_move = int(input('Напиши сколько конфет хочешь взять: '))
#                 if first_person_move<1 or first_person_move>28:
#                     print('Ты не можешь взять столько конфет. Ты можешь взять не больше 28 штук и не менее 1 штуки. Попробуй еще раз')
#                 else:
#                     break
#             sum-=first_person_move
#             print('Количество конфет, взятых игроком 1: ' + str(first_person_move) + ' Осталось конфет: ' + str(sum))
#             if sum<=0:
#                 print('Игра окончена. Победил игрок номер 1')
#                 break

#                 #Игрок 2
#             print('')
#             print('Ход бота.')
#             time.sleep(1)
#             number_if_speech = random.randint(0,2)
#             if number_if_speech==0:
#                 print('Бот: анализирую твой ход, человек. Сейчас что-нибудь придумаю...')
#                 time.sleep(2)
#                 print('Бот: Как тебе это?')
#                 time.sleep(1)
#             elif number_if_speech==1:
#                 print('Бот: Хитрый ход. Думаешь меня подловить? Тут нужно хорошенько подумать, сколько взять конфет')
#                 time.sleep(3)
#                 print('Бот: Придумал!! Как тебе это?')
#                 time.sleep(1)
#             else:
#                 print('Бот: Ахах, ну и ход! Играешь как кожаный мешок. Ах да, вспомнил, ты он и есть! Если бы ты знал, какую ошибку ты совершил...')
#                 time.sleep(2)
#                 print('Бот: Лучше бы я не придумал. Смотри!')
#                 time.sleep(1)

#             while(True):
#                 if sum>= 28:
#                     second_person_move = random.randint(1,28)
#                     time.sleep(0.5)
#                 else:
#                     second_person_move = random.randint(1,sum)
#                 if second_person_move<1 or second_person_move>28:
#                     print('Ты не можешь взять столько конфет. Ты можешь взять не больше 28 штук. Попробуй еще раз')
#                 else:
#                     break
#             sum-=second_person_move
#             print('Количество конфет, взятых ботом: ' + str(second_person_move) + ' Осталось конфет: ' + str(sum))
#             if sum<=0:
#                 print('Игра окончена. Победил бот')
#                 time.sleep(3)
#                 print('Бот: Не плачь и смирись с поражением, кусок мяса. Когда-нибудь тебе обязательно повезет.')
#                 break
#         break


#     else:
#         print('Неправильный ввод. Попробуй еще раз')

#______________________________________________________________________________________________________________________

# Создайте программу для игры в ""Крестики-нолики""


# mas = [[' ', '1', '2', '3'],['1', '-', '-', '-'], ['2', '-', '-', '-'], ['3', '-', '-', '-']]

# count = 1
# print(' ')
# print('ИГРА КРЕСТИКИ - НОЛИКИ')
# print(' ')
# print('ПРАВИЛА ИГРЫ: игрок 1 ходит первым и играет за крестики, игрок 2 за нолики. Привет ввода: 1-1-x \n Используемые значения: строчные буквы x и o на английской раскладке')
# for i in range(0, len(mas)):
#     for i2 in range(0, len(mas[i])):
#         print(mas[i][i2], end=' ')
#     print()



# while (True):
#     #проверка по горизонтали
#     if mas[1][1]=='x' and mas[1][2]=='x' and mas[1][3]=='x':
#         print('Игра окончена. Победил игрок номер 1')
#         break
#     elif mas[2][1]=='x' and mas[2][2]=='x' and mas[2][3]=='x':
#         print('Игра окончена. Победил игрок номер 1')
#         break
#     elif mas[3][1]=='x' and mas[3][2]=='x' and mas[3][3]=='x':
#         print('Игра окончена. Победил игрок номер 1')
#         break
#         #проверка по вертикали
#     elif mas[1][1]=='x' and mas[2][1]=='x' and mas[3][1]=='x':
#         print('Игра окончена. Победил игрок номер 1')
#         break
#     elif mas[1][2]=='x' and mas[2][2]=='x' and mas[3][2]=='x':
#         print('Игра окончена. Победил игрок номер 1')
#         break
#     elif mas[1][3]=='x' and mas[2][3]=='x' and mas[3][3]=='x':
#         print('Игра окончена. Победил игрок номер 1')
#         break
#       #проверка по диагонали
#     elif mas[1][1]=='x' and mas[2][2]=='x' and mas[3][3]=='x':
#         print('Игра окончена. Победил игрок номер 1')
#         break
#     elif mas[3][1]=='x' and mas[2][2]=='x' and mas[1][3]=='x':
#         print('Игра окончена. Победил игрок номер 1')
#         break
#      #то же самое для второго игрока
#      #проверка по горизонтали
#     elif mas[1][1]=='o' and mas[1][2]=='o' and mas[1][3]=='o':
#         print('Игра окончена. Победил игрок номер 2')
#         break
#     elif mas[2][1]=='o' and mas[2][2]=='o' and mas[2][3]=='o':
#         print('Игра окончена. Победил игрок номер 2')
#         break
#     elif mas[3][1]=='o' and mas[3][2]=='o' and mas[3][3]=='o':
#         print('Игра окончена. Победил игрок номер 2')
#         break
#         #проверка по вертикали
#     elif mas[1][1]=='o' and mas[2][1]=='o' and mas[3][1]=='o':
#         print('Игра окончена. Победил игрок номер 2')
#         break
#     elif mas[1][2]=='o' and mas[2][2]=='o' and mas[3][2]=='o':
#         print('Игра окончена. Победил игрок номер 2')
#         break
#     elif mas[1][3]=='o' and mas[2][3]=='o' and mas[3][3]=='o':
#         print('Игра окончена. Победил игрок номер 2')
#         break
#       #проверка по диагонали
#     elif mas[1][1]=='o' and mas[2][2]=='o' and mas[3][3]=='o':
#         print('Игра окончена. Победил игрок номер 2')
#         break
#     elif mas[3][1]=='o' and mas[2][2]=='o' and mas[1][3]=='o':
#         print('Игра окончена. Победил игрок номер 2')
#         break
#     elif count==10:
#         print('Игра окончена. Ничья')
#         break

    
#     #Ввод значения в конкретную ячейку
#     if count%2 != 0:
#         print("Ход игрока номер 1")
#     else:
#         print("Ход игрока номер 2")
#     while(True):
#         m = input("Введите значение в формате номер строки-номер столбца-значение(x или o на английской раскладке): ").split('-')
#         if m.__contains__('x') or m.__contains__('o'):
#             row = int(m[0])
#             column = int(m[1])
#             if mas[row][column] == '-':
#                 count+=1
#                 break
#             else:
#                 print('указанная ячейка уже заполнена, повторите ввод.')
#         else:
#             print("Некорректное значение. Повторите ввод.")


#     #Вывод вдумерного массива на экран
#     mas[row][column] = m[2]
#     for i in range(0, len(mas)):
#         for i2 in range(0, len(mas[i])):
#             print(mas[i][i2], end=' ')
#         print()

#______________________________________________________________________________________________________________________
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
