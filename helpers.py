import random


def create_login():
    email = ''

    for nick in range(8):
        email += random.choice(list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

    email += f'3{random.randint(100, 999)}@example.com'

    return email


def create_password():
    password = ''

    for i in range(random.randint(6, 12)):
        password += random.choice(list('0123456789abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

    return password


def create_incorrect_password():
    password = ''

    for i in range(random.randint(1, 5)):
        password += random.choice(list('0123456789abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

    return password


def create_name():
    name = ''

    for i in range(random.randint(1, 15)):
        name += random.choice(list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

    if name[0].isupper():
        name = name[0] + name[1:len(name)].lower()
    else:
        name = name[0].upper() + name[1:len(name)].lower()

    return name
