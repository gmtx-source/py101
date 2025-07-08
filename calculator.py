def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    
    return False

### Function new calculation
def number_calculation():

    prompt('This is a calculator')
    prompt('Choose a number: ')
    n1 = input()

    while invalid_number(n1):
        prompt("That's an invalid number... Choose another number: ")
        n1 = input()

    prompt('Choose another number: ')
    n2 = input()
    while invalid_number(n2):
        prompt("That's an invalid number... Choose another number: ")
        n2 = input()

    prompt('Choose 1) Addition, 2) Subtraction, 3) Multiplication, 4) Division')
    conta = input()

    while conta not in ['1', '2', '3', '4']:
        prompt('Must choose between "1" and "4"')
        conta = input()

    match conta:
        case '1':
            output = (int(n1) + int(n2))
        case '2':
            output = (int(n1) - int(n2))
        case '3':
            output = (int(n1) * int(n2))
        case '4':
            output = (int(n1) / int(n2))

    print(f'Result: {output}')
    return output

number_calculation()

prompt('Would you like to make another calculation? type y or n')
newcalculation = input()

while newcalculation not in ['y', 'n']:
    prompt('Invalid input insert again: ')
    newcalculation = input()

while newcalculation == 'y':
    number_calculation()
    prompt('Would you like to make another calculation? type y or n')
    newcalculation = input()

if newcalculation == 'n':
    prompt('THANKS FOR USING THE CALCULATOR')