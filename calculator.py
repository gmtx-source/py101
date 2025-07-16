import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

prompt(MESSAGES['welcome'])

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    
    return False

while True:

    prompt('This is a calculator')
    prompt('Choose a number: ')
    n1 = input()

    while invalid_number(n1):
        prompt(MESSAGES['invalid_number'])
        n1 = input()

    prompt('Choose another number: ')
    n2 = input()
    while invalid_number(n2):
        prompt(MESSAGES['invalid_number'])
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

    prompt('Would to like to perform another calculation? (y/n)? ')
    
    answer = input()
    if answer and answer[0].lower() != 'y':
        break    