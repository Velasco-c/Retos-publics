from Utilities import main_menu,Whole
from Fuctions import Calculate_BMI

name = "Calculadora-de-Índice-de-Masa-Corporal/registration.json"


while True:
    main_menu()
    op = Whole("Enter one of the options: ")
    if op == 3:
        print("leaving ..... ")
        break
    elif op == 1:
        Calculate_BMI(name)
    elif op == 2:
        pass
    else:
        print("Invalid option")    