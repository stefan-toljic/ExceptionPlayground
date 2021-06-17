"""
This program showcases what triggers various exceptions and how errors get handled.

Project structure:
  - main.py         (program)       Main program.
  - exceptions.py   (exceptions)    User defined exceptions.

Playground map:
  1. "Dividing by 0"            Un/formatted input handling.
  2. "Guess the number"         Custom exception raising.
  3. "Expressions & results"*   Arithmetic expression generating & result storing.

*work in progress...
"""

from exceptions import ValueTooSmall, ValueTooBig
import random as rand

print("Welcome to the Exception playground.")

INPUT_MESSAGE = "\n\n\tInput:\t"

def prompt(message):
    print(message)
    while True:
        user_input = input("\n\tContinue or keep testing?\tC / T{}"
        .format(INPUT_MESSAGE))

        if user_input.lower() == 'c':
            return True
        elif user_input.lower() == 't':
            return False 
# ----------------------
'''Task 1'''
def generic_check(check, message):
    if check:
        return True
    print("\n[invalid_input: {}]".format(message))
    return False

def input_check_1(input):
    # 1. Unformatted input check
    if not generic_check('/' in input, "no division operator"):
        return False

    input_list = []
    try:
        input_list = [int(n) for n in input.replace(' ', '').split('/')]
    except ValueError:
        print("\nValueError:\t\tPlease use whole numbers as operands.")
        return False

    # 2. Formatted input check
    check_list = (
        (len(input_list) == 2, "too many operands"),
        (input_list[-1] == 0, "divisor not 0")
    )
    
    for check, message in check_list:
        if not generic_check(check, message):
            return False

    return True

def task_1():
    print('\n1. "Dividing by 0"')      
    while True:
          user_input = input('\n\tPlease try dividing any number with a 0. \
          \n\t(for example, type "5 / 0"){}'.format(INPUT_MESSAGE))

          if input_check_1(user_input):
              if prompt("\nSuccess! Unfortunately, you can't divide numbers by 0."):
                  break  
# ---------------------
'''Task 2'''
def input_check_2(input, goal):
    try:
        if int(input) < goal:
            raise ValueTooSmall 
        elif int(input) > goal:
            raise ValueTooBig
        else:
            return True
    except ValueTooSmall:
        print("\nValueTooSmall:\tThat value is too small.")
        return False
    except ValueTooBig:
        print("\nValueTooBig:\tThat value is too big.")
        return False
    except ValueError:
        print("\nValueError:\t\tThe random number is an integer.")
        return False

def task_2():
    print('\n2. "Guess the number"')
    
    no_tries = 0
    goal_number = rand.randint(1, 100)

    while True:
          user_input = input("\n\tTry guessing the random number from 1 to 100. \
          {}".format(INPUT_MESSAGE))
          no_tries += 1
          
          if input_check_2(user_input, goal_number):
              if prompt("\nNice work! You found it in {} tries.".format(no_tries)):
                  break
              else:
                  goal_number = (goal_number + rand.randint(1, 100)) % 100 
                  no_tries = 0
# ----------------------------

TASK_LIST = (task_2, )

for task in TASK_LIST:
    task()

print("\nHope you had fun. Bye!")

# -------------------------------