from utilities import Whole,main_menu

name = "Calculadora-Nutricional-Rápida/Calorias.json"

while True:
    main_menu()
    op = Whole("Enter one of the option: ")
    if op == 3:
        print("leaving ..... ")
        break
    elif op == 1:
        pass
    elif op ==2:
        pass
    else:
        print("invalid option")