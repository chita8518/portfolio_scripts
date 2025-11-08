from random import *

symbols = ''

print('''Добро пожаловать в генератор паролей
определите следующие параметры::
введите количество паролей для генерации''')

def find_count_of_password(count): #функция проверки значения количества паролей
    flag = True
    if count.isdigit() == False:
        flag = False
    return flag

while True:  #определяем количество паролей до тех пор, пока не получим удовлетворительное значение
    count_of_password = input()
    if find_count_of_password(count_of_password) == True:
        count_of_password = int(count_of_password)
        break
    else:
        print('Введите число, а не строку')

print('Введите длину пароля(паролей)')

while True:  #определяем количество паролей до тех пор, пока не получим удовлетворительное значение
    len_of_password = input()
    if find_count_of_password(len_of_password) == True:
        len_of_password = int(len_of_password)
        break
    else:
        print('Введите число, а не строку')

def valid_answer_check(answer):
    results = []
    valid_flag = True 
    # флаг на проверку типа данных ответа (строка)
    YES_NO_flag = 0
    if answer.isalpha() == False:
        valid_flag = False
    else:
        if answer in 'yYyesYESYesyEsyeS':
            YES_NO_flag = 1
        elif answer in 'nNnoNONonO':
            YES_NO_flag = -1
        else:
            YES_NO_flag = 0
    results.append(valid_flag)
    results.append(YES_NO_flag)
    return results

def symbols_maker(symbols_string):
    while True:
        answer = input()
        results = valid_answer_check(answer)
        if results[0] == False:
            print('Недопустимый ответ. Попробуйте ещё раз')
        elif results[0] == True:
            if results[1] == 1:
                global symbols
                symbols += symbols_string
                break
            elif results[1] == -1:
                break
            else:
                print('Недопустимый ответ. Попробуйте ещё раз')


print('Включать ли цифры 0123456789? Y(YES)/N(NO)')

symbols_maker('0123456789')

print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')

symbols_maker('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')

symbols_maker('abcdefghijklmnopqrstuvwxyz')

print('Включать ли символы !#$%&*+-=?@^_')

symbols_maker('!#$%&*+-=?@^_')

print('Исключать ли неоднозначные символы il1Lo0O?')

unusial_symbols = ['i','l','1','L','o','0','O']
symbols_list = list(symbols)
q = 0
while True:
    answer = input()
    results = valid_answer_check(answer)
    if results[0] == False:
        print('Недопустимый ответ. Попробуйте ещё раз')
    elif results[0] == True:
        if results[1] == 1:
            for q in range(len(unusial_symbols)):
                while True:
                    if unusial_symbols[q] in symbols_list:
                        symbols_list.remove(unusial_symbols[q])
                    else:
                        break
            symbols = ''.join(symbols_list)
            break
        elif results[1] == -1:
            break
        else:
            print('Недопустимый ответ. Попробуйте ещё раз')

passwords = []

error_len_symbols = False
for q in range(count_of_password):
    new_password = ''
    if len(symbols) != 0:
        for q in range (len_of_password):
            new_password += symbols[randint(0,len(symbols)-1)]
        passwords.append(new_password)
    elif len(symbols) == 0:
        error_len_symbols = True

print('')
if error_len_symbols == False:
    print(*passwords, sep = '\n')
elif error_len_symbols == True:
    print ('Пароли не могут быть сгенерированы.')

print('','Нажмите любую клавишу чтобы закрыть', sep = '\n')

input()
































# print(symbols)
