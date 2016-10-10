import re
from math import log


def get_password_strength(password):
    N = 0
    len_password = len(password)
    low_letter_rus = bool(re.search(r'[а-яё]', password))
    low_letter_en = bool(re.search(r'[a-z]', password))
    up_letter_rus = bool(re.search(r'[А-ЯЁ]', password))
    up_letter_en = bool(re.search(r'[A-Z]', password))
    digit = bool(re.search(r'\d+', password))
    simbols = bool(re.search(r'[^А-Яа-яA-Za-zЁё0-9]', password))
    lst = [
        [digit, 10],
        [up_letter_en, 26],
        [up_letter_rus, 33],
        [low_letter_en, 26],
        [low_letter_rus, 33],
        [simbols, 30],
        ]
    for item in lst:
        if item[0]:
            N = N + item[1]
    password_strength_bits = len_password * (log(N) / log(2))
    password_strength_max = 16 * (log(158) / log(2))
    password_strength = (password_strength_bits * 100) / password_strength_max
    password_strength = password_strength // 10
    return (password_strength)


if __name__ == '__main__':
    password = input('Введие Ваш пароль для проверки: ')
    password_strength = get_password_strength(password)
    print (password_strength)
