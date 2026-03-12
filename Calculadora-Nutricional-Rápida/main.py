from utilities import Whole,main_menu
from resources import calculate_calories

name = "Calculadora-Nutricional-Rápida/Calorias.json"

while True:
    main_menu()
    op = Whole("Enter one of the option: ")
    if op == 3:
        print("leaving ..... ")
        break
    elif op == 1:
        calculate_calories(name)
    elif op ==2:
        pass
    else:
        print("invalid option")