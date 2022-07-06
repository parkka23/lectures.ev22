# tuple - неизменяемый, индексируемый, упорядоченный
# t=(1,2,3)
# t=1,2,3

# функция - готовый код, есть имя функции, аргументы
# оптимизация - изменение, подстраивание
# это все объекты
# st=str('hello')
# st1='hello'
# ls=list(1,2,3)
# ls2=[1,2,3]
# set={1,2}
# dic={'key':'value'}

# tup=(1,2)
# print(type(tup))

# tup=1,2
# print(tup)
# print(type(tup))

# tup=1,2
# tup[0]=3 error

## конвертация
# tup=tuple([1,2,3]) оптимизация, т.к. tuple меньше памяти, чем list

## range - генератор упорядоченных объектов, функция
# tup=tuple(range(5))
# print(tup)
# print(range(5))
# print(*range(5))

# emails_ls=['python@gmail.com', 'tima@mail.ru']
# emails=('python@gmail.com', 'tima@mail.ru',['potato','melon'])
# print(emails.__sizeof__(),emails_ls.__sizeof__())
# print(type(emails[-1])) # ['potato','melon'] - list
# emails[-1].append('apple')
# print(emails[-1]) # можно изменять list внутри tuple

# tup1=(2,2,3,4)
# tup=tuple(range(5))
# tup += tup1
# print(tup)
# print(tup1.count(2))
# print(id(tup))
# print(tup.index(2))

## Loops

## for
# for value in tuple_sequance:
#     print(value)  

# names=('Tima','bob','Tom')
# names_enter=('bob','Tom')
# for i in names:
#     if i in names_enter:
#         print(i.capitalize()+' hello',len(i))
#     else:
#         print(i.capitalize()+' go home',len(i))
 
####### split
# first_step_names=[]
# names=input('Enter names:').split(' ')
# print(names)
# for name in names:
#     if len(name) > 4:
#         first_step_names.append(name)    
# print(first_step_names)

# for i in range(10):
#     print(i)
  
#проходится по диапазону

### while
# ctrl + C

# i = 0
# while i < 4:
#     print(i)   
#     i += 1 

# i=0
# num=3
# while num > i:
#     print(num)
#     num -= 1

#цикл работает с итерируемыми объектами

# __iter__' скрытый метод
# print(True if '__iter__' in dir(str) else False)

# ls=(str, int, float, list, tuple)
# for i in ls:
#     print(i, True if '__iter__' in dir(i) else False)

# операторы циклов
## continue
# names=['bob','bill','tom','kate','anne']
# for i in names:
#     if i.lower()=='bill':
#         continue
#     print(f'hello {i}')

## break
# names=['bob','bill','tom','kate','anne']
# names.insert(len(names)//2,'ron') #в середину
# print(names)
# for i in names:
#      if i.lower()=='ron':
#          break
#      print(f'hello {i}')

# бесконечный цикл
# можно не исп переменную
# while True:
#     if input('Enter message:') in "war black drug".split(' '):
#         print('blocked')
#         break

# верхний регистр - сигнал не изменять

# CRUD - create read update delete


# DB_EMAILS = []
# while True:
#     print('1 - input email, 2 - show emails, 3 - delete email, 4 - update, 5 - exit')
#     option = int(input("Enter your choice: "))
#     if option==1:
#         email=input('Enter email: ')
#         if email.endswith('@gmail.com'):
#             if email in DB_EMAILS:
#                 print('This email already exists!')
#                 continue
#             DB_EMAILS.append(email)
#             continue
#         else:
#             print('Invalid format!')
#     elif option==2:
#         print(DB_EMAILS)
#     elif option==3:
#         email=input('Enter email: ')
#         if email in DB_EMAILS:
#             # index=DB_EMAILS.index(email)
#             # DB_EMAILS.pop(index)
#             DB_EMAILS.remove(email)
#             continue
#         else:
#             print(f'{email} does not exist!')
#     elif option==4:
#         old=input('Enter email: ')
#         if old in DB_EMAILS:
#             new=input('Enter new email: ')
#             if new.endswith('@gmail.com'):
#                 if new in DB_EMAILS:
#                     print('This email already exists!')
#                     continue
#                 # index=DB_EMAILS.index(old)
#                 # DB_EMAILS[index]=new
#                 DB_EMAILS.remove(old)
#                 DB_EMAILS.append(new)
#             else:
#                 print('Invalid format!')
#         else:
#             print(f'{old} does not exist!')
#     elif option==5:
#         break
#     else:
#         raise Exception('Error!')

   


    







