import sys
import os
import time

import calc_operations


def validate(*kwd):
    for item in kwd:
        try:
            int(item)
        except Exception, detail:
            print detail
            return False
    return True


def screen1():
    os.system('cls')
    print(''.center(80, '*'))
    print(' MAIN MENU '.center(80, '*'))
    print(''.center(80, '*'))
    print('1. Simple Calculator')
    print('2. Scientific Calculator')
    print('3. Exit')
    option = raw_input("Enter your option: ")
    if option == '1':
        screen2()
    elif option == '2':
        screen3()
    elif option == '3':
        print(' THANK YOU '.center(80, '*'))
        print('Exiting ...')
        time.sleep(2)
        sys.exit(0)
    else:
        print('Invalid option. Choose 1, 2, 3 only.'.center(80, ' '))
        print('Try again in 4 secs ...'.center(80, ' '))
        time.sleep(4)
        screen1()


def screen2():
    os.system('cls')
    print(''.center(80, '*'))
    print(' SIMPLE CALCULATOR '.center(80, '*'))
    print(''.center(80, '*'))
    print('1. Add (a,b)')
    print('2. Subtract (a,b)')
    print('3. Divide (a,b)')
    print('4. Multiply (a,b)')
    print('5. Go back to Main Menu')
    option = raw_input("Enter your option: ")
    if option == '1':
        print(''.center(80, '-'))
        operand1 = raw_input("Enter your first operand: ")
        operand2 = raw_input("Enter your second operand: ")
        validation_result = validate(operand1, operand2)
        if validation_result:
            operand1 = int(operand1)
            operand2 = int(operand2)
            result = calc_operations.add(operand1, operand2)
            print(' Result '.center(80, '*'))
            print(str(result).center(80, ' '))
            print(''.center(80, '*'))
        else:
            print('Invalid inputs. Try again.')
        print('Refreshing...')
        time.sleep(1)
        screen2()

    elif option == '2':
        print(''.center(80, '-'))
        operand1 = raw_input("Enter your first operand: ")
        operand2 = raw_input("Enter your second operand: ")
        validation_result = validate(operand1, operand2)
        if validation_result:
            operand1 = int(operand1)
            operand2 = int(operand2)
            result = calc_operations.subtract(operand1, operand2)
            print(' Result '.center(80, '*'))
            print(str(result).center(80, ' '))
            print(''.center(80, '*'))
        else:
            print('Invalid inputs. Try again.')
        print('Refreshing...')
        time.sleep(1)
        screen2()

    elif option == '3':
        print(''.center(80, '-'))
        operand1 = raw_input("Enter your first operand: ")
        operand2 = raw_input("Enter your second operand: ")
        validation_result = validate(operand1, operand2)
        if validation_result:
            operand1 = int(operand1)
            operand2 = int(operand2)
            result = calc_operations.multiply(operand1, operand2)
            print(' Result '.center(80, '*'))
            print(str(result).center(80, ' '))
            print(''.center(80, '*'))
        else:
            print('Invalid inputs. Try again.')
        print('Refreshing...')
        time.sleep(1)
        screen2()

    elif option == '4':
        print(''.center(80, '-'))
        operand1 = raw_input("Enter your first operand: ")
        operand2 = raw_input("Enter your second operand: ")
        validation_result = validate(operand1, operand2)
        if validation_result:
            operand1 = int(operand1)
            operand2 = int(operand2)
            result = calc_operations.divide(operand1, operand2)
            print(' Result '.center(80, '*'))
            print(str(result).center(80, ' '))
            print(''.center(80, '*'))
        else:
            print('Invalid inputs. Try again.')
        print('Refreshing...')
        time.sleep(1)
        screen2()

    elif option == '5':
        print(' Returning to main menu ... '.center(80, '*'))
        time.sleep(2)
        screen1()

    else:
        print('Invalid option. Choose 1, 2, 3, 4, 5 only.'.center(80, ' '))
        print('Try again in 4 secs ...'.center(80, ' '))
        time.sleep(4)
        screen2()


def screen3():
    os.system('cls')
    print(''.center(80, '*'))
    print(' SCIENTIFIC CALCULATOR '.center(80, '*'))
    print(''.center(80, '*'))
    print('1. Sine (a)')
    print('2. Cosine (a)')
    print('3. Power (a, b)')
    print('4. Square root (a)')
    print('5. Go back to Main Menu')
    option = raw_input("Enter your option: ")
    if option == '1':
        print(''.center(80, '-'))
        operand1 = raw_input("Enter your first operand: ")
        validation_result = validate(operand1)
        if validation_result:
            operand1 = int(operand1)
            result = calc_operations.sine(operand1)
            print(' Result '.center(80, '*'))
            print(str(result).center(80, ' '))
            print(''.center(80, '*'))
        else:
            print('Invalid inputs. Try again.')
        print('Refreshing...')
        time.sleep(1)
        screen3()

    elif option == '2':
        print(''.center(80, '-'))
        operand1 = raw_input("Enter your first operand: ")
        validation_result = validate(operand1)
        if validation_result:
            operand1 = int(operand1)
            result = calc_operations.cosine(operand1)
            print(' Result '.center(80, '*'))
            print(str(result).center(80, ' '))
            print(''.center(80, '*'))
        else:
            print('Invalid inputs. Try again.')
        print('Refreshing...')
        time.sleep(1)
        screen3()

    elif option == '3':
        print(''.center(80, '-'))
        operand1 = raw_input("Enter your first operand: ")
        operand2 = raw_input("Enter your second operand: ")
        validation_result = validate(operand1, operand2)
        if validation_result:
            operand1 = int(operand1)
            operand2 = int(operand2)
            result = calc_operations.power(operand1, operand2)
            print(' Result '.center(80, '*'))
            print(str(result).center(80, ' '))
            print(''.center(80, '*'))
        else:
            print('Invalid inputs. Try again.')
        print('Refreshing...')
        time.sleep(1)
        screen3()

    elif option == '4':
        print(''.center(80, '-'))
        operand1 = raw_input("Enter your first operand: ")
        validation_result = validate(operand1)
        if validation_result:
            operand1 = int(operand1)
            result = calc_operations.squareroot(operand1)
            print(' Result '.center(80, '*'))
            print(str(result).center(80, ' '))
            print(''.center(80, '*'))
        else:
            print('Invalid inputs. Try again.')
        print('Refreshing...')
        time.sleep(1)
        screen3()

    elif option == '5':
        print(' Returning to main menu ... '.center(80, '*'))
        time.sleep(2)
        screen1()

    else:
        print('Invalid option. Choose 1, 2, 3, 4, 5 only.'.center(80, ' '))
        print('Try again in 4 secs ...'.center(80, ' '))
        time.sleep(4)
        screen3()

screen1()
