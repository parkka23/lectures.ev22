from random import random
import json
import random
file_path = 'data.json'

def get_data():
    with open(file_path) as file:
        return json.load(file)


def list_of_products():
    data=get_data()
    return data

def retrieve_product():
    data=get_data()
    # print(data,'----------')
    id=int(input('Enter an id of the product: '))
    product =list(filter(lambda x: x['id']==id,data))
    return product[0]


def get_id():
    with open('id.txt','r') as file:
        id=int(file.read())
        # print(id)
        # print(type(id)) 
        id+=1
    with open('id.txt','w') as file:
        file.write(str(id))
    return id

def create_product():
    data=get_data()
    # print(data)
    product ={
        'id':get_id(),
        'title':input('Enter a title of the product: '),
        'price': float(input('Enter a price of the product: ')),
        'description':input('Enter a description of the product: ')
    }
    data.append(product)
    with open(file_path, 'w') as file:
        json.dump(data, file)
    result={
        'msg':'Created',
        'product':product
    }
    return result

def update_product():
    data=get_data()
    flag=False
    id=int(input("Enter an id of the product: "))
    product=list(filter(lambda x:x['id']==id,data))
    if not product:
        return {
            'msg':'Invalid id! Product does not exist!'
        }
     
    index=data.index(product[0])
    choice=input('What do you wnat to change? (1 - title, 2 - price, 3 - description): ')
    if choice=='1':
        data[index]['title']=input("Enter the new title: ")
        flag=True
    elif choice=='2':
        data[index]['price']=input("Enter the new price: ")
        flag=True
    elif choice=='3':
        data[index]['description']=input("Enter the new description: ")
        flag=True
    else:
        print('Invalid choice to update!')
    
    with open(file_path,'w') as file:
        json.dump(data,file)
    
    if flag==True:
        return {
            'msg':'Updated',
            'product':data[index]
        }
    else:
        return {
            'msg':'Not updated'
        }


def delete_product():
    data=get_data()
    id=int(input('Enter an id of the product: '))
    product=list(filter(lambda x: x['id']==id,data))

    if not product:
        return {
            'msg':'Invalid id! Product does not exist!'
        }

    index=data.index(product[0])
    deleted=data.pop(index)
    json.dump(data, open(file_path,'w'))
    return {
        'msg':'Deleted',
        'product':deleted
    }

 
    


# [
#     {
#         "id": 0, 
#         "title": "Iphone 23 Pro Max", 
#         "price": 1000, 
#         "description": "Super fast and good smartphone"
#     }, 
#     {
#         "id": 1, 
#         "title": "Samsung Galaxy S22 Ultra", 
#         "price": 1200, 
#         "description": "Super Puper fast and good smartphone"
#     }
# ] 
