# -*- coding: utf-8 -*-
from re import search, match
from os.path import exists

default_pswd_list = ['123456', '12345', 'password', 'DEFAULT', '123456789', 'qwerty', '12345678', 'abc123', 'pussy',
                     '1234567', '696969', 'ashley', 'fuckme', 'football', 'baseball', 'fuckyou', '111111', '1234567890',
                     'ashleymadison', 'password1', 'madison', 'asshole', 'superman', 'mustang', 'harley', '654321',
                     '123123', 'hello', 'monkey', '000000', 'hockey', 'letmein', '11111', 'soccer', 'cheater', 'kazuga',
                     'hunter', 'shadow', 'michael', '121212', '666666', 'iloveyou', 'qwertyuiop', 'secret', 'buster',
                     'horny', 'jordan', 'hosts', 'zxcvbnm', 'asdfghjkl', 'affair', 'dragon', '987654', 'liverpool',
                     'bigdick', 'sunshine', 'yankees', 'asdfg', 'freedom', 'batman', 'whatever', 'charlie', 'fuckoff',
                     'money', 'pepper', 'jessica', 'asdfasdf', '1qaz2wsx', '987654321', 'andrew', 'qazwsx', 'dallas',
                     '55555', '131313', 'abcd1234', 'anthony', 'steelers', 'asdfgh', 'jennifer', 'killer', 'cowboys',
                     'master', 'jordan23', 'robert', 'maggie', 'looking', 'thomas', 'george', 'matthew', '7777777',
                     'amanda', 'summer', 'qwert', 'princess', 'ranger', 'william', 'corvette', 'jackson', 'tigger',
                     'computer']


def get_password_strength(password):
    strength = 1
    # 1. Проверка на то, что пароль создан из одних цифр (это может быть телефон или дата рождения), да и в любом случае
    # мощность алфавита цифр мала
    if password.isd1igit():
        return 1
    # 2. Проверка на длину
    if len(password) > 10:
        return 10
    if len(password) > 4:
        strength += 1
        if len(password) > 6:
            strength += 1
    else:
        return 1
    # 3. Проверка на наличие цифр
    if not search('\d', password) is None:
        strength += 1
        if not search('\d{2,}', password) is None:
            strength += 1
    # 4. Проверка на наличие специальных символов
    if not search(r'\W', password) is None:
        strength += 1
        if not search(r'\W{2}', password) is None:
            strength += 1
    # 5. Проверка на использование разных регистров букв
    if not search('([a-z].*[A-Z])|([A-Z].*[a-z])', password) is None:
        strength += 1
        if not search('(([a-z].*[A-Z])|([A-Z].*[a-z])){2}', password) is None:
            strength += 1
    return strength


def dict_match(password, pswd_list):
    for bad_password in pswd_list:
        if match(bad_password, password) and len(bad_password) == len(password):
            return 1
        if match((bad_password), password):
            return get_password_strength(password.strip(bad_password))
    return get_password_strength(password)


def load_password_dict(filepath):
    if not exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return file_handler.read().split('\n')


def choose_dict():
    filepath = raw_input(u'Введите путь к файлу с паролями или нажмите Enter, '
                         u'чтобы воспользоваться встроенным словарем:')
    pswd_list = load_password_dict(filepath)
    if pswd_list is None:
        if filepath:
            print (u'Данных нет или указан неверный путь к файлу, будет использован встроенный словарь')
        pswd_list = default_pswd_list
    return pswd_list

if __name__ == '__main__':
    password = raw_input(u"Введите свой пароль:")
    print(u"Защищенность вашего пароля %i из 10" % dict_match(password, choose_dict()))
