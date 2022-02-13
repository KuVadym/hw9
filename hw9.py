contacts = { "Joe": "123456", "Iren": "654321"}

def check_input(func):
    def wrapper(string: str) -> str:
        try:
            return func(string)
        except ValueError as e:
            print("Give me name and phone please")
        except IndexError as e:
            print("Give me all information")
        except KeyError   as e:
            print("Enter user name")
    return wrapper

@check_input
def add_command(command:str) -> str:
    name, phone = command.replace('add','').strip().split(' ')
    contacts[name] = phone
    return 'Contact add successfully'


def hello_command ():
    return "How can I help you?"

def all_number():
    x = ""
    for k, val in contacts.items(): 
        x = x + ("".join(("Phone ", k.capitalize(), " is: ", val))) + "\n"
    return x

@check_input
def phone(command:str) -> str:
    name = "".join(command.replace('phone','').strip().split(' ')).capitalize()
    result = contacts[name]
    return f"{name.capitalize()} phone is: {result}"

@check_input
def change(command:str) -> str:
    name, phone = command.replace('change','').strip().split(' ')
    contacts[name] = phone
    return f"New phone for {name.capitalize()} is: {phone}"

@check_input
def parse(command:str) -> str:
    if command.startswith('add'):
        return add_command(command)
    elif command.startswith('exit'):
        return 'exit'
    elif command.startswith('good bye'):
        return 'exit'
    elif command.startswith('close'):
        return 'exit'
    elif command.startswith('show all'):
        return all_number()         
    elif command.startswith('hello'):
        return hello_command()
    elif command.startswith('phone'):
        return phone (command)
    elif command.startswith('change'):
        return change (command)
    else:
        return "Unknown command"

def main():
    print("User help bot v 1.0.0")
    while True:
        command = input("Please, type command >>> ").lower()
        result = parse(command)
        if result == 'exit':
            print("Good bye")
            break
        if result:
            print(result)

if __name__ == '__main__':
    main()