import random


def generate_password():
    for _ in range(1, Number_of_passwords+1):
        if Exclusion_of_ambiguous_characters == 'да':
            if chars not in 'il1Lo0O':
                for i in range(password_length):
                    print(random.choice(chars), end='')
                print()
        else:
            for i in range(password_length):
                print(random.choice(chars), end='')
            print()


print('Введите количество паролей для генерации')
Number_of_passwords = int(input())
print('Длину одного пароля')
password_length = int(input())
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
print('Включать ли цифры 0123456789 "Да" если включать или "НЕТ"')
Include_numbers = input().lower()
if Include_numbers == 'да':
    chars += digits
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ "Да" если включать или "НЕТ"')
Include_uppercase_letters = input().lower()
if Include_uppercase_letters == 'да':
    chars += lowercase_letters
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz "Да" если включать или "НЕТ"')
Include_lowercase_letters = input().lower()
if Include_lowercase_letters == 'да':
    chars += uppercase_letters
print('Включать ли символы !#$%&*+-=?@^_ "Да" если включать или "НЕТ"')
Include_characters = input().lower()
if Include_characters == 'да':
    chars += punctuation
print('Исключать ли неоднозначные символы il1Lo0O "Да" если ислючать или "НЕТ" если оставить')
Exclusion_of_ambiguous_characters = input()
generate_password()