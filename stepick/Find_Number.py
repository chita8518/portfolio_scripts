from random import *

def is_valid(answer):
    flag = 0
    if answer.isdigit():
        flag = 1
    else:
        if answer == 'exit':
            flag = 2
        else:
            flag = 3
    return flag
        
x = randint(1,100) 

print('Добро пожаловать в числовую угадайку!')
print('Угадайте и введите число от 1 до 100 или введите "exit" для завершения программы.')

while True:
    answer = input()
    flag = is_valid(answer)
    if flag == 2:
        break
    if flag == 3:
        print('Нужно ввести число, а не белиберду')
    elif flag == 1:
        if float(answer) in range (1,101):
            if float(answer) == x:
                print('Верно, ты угадал! Поздравляю!')
                break
            else:
                print('Неа, ты не угадал. Поробуй ещё раз.')
        else:
            print('В диапазоне от 1 до 100! будь внимательнее')
