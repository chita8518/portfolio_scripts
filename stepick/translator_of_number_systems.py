numbers_list = ['0','1','2','3','4','5','6','7','8','9',
                'A','B','C','D','E','F','G','H','I','J',
                'K','L','M','N','O','P','Q','R','S','T',
                'U','V','W','X','Y','Z']

print('введите число')

flag1 = True
flag2 = True

# считывание числа
while flag1:
    number = list(input())
    if number == []:
        print('вы не ввели число. введите число')
        continue
    elif number != []:
        for q in range (len(number)):
            if number[q] not in numbers_list:
                flag2 = False
                break
    if flag2 == False:
        print('введите число ещё раз')
        flag2 = True
    elif flag2 == True:
        flag1 = False

# присвоение каждому символу числа числовое значение в 10-чной системе счисления
for q in range (len(number)):
    if number[q] in numbers_list:
        if number[q].isdigit() == True:
            number[q] = int(number[q])
        elif number[q].isalpha() and number[q] in numbers_list:
            number[q] = numbers_list.index(number[q])

limit_number_system = int(max(number))

print('введите систему исчисления этого числа (до 36-значной системы исчисления)')

# считывание основания системы счисления
while True:
    number_system_1 = int(input())
    if number_system_1<=limit_number_system or number_system_1>36 or number_system_1<1:
        print('введите систему счисления ещё раз')
    elif number_system_1>limit_number_system and number_system_1<=36 and number_system_1>0:
        break

print('введите интересующую вас систему исчисления (до 36-значной системы исчисления)')

# считывание основания системы счисления, в которую мы хотим перевести число
while True:
    number_system_2 = int(input())
    if number_system_2>36 and number_system_2<1:
        print('введите интересующую вас систему счисления ещё раз')
    elif number_system_2<=36 and number_system_2>0:
        break

# промежуточный перевод в десятичную систему счисления
number_decimal = 0
for q in range (0,len(number)):
    number_decimal += int(number[q]) * number_system_1**(len(number)-1-q)

# перевод из десятичной системы счисления в выбранную пользователем
result_number = []
current_number = number_decimal
flag = True
while flag:
    if current_number>number_system_2:
        result_number.append(current_number%number_system_2)
        current_number//=number_system_2
    elif current_number<=number_system_2:
        result_number.append(current_number)
        flag = False
        break

result_number = result_number[::-1]

result = ''
# формирование готового ответа
for q in range (0,len(result_number)):
    if result_number[q] > 9:
        result_number[q] = numbers_list[result_number[q]]
        result+= str(result_number[q])
    elif result_number[q] <=9:
        result+= str(result_number[q])

print(result)

print('нажмите любую клавишу, чтобы закрыть')

input()



