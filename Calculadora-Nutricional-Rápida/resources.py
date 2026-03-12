from data import load_data,save_data,resources
from utilities import Whole,Decimal

def calculate_calories(name):
    load_data(name)
    amount = Whole("Enter you whole: ")
    for i in range(0,amount):
        print("\n"+"-"*60)
        print(f"Number #{i+1}")
        print("\n"+"-"*60)
        Food = input("Enter name the food: ")
        protein = Decimal("Enter grames the proteins: ")
        carbohyudrates = Decimal("Enter grames the carbohyudrates: ")
        fat = Decimal("Enter grames the fat: ")
        total = (protein*4)+(carbohyudrates*4)+(fat*9)
        new ={
            "Food" : Food,
            "protein" : protein,
            "fat" : fat,
            "carbohyudrates" : carbohyudrates,
            "total" : total
        }
        resources.append(new)
    print("it was added correctly")
    save_data(name)
    