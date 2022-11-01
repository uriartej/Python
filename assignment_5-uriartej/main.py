from contacts import *

contacts = Contacts(filename = 'c.dat')

while(True):
    print("*** TUFFY TITAN WEATHER LOGGER MAIN MENU")
    print()
    print("1. Add Contact: ")
    print("2. Modify Contact: ")
    print("3. Delete Contact: ")
    print("4. Print Contact:")
    print("5. Set Contact:")
    print("6. Exit the program")

    choice = int(input("Enter menu choice:"))
    print()

    if choice == 1:
        i = input("Enter Phone Number:" )
        fn = input("Enter First Name:")
        ln = input("Enter Last Name:")
        r = contacts.add_contact(id=i, first_name=fn, last_name=ln)
        if r == 'error':
            print("Phone number already exists")
        else:
            print("Added: " + r[0] + " " + r[1] + ".")
            print()

    elif choice == 2:
        i = input("Enter Phone Number:")
        fn = input("Enter First Name:")
        ln = input("Enter Last Name:")
        r = contacts.modify_contact(id=i, first_name=fn, last_name=ln)
        if r == 'error':
            print('Modification cannot be made')
        else:
            print("Modified: " + r[0] + " " + r[1] + ".")
        print()


    elif choice == 3:
        i = input("Enter Phone Number:")
        r = contacts.delete_contact(id=i)
        if r == 'error':
            print('Modification cannot be deleted')
        else:
            print("Deleted: " + r[0] + " " + r[1] + ".")
        print()

    elif choice == 4:
        print("*************************CONTACT LIST********************")
        print("Last Name              First Name              Phone")
        print("*************** ******************* *****************")
        for key in contacts.data:
            print(f'{contacts.data[key][1]:22}{contacts.data[key][0]:22} {key:12}')
            print()
        
    #set filename
    elif choice == 5:
        fn = input("Enter new filename: ")
        contacts = Contacts(filename=fn)
        print()
        
    elif choice == 6:
        break