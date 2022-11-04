# Your ToDo: Provide Docstring for every function

def print_menu():
    while True:
        print('\n\nMenu:')
        print('Enter 1 to sum numbers from 1 to N')
        print('Enter 2 to evaluate simple 2 numbers expression (e.g. 2 + 3)')
        print('Enter 3 to end the program')

        user_inp = input('\nEnter choice from 1 to 3: ')

        if user_inp != '1' and user_inp != '2' and user_inp != '3':
            print('Invalid Input...Try again')
            continue
        else:
            return user_inp


def sum_1_to_n():
    n = int(input('Enter a number: '))
    sum = (n * (n+1))//2
    print('Sum from 1 to', n, 'is', sum)


def divide(num1, num2, operation):
    # / or //

    #  See this function prints nothing. This is a better design
    # It is only responsible to compute answer if possible
    # someone else should print

    if num2 == 0:
        result = None
    elif operation == '/':
        result = num1 / num2
    else:
        result = num1 // num2

    return result


def expression():
    num1, operation, num2 = input('Enter a simple expression: ').split()
    num1, num2 = float(num1), float(num2)

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '**':
        result = num1 ** num2
    else:
        result = divide(num1, num2, operation)

    if result != None:
        print('Expression value is ', result)
    else:
        print('Sorry: No way to compute this expression')


def calculator_interface():
    while True:
        user_inp = print_menu()

        if user_inp == '1':
            sum_1_to_n()
        elif user_inp == '2':
            expression()
        else:
            break


calculator_interface()

