def is_number(input):
    try:
        return int(input)
    except:
        return None

def is_valid_operator(operator):
    #valid_operators = ["+", "-", "/", "*"]
    return operator in ["+", "-", "/", "*"]

def ask_for_a_number(forceValidInput = True):
    user_input = input("Podadaj liczbe: ")
    casted_value = is_number(user_input)
    if forceValidInput:
        while casted_value == None:
            user_input = input("Podaj liczbe: ")
            casted_value = is_number(user_input)
    return is_number(user_input)


def ask_for_a_operator(forceValidInput = True):
    user_input = input("Podadaj operator: ")
    if forceValidInput:
        while not is_valid_operator(user_input):
            user_input = input("Podaj operator: ")
    else:
        if not is_valid_operator(user_input):
            return None
        else:
            return user_input
    

def calculate(number1, operator, number2):
    if number1 == None or operator == None or number2 == None:
        return None
    
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        if number2 == 0:
            print("Error, division by zero")
            return None
        else:
            return number1 / number2
    else:
        return None

def simple_calculator():
    end_condition = True
    while end_condition:
        print("Podaj pierwszy numer")
        number1 = ask_for_a_number(False)
        if number1 == None:
            end_condition = False
        else:
            print("Podaj operator")
            operator = ask_for_a_operator(True)
            print("Podaj drugi numer")
            number2 = ask_for_a_number(True)
            result = calculate(number1, operator, number2)
            print(f"Result of calculation is {result}")



if __name__ == "__main__":
    simple_calculator()
