# -*- coding: utf-8 -*-
from re import search, match, fullmatch
from os.path import exists
from getpass import getpass

default_pswd_list = ['123456', 'password', '12345678', 'qwerty', '123456789', '12345', '1234', '111111',
                     '1234567', 'dragon', '123123', 'baseball', 'abc123', 'football', 'monkey',
                     'letmein', '696969', 'shadow', 'master', '666666', 'qwertyuiop', '123321',
                     'mustang', '1234567890', 'michael', '654321', 'pussy', 'superman', '1qaz2wsx',
                     '7777777', 'fuckyou', '121212', '000000', 'qazwsx', '123qwe', 'killer', 'trustno1',
                     'jordan', 'jennifer', 'zxcvbnm', 'asdfgh', 'hunter', 'buster', 'soccer', 'harley',
                     'batman', 'andrew', 'tigger', 'sunshine', 'iloveyou', 'fuckme', '2000', 'charlie',
                     'robert', 'thomas', 'hockey', 'ranger', 'daniel', 'starwars', 'klaster', '112233',
                     'george', 'asshole', 'computer', 'michelle', 'jessica', 'pepper', '1111', 'zxcvbn',
                     '555555', '11111111', '131313', 'freedom', '777777', 'pass', 'fuck', 'maggie',
                     '159753', 'aaaaaa', 'ginger', 'princess', 'joshua', 'cheese', 'amanda', 'summer',
                     'love', 'ashley', '6969', 'nicole', 'chelsea', 'biteme', 'matthew', 'access',
                     'yankees', '987654321', 'dallas', 'austin', 'thunder', 'taylor', 'matrix',
                     'william', 'corvette', 'hello', 'martin', 'heather', 'secret', 'fucker', 'merlin',
                     'diamond', '1234qwer', 'gfhjkm', 'hammer', 'silver', '222222', '88888888',
                     'anthony', 'justin', 'test', 'bailey', 'q1w2e3r4t5', 'patrick', 'internet',
                     'scooter', 'orange', '11111', 'golfer', 'cookie', 'richard', 'samantha', 'bigdog',
                     'guitar', 'jackson', 'whatever', 'mickey', 'chicken', 'sparky', 'snoopy',
                     'maverick', 'phoenix', 'camaro', 'sexy', 'peanut', 'morgan', 'welcome', 'falcon',
                     'cowboy', 'ferrari', 'samsung', 'andrea', 'smokey', 'steelers', 'joseph',
                     'mercedes', 'dakota', 'arsenal', 'eagles', 'melissa', 'boomer', 'booboo', 'spider',
                     'nascar', 'monster', 'tigers', 'yellow', 'xxxxxx', '123123123', 'gateway',
                     'marina', 'diablo', 'bulldog', 'qwer1234', 'compaq', 'purple', 'hardcore',
                     'banana', 'junior', 'hannah', '123654', 'porsche', 'lakers', 'iceman', 'money',
                     'cowboys', '987654', 'london', 'tennis', '999999', 'ncc1701', 'coffee', 'scooby',
                     '0000', 'miller', 'boston', 'q1w2e3r4', 'fuckoff', 'brandon', 'yamaha', 'chester',
                     'mother', 'forever', 'johnny', 'edward', '333333', 'oliver', 'redsox', 'player',
                     'nikita', 'knight', 'fender', 'barney', 'midnight', 'please', 'brandy', 'chicago',
                     'badboy', 'iwantu', 'slayer', 'rangers', 'charles', 'angel', 'flower', 'bigdaddy',
                     'rabbit', 'wizard', 'bigdick', 'jasper', 'enter', 'rachel', 'chris', 'steven',
                     'winner', 'adidas', 'victoria', 'natasha', '1q2w3e4r', 'jasmine', 'winter',
                     'prince', 'panties', 'marine', 'ghbdtn', 'fishing', 'cocacola', 'casper', 'james',
                     '232323', 'raiders', '888888', 'marlboro', 'gandalf', 'asdfasdf', 'crystal',
                     '87654321', '12344321', 'sexsex', 'golden', 'blowme', 'bigtits', '8675309',
                     'panther', 'lauren', 'angela', 'bitch', 'spanky', 'thx1138', 'angels', 'madison',
                     'winston', 'shannon', 'mike', 'toyota', 'blowjob', 'jordan23', 'canada', 'sophie',
                     'Password', 'apples', 'dick', 'tiger', 'razz', '123abc', 'pokemon', 'qazxsw',
                     '55555', 'qwaszx', 'muffin', 'johnson', 'murphy', 'cooper', 'jonathan', 'liverpoo',
                     'david', 'danielle', '159357', 'jackie', '1990', '123456a', '789456', 'turtle',
                     'horny', ]

pswd_min_strength = 1
pswd_max_strength = 10

def check_for_one_digit(password):
    return True if search('\d', password) is not None else False


def check_for_many_digits(password):
    return True if search('\d{2}', password) is not None else False


def check_for_upper_and_lower_case_letters(password):
    return False if password.islower() or password.isupper() else True


def check_for_one_special_symbol(password):
    return True if search(r'\W', password) is not None else False


def check_for_many_special_symbols(password):
    return True if not search(r'\W{2}', password) is None else False


def check_pswd_is_digit(password):
    return True if password.isdigit() else False


def get_password_strength(password):
    pswd_current_strength = pswd_min_strength

    if check_pswd_is_digit(password):
        return pswd_min_strength

    if len(password) > 10:
        return pswd_max_strength
    elif len(password) < 5:
        return pswd_min_strength
    elif len(password) > 4:
        pswd_current_strength += 1
        if len(password) > 6:
            pswd_current_strength += 1
            if len(password) > 8:
                pswd_current_strength += 1

    if check_for_one_digit(password):
        pswd_current_strength += 1
        if check_for_many_digits(password):
            pswd_current_strength += 1

    if check_for_one_special_symbol(password):
        pswd_current_strength += 1
        if check_for_many_special_symbols(password):
            pswd_current_strength += 1

    if check_for_upper_and_lower_case_letters(password):
        pswd_current_strength += 1

    return pswd_current_strength


def compare_with_common_passwords_dictionary(password, pswd_list):
    for bad_password in pswd_list:
        if fullmatch(bad_password.rstrip('\n'), password):
            return pswd_min_strength
        if match(bad_password.rstrip('\n'), password):
            return get_password_strength(password.strip(bad_password))
    return get_password_strength(password)


def load_password_dict(filepath):
    if exists(filepath):
        with open(filepath, 'r') as file_handler:
            return file_handler.readlines()


def choose_dictionary_with_common_passwords():
    filepath = input(u'Введите путь к файлу с паролями или нажмите Enter, чтобы воспользоваться встроенным словарем:')
    pswd_list = load_password_dict(filepath)
    if pswd_list is None:
        if filepath:
            print(u'Данных нет или указан неверный путь к файлу, будет использован встроенный словарь')
        pswd_list = default_pswd_list
    return pswd_list

if __name__ == '__main__':
    password = getpass(u"Введите свой пароль:")
    print(u"Защищенность вашего пароля %i из 10" %
          compare_with_common_passwords_dictionary(password, choose_dictionary_with_common_passwords()))
