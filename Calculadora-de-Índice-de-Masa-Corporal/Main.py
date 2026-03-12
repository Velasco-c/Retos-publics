from Utilities import main_menu,Whole

while True:
    main_menu()
    op = Whole("Enter one of the options: ")
    if op == 3:
        print("leaving ..... ")
        break
    elif op == 1:
        pass
    elif op == 2:
        pass
    else:
        print("Invalid option")    