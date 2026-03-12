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
    HEALTH TOOL - BMI CALCULATOR
    ========================================
    1. Calculate Body Mass Index (BMI)
    2. Display BMI Information
    3. Exit
    ========================================
    """)
    