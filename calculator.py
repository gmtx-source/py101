LANGUAGE = 'en'

import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

#Define the language of the text program
def messages(message, lang='en'):
    return MESSAGES[lang][message]


def prompt(key):
    message = messages(key, LANGUAGE)
    print(f"==> {message}")


def invalid_number(number_str):
    
    try:
        float(number_str)
    except ValueError:
        return True
    
    return False


while True:

    prompt('welcome')
    prompt('choose_first_number')
    n1 = input()

    while invalid_number(n1):
        prompt('invalid_number')
        n1 = input()

    prompt('choose_second_number')
    n2 = input()
    while invalid_number(n2):
        prompt('invalid_number')
        n2 = input()

    prompt('choose_operation')
    conta = input()

    while conta not in ['1', '2', '3', '4']:
        prompt('invalid_operation')
        conta = input()

    match conta:
        case '1':
            output = (float(n1) + float(n2))
        case '2':
            output = (float(n1) - float(n2))
        case '3':
            output = (float(n1) * float(n2))
        case '4':
            output = (float(n1) / float(n2))

    print(f'Result: {output}')

    prompt('another_calculation')
    
    answer = input()
    if answer and answer[0].lower() != 'y':
        break    