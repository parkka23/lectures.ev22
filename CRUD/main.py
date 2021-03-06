from views import list_of_products, retrieve_product, create_product, update_product,delete_product

def main():
    print('Hello! You have an access to following functions:\n\tLIST - 1\n\tRETRIEVE - 2\n\tCREATE - 3\n\tUPDATE - 4\n\tDELETE - 5')
    choice=input('Enter your choice: ')
    if choice=='1':
        print(list_of_products())
    elif choice=='2':
        print(retrieve_product())
    elif choice=='3':
        print(create_product())
    elif choice=='4':
        print(update_product())
    elif choice=='5':
        print(delete_product())
    else:
        print('Invalid choice!')
        main()
    
    ask=input('Do you want to continue? (Y/n): ')
    if ask.lower()=='y': main()
    elif ask.lower()=='n': print('Bye-bye!')

main()