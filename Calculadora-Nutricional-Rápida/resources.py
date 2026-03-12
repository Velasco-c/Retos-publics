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
        carbohydrates = Decimal("Enter grames the carbohyudrates: ")
        fat = Decimal("Enter grames the fat: ")
        total = (protein*4)+(carbohydrates*4)+(fat*9)
        new ={
            "Food" : Food,
            "protein" : protein,
            "fat" : fat,
            "carbohydrates" : carbohydrates,
            "total" : total
        }
        resources.append(new)
    print("it was added correctly")
    save_data(name)
    
def Display_Calories(name):
    load_data(name)
    print("\n" + "=" * 60)
    print("RECORD CALORIES")
    print("=" * 60)
    if not resources:
        print(f"No records were found for: {name}")
        print("-" * 60)
    else:
        for p in resources:
            print(f"Type   : {p['Food']}")
            print(f"protein : {p['protein']} g")
            print(f"carbohydrates : {p['carbohydrates']} g")
            print(f"Total calories    : {p['total']} kcal")
            print("-" * 60)
