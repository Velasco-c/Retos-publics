def Whole(message):
    while True:
        try:
            whole = int(input(message))
            return whole
        except ValueError as e:
            print(f"Type error is: {e}")
            
def Decimal(message):
    while True:
        try:
            decimal = float(input(message))
            return decimal
        except ValueError as e:
            print(f"Type error is: {e}")

def main_menu():
    print("""
    ========================================
            Quick Nutrition Calculator
    ========================================
    1. Calculate the total calories
    2. Display calories Information
    3. Exit
    ========================================
    """)
    