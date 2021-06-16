"""
This program showcases what triggers various exceptions and how errors get handled.
"""

print("Welcome to the Exception playground.")

base_message = "\n[invalid_input: {}]"

def symbol_check(input, symbol, msg):
    if symbol in input:
        return True
    print(base_message.format(msg))
    return False

def division_check(input):
    return symbol_check(input, '/', "no division operator")

def zero_check(input):
    return symbol_check(input, '0', "no 0 operand")

def format_check(input):
    try:
        input_list = [int(n) for n in input.replace(' ', '').split('/')]
    except ValueError:
        print("\nValueError:\t\tDivision only works with numbers.")

    if len(input_list) != 2:
        print(base_message.format("too many operands"))
        return False

    if input_list[-1] != 0:
        print(base_message.format("0 not divisor"))
        return False

    if type(input_list[0]) != int:
        print(base_message.format("divident not integer"))
        return False

    return True

CHECK_LIST = (division_check, zero_check, format_check)    

def input_check(input):
    for check in CHECK_LIST:
        if not check(input):
            return False
    return True

CONTINUE = 'c'
KEEP_TESTING = 't'

input_message = "\n\n\tInput:\t"

def prompt_1():
    while True:
        user_input = input("\n\tContinue or keep testing?\tC / T{}"
        .format(input_message))

        if user_input.lower() == CONTINUE:
            return True
        elif user_input.lower() == KEEP_TESTING:
            return False 

def task_1():
    print('\n1. "Dividing by 0"')      
    while True:
        try:
            user_input = input('\n\tPlease try dividing any number with a 0. \
            \n\t(for example, type "5 / 0"){}'.format(input_message))

            if input_check(user_input):
                print("\nSuccess! Unfortunately, you can't divide numbers by 0.")

                if prompt_1():
                    break  

        except Exception:
            print("Exception:\t\tAn error has occurred.")

TASK_LIST = (task_1, )

for task in TASK_LIST:
    task()

print("\nHope you had fun. Bye!")

# -------------------------------