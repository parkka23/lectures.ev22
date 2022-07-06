# Работа с файлами

# каретка - указатель
# В текстовом виде
# контекстный менеджер или open()

# open(<path>)

# Виды путей: относительный (от рабочей папки), абсолютный
# file=open('/home/humster/Desktop/ev.22/files/files.py')
#file=open('files.py') 

# print(file)
# <_io.TextIOWrapper name='/home/humster/Desktop/ev.22/files/files.py' mode='r' encoding='UTF-8'>

# Режимы для работы с файлами: 
# r/r+ - read (считывание содержимого)
# w/w+ - write (удаляет, потом записывать) если не сущ, создает новый
# a/a+ - append (добавить) если не сущ, создает новый
# t - text, b - binary, 
# x - запись, создать файл,если не сущ, создает новый

# read()
# file=open('/home/humster/Desktop/ev.22/files/text.txt','r')
# data = file.read() # str
# data=data.split('\n') # list
# print(data) # ['Hello, world. ', '', 'My names is Park Ksenia. ', 'I am a student.']
# print(type(data))
# file.close()

# readlines()  возвращает список строк содержимого, цифра - лимит байтов
# file=open('/home/humster/Desktop/ev.22/files/text.txt','r')
# data=file.readlines(16)
# print(data) # ['Hello, world. \n', '\n', 'My names is Park Ksenia. \n', 'I am a student.']
# file.close()


# w (не сможем прочесть, но c + сможем)
# file=open('/home/humster/Desktop/ev.22/files/text.txt','w')
# file.write('Hello-hello!\nBye!')
# file.close()

# a
# file=open('/home/humster/Desktop/ev.22/files/text.txt','a+')
# file.write('\nYES YES YES\nNO NO NO')
# file.close()

#--------------------------
# контекстный менеджер - с ним не нужно закрыть файл

# with open('/home/humster/Desktop/ev.22/files/text.txt') as file:
#     data= file.read()
#     print(data)
#-----------------

# # writelines - принимает итерируемый объект
# ls=['Hello, world','My name is Ksenia','I am 19']
# with open('/home/humster/Desktop/ev.22/files/text.txt','w') as file:
#     file.writelines(i+'\n' for i in ls)

#----------------------------

# Методы для каретки:
# tell() - возвращает инфекс, где находится каретка
# seek(<int>) 0 перемещает каретку н указанный индекс

# task
from PIL import Image
import pytesseract
import re
def get_imei_codes(list_images):
    list_of_imei=[]
    for image in list_images:
        string=pytesseract.image_to_string(image)
        print(string)
        list_of_imei.append(re.findall(r'IME\d.\s\d+',string))
        print(list_of_imei)
    
    with open('/home/humster/Desktop/ev.22/files/imeicodes.txt','w') as file:
        for i in list_of_imei:
            for j in i:
                file.write(f'{i}\n')
list_images=['/home/humster/Desktop/ev.22/files/imei.jpg']

get_imei_codes(list_images)