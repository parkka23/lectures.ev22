## Операторы сравнения
# <, >, ==, >=, <=, !=
# сравнение слов - сравнение первых букв
# true - 1, false - 0
# print(orb(str)) - ASCII code of char
# print(chr(1280)) - char of ASCII code fff

## Условные операторы
# if, else, elif

# Синтаксис
# if <condition> :
#     <body>
# elif <condition>:
#     <body>
# else:
#     <body>

# example
# str=input()
# if str=='Hello':
#     print('Hello, stranger')
# elif str == 'Bye':
#     print('Bye, stranger')
# else:
#     print('Error')
# print('Finished')
 
# sign up
# email=input('email:')
# pw1=input('Password:')
# pw2=input('Password confirmation:')
# if pw1!=pw2:
#     raise Exception('Password did\'t match')
# else:
#     print('Success')

# age=input('Age:')
# print(type(age))
# if age.isdigit():
#     age=int(age)
# else:
#     raise Exception('Error')

# if age<18:
#     print(f'Come in {18-age} years')
# else:
#     print('Accepted')

## Логические операторы
# and, or, not
# xor
# me=20
# you = 18
# res = not me==20 
# print(res)

# isUserGoogleUser=True
# isUserGitHubUser=True
# isUserAgeGreater21=False
# userAccountCoins=7000
# if isUserGoogleUser and isUserGitHubUser and isUserAgeGreater21 or userAccountCoins>5000:
#     print('You can enter')
# else:
#     print('You can\'t enter')


