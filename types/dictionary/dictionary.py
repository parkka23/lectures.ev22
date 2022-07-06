# dicr() - словарь, упорядоченная коллекция элементов (с python 3.7 упорядоченный)
# Упорядоченный - в каком порядке добавляем, в таком и сохраняется, порядок сохраняется
# Каждый элемент в словаре содержится в паре ключ:значение
# Ключ может быть только неизменяемым типом данным (str, tuple, Integer) и уникальным, чотобы найти
# Значения могут быть любыми типами данных
# нет дубликатов
# hash taples, ассоциативный массив, объект(js) - dictionary

# dic={
#     'brand':'Ford',
#     'model':'Mustang',
#     'year':1964
# }
# print(dic)
# print(type(dic))

# литервлы tuple - запятые
# tup=1,2,3
# print(type(tup))

## Способы создания
# 1
# dic={'key':'value'}

# 2
# dic = dict()
# dic=dict((('key1','value1'),('key2','value2')))
# print(dic)

# user_info={
#     'first name':'John',
#     'last name':'Snow',
#     'age':24,
#     'email':'john_snow@gmail.com',
#     'role':'moderator',
#     # 'first name':'Ron' last in first out
#     # [1,2,3]:'list' error
# }

# Доступ к элементу 
# 1 []
# print(user_info['first name'])

# 2 get()
# print(user_info.get('age'))

# items() вывод пар, каждая пара в кортеже, список кортежей пар
# print(user_info.items())
# for i in user_info.items():
#     print(i)

# keys() выводит ключи, список ключей
# print(user_info.keys())

# добавить пару
# user_info['height']=185
# print(user_info)

# изменить значение 
# user_info['age']=30
# print(user_info)

# update({key: value}) изменяет или создает новую пару
# update
# print(user_info)
# user_info.update({'first name':'Bill'})
# print(user_info)
# create
# user_info.update({'address':'Moscow'})
# print(user_info)

# keys()
# ключи по отдельности
# for i in user_info.keys():
#     print(i)

# values() выводит значения
# print(user_info.values())

# pop() удаляет пару по ключу 
# user_info.pop('age')
# print(user_info)

# popitem() удаляет последнюю пару в словаре
# user_info.popitem()
# print(user_info)

# setdefault(key, [default value]) возвращает значение по ключу, если не существует - создает новую пару
# return
# res=user_info.setdefault('age')
# print(res)

# create
# res=user_info.setdefault('address', 'Moscow')
# print(user_info)



# example1
# список словарей(структур)
# roles={
#     0:'Adimin',
#     1:'Moderator',
#     2:'Vendor',
#     3:'Customer',
#     4:'Guest'
# }
# users=[
# {
#     'id':0,
#     'name':'John',
#     'role':roles[0]
# },
# {
#     'id':1,
#     'name':'Mike',
#     'role':roles[3]
# },
# {
#     'id':2,
#     'name':'Jean',
#     'role':roles[2]
# }
# ]

# product={
#     'id':1,
#     'title':'Samsung Galaxy S22',
#     'description':'Lorem Ipsum',
#     'price':1000
# }
# print(users)
# print(product)

# id = int(input('Enter your id: '))
# if users[id]['role']==roles[0]:
#     product['description']=input('Enter new description: ')
# else:
#     raise Exception('You have no rights!')
# print(product)

# example2
# import random
# ls=['plov','manty','kuurdak','lagman']
# p=0
# m=0
# k=0
# l=0
# for i in range(0,10000):
#     choice = random.choice(ls)
#     if choice.lower() == 'plov':
#         p+=1
#     elif choice.lower() == 'manty':
#         m+=1
#     elif choice.lower() == 'kuurdak':
#         k+=1
#     elif choice.lower() == 'lagman':
#         l+=1
# print(f'plov = {p}')
# print(f'manty = {m}')
# print(f'kuurdak = {k}')
# print(f'lagman = {l}')
# mx=max(p,m,k,l)

#1 0-200 mean numbers
# ls=list(range(0,200,2))
# print(ls)

#2 3 5    0-200
# ls=[]
# for i in range(0,200):
#     if i%3==0 and i%2==0:
#         ls.append(i)
# print(ls)

# ls=list(range(6,200,6))
# print(ls)


#0 100 1 4
# ls=[]
# for i in range(0,100):
#     if i%2==0:
#         i*=i
#     ls.append(i)
# print(ls)



print(dir(set))
    