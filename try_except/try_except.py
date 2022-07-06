# Обработка исключений
# оператор try-except

# Ошибки (всегда) - связаны с кодом 
# SyntaxError
# IndentationError
# TabError

# Исключения (иногда) - invalid values
# ZeroDivisionError
# ArithmeticError
# NameError
# ImportError
# IndexError
# KeyError
# ValueError
# BaseException # прородитель всех



# try ... except
# если в try error выполнится except

# try:
#     <body try>
# except:
#     <body except>

# try:
#     num=int(input('Enter a number:'))
#     print('Success!')
# except:
#     print('Incorrect data!')
# print('Very inmportant code...')

##### sys
# ls=[1,2,3,4]
# index=int(input())
# try:
#     res=ls[index]
#     print(res)
# except:
#     import sys
#     print(f'Oops, we caught {sys.exc_info()[0]} error!')


##### Exception as 
####  list index out of range error!
# ls=[1,2,3,4]
# index=int(input())
# try:
#     res=ls[index]
#     print(res)
# except Exception as e:
#     print(f'Oops, we caught {e} error!')

#####  <class 'IndexError'> error!
# ls=[1,2,3,4]
# index=int(input())
# try:
#     res=ls[index]
#     print(res)
# except Exception as e:
#     print(f'Oops, we caught {e.__class__} error!')

##### (IndexError, ValueError)
# ls=[1,2,3,4]
# index=int(input())
# try:
#     res=ls[index]
#     print(res)
# except (IndexError, ValueError):
#     print(f'Oops, incorrect index!')

#####
# ls=[1,2,3,4]
# try:
#     index=int(input())
#     res=ls[index]
#     print(res)
# except IndexError:
#     print('IndexError!')
# except ValueError:
#     print('ValueError!')


# else in try...except
# finally in try...except        
# try:
#     <body>
# except:
#     <body>
# else:
#     # есди нет ошибки в try
#     <body>
# finally:
#     # в любом случае
#     <body>



# try:
#     n1=int(input())
#     n2=int(input())
#     res=n1/n2
# except ZeroDivisionError:
#     print('ZeroDivisionError')
# except ValueError:
#     print('Invalid symbols')
# else:
#     print(res)
# finally:
#     print('End of the code')



