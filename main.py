"""
This program showcases what triggers various exceptions and how errors get handled.
"""

print("Welcome to the Exception playground.")

def generic_check(check, message):
    if check:
        return True
    print("\n[invalid_input: {}]".format(message))
    return False

def input_check(input):
    # 1. Unformatted input check
    if not generic_check('/' in input, "no division operator"):
        return False

    input_list = []
    try:
        input_list = [int(n) for n in input.replace(' ', '').split('/')]
    except ValueError:
        print("\nValueError:\t\tPlease use whole numbers.")
        return False

    # 2. Formatted input check
    check_list = (
        (len(input_list) == 2, "too many operands"),
        (input_list[-1] == 0, "0 not divisor")
    )
    
    for check, message in check_list:
        if not generic_check(check, message):
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
          user_input = input('\n\tPlease try dividing any number with a 0. \
           \n\t(for example, type "5 / 0"){}'.format(input_message))

          if input_check(user_input):
              print("\nSuccess! Unfortunately, you can't divide numbers by 0.")

              if prompt_1():
                  break  

TASK_LIST = (task_1, )

for task in TASK_LIST:
    task()

print("\nHope you had fun. Bye!")

# -------------------------------