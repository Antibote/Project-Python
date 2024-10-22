import random

def generate_password(len, char):
    return random.sample(char,int(len))


digits= '0123456789'
lowercase_letters='abcdefghijklmnopqrstuvwxyz'
uppercase_letters= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation= '#$%&*+-=?@^_.'
exc= 'il1Lo0O'

chars = ''

cntPw = input('Укажите количество паролей для генерации:')
lenPw = input('Укажите длину одного пароля:')
digOn = input('Включать ли цифры 0123456789? (y/n)')
if digOn == 'y':
    chars+=digits
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
if ABCon == 'y':
    chars+=uppercase_letters
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
if abcOn == 'y':
    chars+=lowercase_letters
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
if chOn == 'y':
    chars+= punctuation
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')
if excOn == 'y':
    for c in 'il1Lo0O':
        chars.replace(c,'')

for i in range(int(cntPw)):
    print('Ваш ', i+1, '-й пароль: ', *generate_password(lenPw,chars),sep='')