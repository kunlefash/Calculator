from fractions import Fraction

def welcome():
    print('''
    Welcome to Kunle's Calculator
    ''')

#Define again() function to ask user if they want to calculate again
def again():
    #Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES and N for NO
''')
    #if user typer YES, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()

    #If user types in N, say good_bye to he user and end the program
    elif cal_again.upper() == 'N':
        print('Have a nice day')

    #If user types in another key, run the function again
    else:
        again()


def add_fractions(x, y):
    print('Sum of fractions: {0}'.format(x + y))


def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for modulo
''')
    number_1 = int(input('enter your first number: '))
    number_2 = int(input('Enter your second number: '))

    if operation == '+':
        print('{} + {} ='.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1,number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} '.format(number_1, number_2))
        print(number_1 / number_2)

    elif operation == '**':
        print('{} ** {}'.format(number_1, number_2))
        print(number_1 ** number_2)

    elif operation == '%':
        print('{} % {}'.format(number_1, number_2))
        print(number_1 % number_2)
    else:

        print('You have not typed a valid operator, please run the program again')


def again():
    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES and N for NO
''')
    # if user typer YES, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()

    # If user types in N, say good_bye to he user and end the program
    elif cal_again.upper() == 'Y':
        print('Have a nice day')

    # If user types in another key, run the function again
    else:
        again()

calculate()
again()