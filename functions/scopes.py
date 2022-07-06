# Области видимости и пространтсва имен:

# Built-in (встроенная) - print, len, max
# Global (глобальная) везде доступна
# Enclosed (нелокальнаяб охватывающая локальную функцию, non local)
# Local (локальная)


# def printlist(ls):
#     for i in ls:
#         print(i)
# ls=[1,2,3]
# printlist(ls)


# a=10 # global
# print # built-in
# def hello(): # global
#     a='hello' #local
#     print(a,'- local')
# hello()
# print(a,'- global')



# x='global'
# print(x)
# def enclosed():
#     x='enclosed'
#     def local():
#         x='local'
#         print(x)
#     print(x)
#     local()
#     print(x)
# enclosed()
# print(x)

# LEGB компилятор ищет переменную


# def func():
#     a=5
#     print(a)
# a='str'
# func()

# num=10
# def func():
#     def innerfunc():
#         print(num)
#     innerfunc()
# func()

##### глоб пременую нельзя изменить в локальной области видимости - создает локальную перем с таким именем
# Оператор global - изменяет значение глобальной переменной в локальной области видимости
# Оператор nonlocal - изменяет значение нелокальной переменной в локальной области видимости

# var=100 # global
# def increment():
#     global var
#     var+=1
#     print(var)
# increment()

# def counter():
#     num=0
#     def increment():
#         nonlocal num
#         num+=1
#         return num
#     return increment
# c=counter()
# print(c) 
# print(c())
# print(c())
# print(c())
"""
<function counter.<locals>.increment at 0x7fac20ecf0d0>
1
2
3
"""

# print(dir(__builtins__))
# print(len(dir(__builtins__)))
# print(abs(-2))        
# abs=12 # переобпределение встроенного имени в глобальной области
# del abs
# print(abs(-3)) # error


##### 1
# ls=[[1,2,3],[4,5,6],[3,5,1]]
# ls2=[]
# for i in ls:
#     s=0
#     for j in i:
#         s+=j
#     ls2.append(s)
# print(ls2)
# print(max(ls2))


# ls=[[1,2,3],[4,5,6],[3,5,1]]
# ls2=[]
# for i in ls:
#     ls2.append(sum(i))
# print(ls2)
# print(max(ls2))


# ls=[[1,2,3],[4,5,6],[3,5,1]]
# ls2=[sum(i) for i in ls]
# print(max(ls2))


### 2
alice=[13,15,90]
john=[5,15,50]

# a=0
# j=0
# for i in range(len(alice)):
#     if alice[i]>john[i]: a+=1
#     elif john[i]>alice[i]: j+=1
# dic={'alice':a, 'john':j}
# print(dic)

###
# def func(A,J):
#     a=0
#     j=0
#     for i in range(3):
#         if A[i]>J[i]: a+=1
#         elif J[i]>A[i]: j+=1
#     return {'alice':a, 'john':j}
# print(func(alice,john))


#### 3
str='sdfsdfasd'
dic={i: str.count(i) for i in str}
print(dic)