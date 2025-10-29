contacts={}

while True:
    print("welcome to contact book app")
    print("1. create contact")
    print("2. view contact")
    print("3. update contact")
    print("4. delete contact")
    print("5. search contact")
    print("6. count contact")
    print("7. exit contact")

    choice = input("enter your choice: ")

    if choice == "1":
        name=input("enter your name:  ")
        if name in contacts:
            print(f"contact {name} already exists!")
        else:
            age=int(input("enter your age: "))
            email=input("enter your email: ") 
            mobile=int(input("enter your number: "))
            contacts[name]={"age":age , "email":email , "mobile":mobile} 
            print(f"contact {name} has been created succesfully")

    elif choice== "2":
        name = input("enter contact name to view: ")
        if name in contacts:
            contact =contacts[name]
            print(f"name{name}, age{age}, email{email}, mobile{mobile}")
        else:
            print("contact not found!")

    elif choice == "3":
        name =input("enter name to update contact: ")
        if name in contacts:
            age=int(input("enter your updated age: "))
            email=input("enter your updated email: ") 
            mobile=int(input("enter your updated number: "))
            contacts[name]={"age":age , "email":email , "mobile":mobile} 
        else:
            print("contact not found!") 

    elif choice == "4":
        name =input("enter name to delete contact: ")
        if name in contacts:
            del contacts[name]
            print("contact deleted succesfulyy")
        else:
            print("contact not found")

    elif choice == "5":
        search_name =input("enter name to search contact: ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower in name.lower():
                print(f"found-name{name}, age{age}, email{email}, mobile{mobile}")
                found = True
            if not found:
                print(" no contact found with that name ")

    elif choice == "6":
        print(f"total contacts in your book {len(contact)}")

    elif choice == "7":
        print("closing the program....")
        break 
    else:
        print("invalid input")
           
