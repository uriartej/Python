import flights
f = flights.Flights('f.dat')


while True:
    print("       *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU")
    print()
    print("1.   Add Flights")
    print("2.   Print Flight Schedule")
    print("3.   Set Flight Schedule Program")
    print("9.   Exit the Program")
    print()
    choice = int(input("Enter Menu Choice:  "))
    print()
    
    if choice == 1:
        org = input("Enter Origin: ")
        dest = input("Enter Destination: ")
        num = input("Enter Flight Number: ")
        dep = input("Enter departure time(HHHMM): ")
        arr = input("Enter arrival time(HHHMM): ")
        next_day = input("IS arrival next day (Y/N): ")
        
        f.add_flight(org, dest, num, dep, next_day, arr)
        print()
        
    elif choice == 2:
        fts = f.get_flights()
        print("=============== FLIGHT SCHEDULE ====================")
        print("Origin Destination Number Departure Arrival Duration")
        print("====== =========== ====== ========= ======= ========")
        for x in fts:
            org = x[0]
            dest = x[1]
            num = x[2]
            dep = x[3]
            arr = x[4]
            dur = x[5]
            print(f'{org: 7}{dest:12}{num:>6}{dep:>10}{arr:>9}{dur:>9}')
            print()
    
    elif choice == 3:
        fn = input("Enter the filename: ")
        f = flights.Flights(fn)
        print()
        
    elif choice == 9:
        break