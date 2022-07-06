## task 1 
# 1)
# ls=list(range(0,200,2))
# print(ls)

# task 2 
# ls=[]
# for i in range(0,200):
#     if i%3==0 and i%2==0:
#         ls.append(i)
# print(ls)

# ls=list(range(6,200,6))
# print(ls)

# task 3 
# ls=[]
# for i in range(0,100):
#     if i%2==0:
#         i*=i
#     ls.append(i)
# print(ls)

# list comprehension - генератор списка
# в одну строку, простые, избавиться от for, быстрее for
# синтаксический сахар (только в питоне) - красивый и краткий код
# Синтаксис:
# ls = [expression for item in iterable <if condition == True>]
# expression - то что append
# list - comprehension - упрощенный подход к созданию списков, который задействует цикл for, а также конструкции if-else для определения того, 
# что в итоге окажется добавлено в список
# на моменте создания добавляет элемент
###

# task 1
# ls=[i for i in range(0, 100, 2)]
# print(ls)

# task 1
# ls=[i for i in range(200) if i%2==0 and i%3==0]
# print(ls)

# task 3
# ls=[i**2 if i%2==0 else i for i in range(100)]
# print(ls)

###
# fruits=['apple', 'banana', 'peach', 'mango', 'lemon']
# ls=[i.capitalize() for i in fruits]
# ls=[i for i in fruits if i == 'cherry']
# ls=[i for i in fruits if i != 'apple']
# print(ls)


###
# вложенный цикл
# list_=[[1,2,3],[4,5,6]]
# ls=[]
# for inner_list in list_:
#     for num in inner_list:
#         ls.append(num)
# print(ls)

# comprehension
# ls=[num for inner_list in list_ for num in inner_list]
# print(ls)


###
# import datetime
# ls=[]
# start = datetime.datetime.now()
# print(start)
# for i in range(1,100_000_000):
#     ls.append(i)
    
# finish=datetime.datetime.now()
# print(finish)
# print('time =', finish-start)

# ls=[i+10 if i==8 else i+1 for i in range(10)]
# print(ls)

