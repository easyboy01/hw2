password = input('Введите пароль: ')
try:
    c = 1 / len(password)
    b = 1 / int(password)
    print('Ваш пароль состоит только из цифр')
except ZeroDivisionError:
    print('Вы ввели пустой пароль')
except ValueError:
    print('Требования к паролю соблюдены')