from Data import load_data,save_load,resources
from Utilities import Decimal,Whole


def Calculate_BMI(name):
    load_data(name)
    amount = Whole("Enter your whole: ")
    for i in range(0,amount):
        print("-"*60)
        name_personal = input("enter your name: ").strip()
        weight = Decimal("enter your weight: ")
        height = Decimal("enter your height: ")
        IMC = weight/(height*height)
        print("-"*60)
        new = {
            "Name": name_personal,
            "weight": weight,
            "height": height,
            "IMC": IMC
        }
        resources.append(new)
    print("data entered correctly")
    save_load(name)