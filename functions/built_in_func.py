# map()
# filter()
# lambda()
# enumerate()



####### Анонимные функции lambda() (такие же функции только без названия)
# Lambda функции могут принимать сколько угодно аргументов, но всегда возвращают только одно выражение

# def sum_args(a,b):
#     return a+b

# def sum_args1(a,b): return a+b

# print(sum_args(1,2))
# print(sum_args1(1,2))


# sum_arg = lambda a,b: a+b
# print(sum_arg(1,2))

# x=lambda a,b,c: a+b+c
# print(x(1,2,3))



# ex
# def func(n):
#     return lambda a:a*n

# mydoubler=func(2)
# # mydoubler = lambda a:a*2
# print(mydoubler(11))

# mytripler=func(3)
# print(mytripler(11))



# ex
# ls=['def','john','','  ','hello']
# ls2=sorted(ls,key=len)
# print(ls2)








# ex
# import random
# ls=['plov','manty','kuurdak','lagman','dymlama']
# p=0
# m=0
# k=0
# l=0
# d=0
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
#     elif choice.lower() == 'dymlama':
#         d+=1
# # print(f'plov = {p}')
# # print(f'manty = {m}')
# # print(f'kuurdak = {k}')
# # print(f'lagman = {l}')
# # print(f'dymlama = {d}')
# # mx=max(p,m,k,l)
# dic={'plov':p,'manty':m,'kuurdak':k,'lagman':l,'dymlama':d}
# print(dic)
# print(sorted(dic.items()))
# # [('dymlama', 1923), ('kuurdak', 1967), ('lagman', 2060), ('manty', 2008), ('plov', 2042)]
# res=sorted(dic.items(), key=lambda x:x[1])
# print(res)
# winner=res[-1]
# print('Winner =',winner[0],', score =',winner[1])

# # def func(x):
# #     return x[1]
# # key=func                     = lambda x:x[1]
    


#----------------------------------------------

##### map(function, iterabale) - применяет функцию к каждому элементу последовательности и возвращает map object (итератор) с результатами
# например - с его помощью выполнить преобразование элементов

# ex
# ls=['one','two','three']
# res=map(str.upper,ls)  # <map object at 0x7f06b52a7ca0>  
# print(res)

# res=list(map(str.upper,ls))  # list 
# print(res)


# ex
# ls=['1','2','3']
# res=list(map(int,ls))
# print(res)


# ex
# ls=['John','Kate','Anne']
# res=list(map(lambda i:f'Hello, {i}!',ls))
# print(res)

# ex
# ls=[1,2,3,4]
# ls2=[100,200,300,400,500]
# res=list(map(lambda i,j:i*j,ls,ls2))
# print(res)

# ex
# dic={
#     1:2,
#     3:4,
#     4:5
# }
# res=dict(map(lambda items:(items[0],str(items[1])),dic.items()))
# print(res)

#----------------------




##### filter(function,iterable) - применяет функцию ко всем элементам последовательности и возвращает filter object (итератор) с теми объектами для которых функция вернула True

# ex
# ls=['one','two','tree','100','1','JOhn22']
# res=list(filter(str.isdigit,ls))
# print(res)

# for i in res:
#     print(i)


# ex
# ls=[10,11,102,213,131,132]
# res=list(filter(lambda x:x%2==0,ls))
# print(res)


# ex
# ls=['one','john','two','hello']
# res=list(filter(lambda i:len(i)>3,ls))
# print(res)


#-------------------------------

##### enumerate(iterable) - принимает итерируемый объект

# ls=[1,2,3,4]
# for i,j in enumerate(ls):
#     print(i,j)

# res=list(enumerate(ls))
# print(res)



# task



# ls=['D','D','U','U','D','D','U','D','U','U','U','D']
# level=0
# valley=0
# for i in range(len(ls)):
#     if ls[i]=='U':
#         level+=1
#     else: level-=1
#     if level==-1 and ls[i+1]=='U': valley+=1
#     print(i,level)
# print(valley)

# def countingValleys(step,path):
#     valley=0
#     level=0
#     for i in path:
#         if i=='U': 
#             level+=1
#             if level==0:valley+=1

#         elif i=='D': level-=1
#     return valley
        
# print(countingValleys(12,ls))


#------------------------------------------------------------------

#### zip(iterables) - соединяет каждый элемент итерируемых элементво между собой в тип данных tuple и возвращает его

# ls1=[1,2,3]
# ls2=[100,200,300]
# res=list(zip(ls1,ls2))
# print(res)  # [(1, 100), (2, 200), (3, 300)]


# a=[1,2,3,4,5]
# b=[10,20,30,40]
# c=[100,200,300]
# res=list(zip(a,b,c))
# print(res)  # [(1, 10, 100), (2, 20, 200), (3, 30, 300)]


#--------------------------------------------------------
##### zip for creating dicts

# ex
# d_keys=['hostname','location','vendor','model','IOS','IP']
# d_val=['john22','Moscow street','Cisco','4452','15.4','12.211.2.2']
# res=dict(zip(d_keys,d_val))
# print(res)

# ex
# d_keys=['hostname','location','vendor','model','IOS','IP']
# data={
#     'r1':['john22','Moscow street','Cisco','4452','15.4','12.211.2.2'],
#     'r2':['ann22','Moscow street','Cisco','2453','15.5','12.211.2.3']

# }

# # 1
# data2={k: dict(zip(d_keys,v)) for k,v in data.items()}
# print(data2)

# # 2
# ann={}
# for k in data.keys():
#     ann[k]=dict(zip(d_keys,data[k]))
# print(ann)

#----------------------------------------------

# all - возвращает True, если все элементы объекта - истина(или объект пустой)   проверка
# пустой эл- False
# пустая строка - False

# ls=[False,1,'ee',True]
# print(all(ls)) # False

# ls=[True,1,'ee',True]
# print(all(ls)) # True

# ls=[]
# print(all(ls)) # True


# ip='10.233.0.0'
# res=all(i.isdigit() for i in ip.split('.'))
# print(ip.split('.'))
# print(res)

#----------------

# any - возвращает True, если хотя бы один эл - истинна
# ls=[0,1,'',False]
# print(any(ls))

# ex
# def ignore_command(com):
#     '''
#     функция проверяет есть ли в команде слово из списка ignore, True - есть, False - нет
#     '''
#     ignore=['rm -rf','alias','reset']
#     for i in ignore:
#         if i in com: return True
#         else: return False

# if ignore_command('sudo rm user'):
#     raise Exception('Invalid command')
# else:
#     print('OK!')

# ex
# ignore=['rm -rf','alias','reset']
# com='sudo rm user'
# if any([i in com for i in ignore]):
#     raise Exception('Invalid command')
# else:
#     print('OK!')

# print([i in com for i in ignore])

#-------------------------
# ex
# from random import choice, choices
# from string import ascii_letters, digits
# from itertools import repeat

# n=int(input('Enter the number of passwords: '))
# res={f(choices(ascii_letters, k=10), choices(digits, k=5)) 
#     for f in repeat(lambda x,y: ''.join(set((x+y))),n)}
# print(
#     res
# )

# from statistics import mean

# dlina={len(x) for x in res}
# print({mean(dlina)})
# # ls=['a','b','c']
# # ls2=['2','1','3']
# # print(''.join(set((ls+ls2))))

ls=1,2,3,4
res=list(enumerate(ls))
print(res)
