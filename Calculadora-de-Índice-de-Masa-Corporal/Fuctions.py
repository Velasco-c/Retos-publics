from Data import load_data,save_load,resources
from Utilities import Decimal,Whole


def Calculate_BMI(name):
    load_data(name)
    amount = Whole("Enter your whole: ")
    for i in range(0,amount):
        print("\n" + "-" * 60)
        print(f"Person #{i + 1}")
        print("-" * 60)
        name_personal = input("Enter your name   : ").strip()
        weight = Decimal("Enter your weight (kg): ")
        height = Decimal("Enter your height (m): ")
        IMC = weight/(height*height)
        print("-"*60)
        new = {
            "Name": name_personal,
            "Weight": weight,
            "Height": height,
            "IMC": IMC
        }
        resources.append(new)
    print("\n Data entered correctly")
    save_load(name)
    
def Display_BMI(name):
    load_data(name)
    print("\n" + "=" * 60)
    print("BMI RECORDS")
    print("=" * 60)
    for p in resources:
        print(f"Name   : {p['Name']}")
        print(f"Weight : {p['Weight']} kg")
        print(f"Height : {p['Height']} m")
        print(f"BMI    : {p['IMC']}")
        print("-" * 60)