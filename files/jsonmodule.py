# JavaScript Object Notation - JSON
# Единый формат хранения и передачи данных между компьютерами, сервисами, приложениями и языками программирования через сеть Интернет или файлами 
# <filename>.json
# json выглядит как питон словарь 

# {
#     'id':1,
#     'author':'John',
#     'posts':[]
# }

# Задача - переводить json в python dictionary

# JS object == {}
# PY dict == {}
# JSON == {}

#-------------------

####### Процесс сериализации данных и их десериализация

# Сериализация (запись данных в JSON) - перевод python dict в JSON формат (либо созранять все в файл либо сохранить просто как текстовые данные)(dict -> JSON)
# Методы сериализации:
# dump() - метод записывает объект python в файл в формате JSON
# dumps() - метод записывает объект python в строку в формате JSON

# Десериализация (чтение данных из JSON) - перевод из JSON в python dict (python object) (JSON -> fict).
# Методы десериализации:
# load() - метод считывать файл в формате JSON и переводит в объект python
# loads() - метод считывать JSON в текстовом формате и переводит в объект python

#------------------

# JSON "", пробел после :, true, null вместо None

#------------------

###### Процесс десериализации

# load()
# import json
# from urllib.request import urlopen
# data = urlopen('https://randomuser.me/api/')
# print(type(data))
# # print(data)
# # <class 'http.client.HTTPResponse'>
# # <http.client.HTTPResponse object at 0x7fa54acc9550>
# genetate_to_dict=json.load(data)
# print(genetate_to_dict)
# print(type(genetate_to_dict)) # dict

# loads()
# import json
# with open('downApi.json','r') as file:
#     data=file.read()
#     # print(data)
#     # print(type(data)) # str
#     user=json.loads(data)
#     print(user)
#     print(type(user)) # dict

#----------------------

##### Процесс десериализации

# dump()
# import json
# dic={
#     'name':'John',
#     'surname':'Snow',
#     'status':True,
#     'wife':None,
#     'children': False
# }

# with open('new.json','w') as file:
#     json.dump(dic,file)

# dumps()
# import json
# dic={
#     'name':'John',
#     'surname':'Snow',
#     'status':True,
#     'wife':None,
#     'children': False
# } 

# string=json.dumps(dic)
# print(string)

#---------------------------------------------------

# CRUD - create retrieve(read) update delete