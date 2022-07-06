# def sumOfArgs(a: int,b: int,c: int,d: int)-> int:
#     return a+b+c+d
# print(sumOfArgs(1,2,3,4))

## адрес функции
# print(sumOfArgs)

## присваивание перерменной
# res=sumOfArgs
# print(res(1,2,3,4))


#### Позиционные и именованные аргументы
# def printParams(a=None,b=None,c=None):
#     print(a,'is stored in a')
#     print(b,'is stored in b')
#     print(c,'is stored in c')

# # именованные
# printParams(1,2,3)

# # Позиционные
# printParams(1,c=3,a=3)

# # Error   1 -> a
# printParams(1,c=3,a=3)





# def sumOfArgs(a: int,b: int,c: int,d: int)-> int:
#     return a+b+c+d
# print(sumOfArgs(1,2,3,4)) # позиционные аргументы (arguments)
# print(sumOfArgs(d=1,a=2,b=3,c=4)) # именованные аргументы (keyword arguments)

## сначала позиционные 
# print(sumOfArgs(4,5,d=1,c=2)) 






#### оператор * разпаковывает итерируемые объекты (раскрыть без цикла)
# a=[1,2,3]
# b=[4,5,6]
# c=[*a,*b]
# print(c) # - [1, 2, 3, 4, 5, 6]

# print(*a) # 1 2 3
# print(*a, end='*\n') # 1 2 3*





### *args (распаковка позиционных аргуметнов) **kwargs (распаковка именованных) в функциях


# def print_scores(student, *scores):
#     print(f'Student name: {student}')
#     # print(scores)
#     # print(type(scores)) # tuple
#     for i in scores:
#         print(f'Score: {i}')
# print_scores('John',100,90,80)

# def print_pet_names(owner, **pets):
#     print(f'Owner name: {owner}')
#     for p, n in pets.items():
#         print(f'{p} : {n}')
# print_pet_names('John',dog='Rex',cat='Larry',fish=['Nemo','Dori','Alex'],turtle='Leonardo')






# def getData(a,b,*args,**kwargs):
#     print('Параметры a и b:',a,b)
#     print(args[1])

#     print(kwargs['name'])
#     print('Аргументы:', args)
#     print('Именованные аргументы:', kwargs)
# getData(1,2,3,4,5,lang='python',name='John',car="BMW")







# def conc_two_strings(str1,str2):
#     import random
#     res=random.randint(1,10)
#     return str1+str2+str(res)
# print(conc_two_strings('hello','world'))





# def generate_password(name, surname):
#     import random
#     num=random.randint(100000,1000000)
#     return name+surname+'_'+str(num)

# print(generate_password('John','Snow'))

# def getInfo():
#     name=input('Enter your name: ')
#     surname=input('Enter your surname: ')
#     return generate_password(name,surname)

# print(getInfo())






# def gen_rand_str(len_, lang):
#     import string as s
#     import random
#     str= ''.join(random.choice(s.ascii_lowercase+s.digits) for i in range(len_))
#     return str
# print(gen_rand_str(15,'eng'))







def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('ZeroDivisionError')

def multiply(a,b):
    return a*b

def calc():
    try:
        a=float(input('Enter the first number: '))
        b=float(input('Enter the second number: '))
    except ValueError:
        print('ValueError')
        calc()
    sign=input('Enter an operator (+, -, /, *): ')
    res=None
    if sign=='+': res= add(a,b)
    elif sign=='-': res= subtract(a,b)
    elif sign=='/': res=divide(a,b)
    elif sign=='*': res= multiply(a,b)
    else: 
        print('Incorrect operator!')
    print(res)
    question=input('Do you want to continue? (y/n): ')
    if question.lower()=='y': calc()
    else: print('Thanks for using our calculator! Bye!')

calc()
