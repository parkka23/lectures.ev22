## list() - коллекция, список, массив, изменяемый, последовательный тип данных, коллекция объектов разного типа
# list, tuple, set, dic
# l=[1,'Hello',[1,2,3]]
# l[2][2] вложенные списки

# Изменение списка
# l=[1,'f',3]
# l[1]=2
# print(l)

# Удаление элемента del 
# l=[1,2,3]
# del l[0]
# print(l)

# list=[1,'str', False, None, [1,2,3]]
# print(list)
# print(type(list))

## Создать список
# Способ1
# list(<iterable>)
# iterable - разделяемый на элементы

# list=list('Hello world')
# print(list)

# tuple=('banana','cherry','apple')
# print(tuple)
# print(type(tuple))
# list=list(tuple)
# print(list)
# print(type(list))

# Способ2
# list(range(start,stop,[step])) - возвращает последовательность элементов (числа)
# a= list((range(0,-100,-2))
# print(a)

# Способ3
# []
# list=[1,11,'qq']
# print(list)
# print(type(list))

## Методы
# print(dir(list))

# append(element) - добавляет элемент в конец списка
# l=[1,2,3]
# print(l)
# l.append(4)
# l.append([1,2,3])
# print(l)

# extend(element[iterable]) - расширяет и добавляет в конец раздробленный элемент
# l=[1,2,3]
# l.extend([1,2,3])
# print(l)

# insert(<index>, element) - добавляет элемент по указанному index
# l=['str', 2,3,False]
# l.insert(1,[1,2,3,None])
# l.insert(2,1)
# print(l)
# print(l[2:5]) срез
# print(len(l)) длина списка

# index(element, [start, end]) - возвращает индекс элемента (начиная с start, в интервале start - end)
#не существует - ошибка
# l=[1,2,3,33,3,4,5,3,2,1,'hello']
# print(l.index(3,0,4))

# проверка на наличие в списке in
# if 'hello' in l:
#     print(f'"hello" is in this list:{l.index("hello")}')

# count(element) - возвращает количество вхождений element в списке
# l=[1,2,3,4,5,5,5,5,1]
# print(l.count(5))

# remove(element) - удаляет element, но если нет - ошибка

# pop([index]) - удаляет и возвращает элемент по index, но если index не указан, то удаляет последний элемент
# l=[5,1,2,3,4,5]
# l.remove(5)
# l.remove(5)
# print(l)
# l.pop()
# print(l)
# deleted = l.pop(0)
# print(l)
# print(deleted)

# sort([reverse=True/False], [key=<>]) - сортирует список; если reverse=True - убывающий порядок
# l=[1,2,3,4,5,5,5,-2,-3]
# print(l)
# l.sort(reverse=True)
# print(l)

# l=['hello','john','London','a']
# l.sort() #по ASCII коду первого символа
# print(l)
# l.sort(key=len) # по длине   
# print(l)




# ls=[1,2,3]
# append
# pop lifo last in first out
# del
# remove fifo first in first out

# a=(1,'s')

# изменяемы больше памяти выделяется
# неизм только нужное количество



# for i in range(1,10):
#     i-=5
#     print(i)
# print(i)