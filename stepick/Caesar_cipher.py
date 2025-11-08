
EN_Upper_symbols = []
EN_Lower_symbols = []
RU_Upper_symbols = []
RU_Lower_symbols = []

for q in range (ord('A'), ord('Z')+1):
    EN_Upper_symbols.append(chr(q))
for q in range (ord('a'), ord('z')+1):
    EN_Lower_symbols.append(chr(q))
for q in range (ord('А'), ord('Я')+1):
    RU_Upper_symbols.append(chr(q))
for q in range (ord('а'), ord('я')+1):
    RU_Lower_symbols.append(chr(q))

print('''Шифрование - cipher
Дешифрование - decipher
Выберите опцию''')
while True:
    cipher_flag = input()
    if cipher_flag != 'cipher' and cipher_flag != 'decipher':
        print('Некорректный ввод. Задайте опцию снова')
    else:
        break

original_text = []

print('Введите текст. Для начала работы программы введите слово start')
while True:
    text = input()
    if text != 'start':
        original_text.append(text)
        original_text.append('\n')
    else:
        break

original_text = ''.join(original_text)
original_text = list(original_text)

print('Введите ключ шифрования')
while True:
    key = input()
    if key.isdigit() == False:
        print('Ключом может являться только число')
    else:
        key = int(key)
        break

def cipher_text(original_text: str, key: int) -> str:
    cipher_text = []
    for q in range (len(original_text)):
        if original_text[q] in EN_Upper_symbols:
            cipher_text.append(EN_Upper_symbols[(EN_Upper_symbols.index(original_text[q])+key) % len(EN_Upper_symbols)])
        elif original_text[q] in EN_Lower_symbols:
            cipher_text.append(EN_Lower_symbols[(EN_Lower_symbols.index(original_text[q])+key) % len(EN_Lower_symbols)])
        elif original_text[q] in RU_Upper_symbols:
            cipher_text.append(RU_Upper_symbols[(RU_Upper_symbols.index(original_text[q])+key) % len(RU_Upper_symbols)])
        elif original_text[q] in RU_Lower_symbols:
            cipher_text.append(RU_Lower_symbols[(RU_Lower_symbols.index(original_text[q])+key) % len(RU_Lower_symbols)])
        elif original_text[q] not in (EN_Upper_symbols+EN_Lower_symbols+RU_Upper_symbols+RU_Lower_symbols):
            cipher_text.append(original_text[q])
    cipher_text = ''.join(cipher_text)
    return cipher_text
    
def decipher_text(original_text: str, key: int) -> str:
    cipher_text = []
    for q in range (len(original_text)):
        if original_text[q] in EN_Upper_symbols:
            shift = EN_Upper_symbols.index(original_text[q])-key
            if shift<0:
                shift = shift%(-len(EN_Upper_symbols))
            elif shift>(len(EN_Upper_symbols)-1):
                shift = shift%(len(EN_Upper_symbols))
            cipher_text.append(EN_Upper_symbols[shift])

        elif original_text[q] in EN_Lower_symbols:
            shift = EN_Lower_symbols.index(original_text[q])-key
            if shift<0:
                shift = shift%(-len(EN_Lower_symbols))
            elif shift>(len(EN_Lower_symbols)-1):
                shift = shift%(len(EN_Lower_symbols))
            cipher_text.append(EN_Lower_symbols[shift])
        
        elif original_text[q] in RU_Upper_symbols:
            shift = RU_Upper_symbols.index(original_text[q])-key
            if shift<0:
                shift = shift%(-len(RU_Upper_symbols))
            elif shift>(len(RU_Upper_symbols)-1):
                shift = shift%(len(RU_Upper_symbols))
            cipher_text.append(RU_Upper_symbols[shift])

        elif original_text[q] in RU_Lower_symbols:
            shift = RU_Lower_symbols.index(original_text[q])-key
            if shift<0:
                shift = shift%(-len(RU_Lower_symbols))
            elif shift>(len(RU_Lower_symbols)-1):
                shift = shift%(len(RU_Lower_symbols))
            cipher_text.append(RU_Lower_symbols[shift])
        
        elif original_text[q] not in (EN_Upper_symbols+EN_Lower_symbols+RU_Upper_symbols+RU_Lower_symbols):
            cipher_text.append(original_text[q])

    cipher_text = ''.join(cipher_text)

    return cipher_text

if cipher_flag == 'cipher':
    result_text = cipher_text(original_text,key)
    print(result_text)
elif cipher_flag == 'decipher':
    result_text = decipher_text(original_text,key)
    print(result_text)

print('Для завершения нажмите любую клавишу')

input()