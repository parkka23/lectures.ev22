# def - ключевое слово

# определение
# def <name_of_function> (<a, b> # параметры):
#     <body> # некий кодб некая логика
#   <return>

# вызов
# <name_of_function>(<5, 6> # аргументы)

# Параметры функции - переменные, которые будет принимать функция для того, чтобы мы смогли работать с данными, которые передаются в функцию
# Аргументы - данные, которые мы передаем для параметров при вызове функции

# return для того, чтобы функция что-то возвращала и для того, чтобы мы могли работать с результатом функции
# является необязательным оператором (возвращает None, если не указать его)

# методы привязаны к типу, классу, а функции - нет

# ls=[]
# result = ls.append(1)
# print(ls)
# print(result)

# res=ls.pop()
# print(res)

# snapcase - _
# camelcase - новое слово с большой


# return
# def sumTwoNums (a, b):
#     res=a+b
#     return res
# sumTwoNums(4,4)

# no return
# def sumTwoNums (a, b):
#     res=a+b
#     print(res)
# print(sumTwoNums(4,4))



# def isEven(a):
#     return True if a%2==0 else False
    # if a%2==0:
    #     return True
    # else:
    #     return False


# Аннотация
# def isEven1(a: int) -> bool:
#     """
#     Функция определяет, является ли число типа int четным
#     """
#     return True if a%2==0 else False
# isEven()
# isEven1()

# from typing import list
# def getPolindrom(words: list[str]) -> list[str]:
#     """
#     Функция возвращает список из полиндромов
#     """
#     res=[]
#     for i in words:
#         if i.lower()==i.lower()[::-1]:
#             res.append(i)
#     return res
    
# ls=['1111','sdf','dd','sdggggg']
# print(getPolindrom(ls))


# без параметров
# def func():
#     print('Hello world')
# func()



# default parameters
# def printWelcome(name: str ='User') -> str:
#     print(f'Welcome, {name}!')
# printWelcome('Ksenia')
# printWelcome()


# task депозит через опр время с процентом 10
# def func(n: float, t: int) -> float: 
#     """
#     return final amount of money
#     """ 
#     if n<30000:
#         raise Exception('Incorrect amount of money!')
#     if t<3:
#         raise Exception('Incorrect period!')
#     for i in range(t):
#         n+=n*0.1       
#     return n
# n=float(input('Enter the amount of money (>= 30000):'))
# t=int(input('Enter the number of years (>=3):'))
# print(func(n,t))

# tast 
# def func(st:str)-> str:
#     ls=st.split(' ')
#     res=' '.join(ls[::-1])
#     return res
# st='Hello John Snow'
# print(func(st))