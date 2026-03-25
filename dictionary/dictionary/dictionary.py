dictionary = {}  
print(" (1)add (2)delete (3)list (4)exit") 

while True: 
    choice = input("Enter your choice: ")  

    if choice == '1': 
        name = input("Enter item name:")
        qty = int(input("Enter item quantity:"))
        dictionary[name] = qty

    elif choice == '2':  
        name = input("Enter item name:")
        if name in dictionary:
            del dictionary[name]
    elif choice == '3':
         print(dictionary) 

    elif choice == '4':
        break