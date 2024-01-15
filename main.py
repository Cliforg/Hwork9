def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print('Enter a valid command')
        except ValueError:
            print('Enter phone and(or) number')
        except IndexError:
            print('Vrong value')
            
    return inner

phone_book ={}

@input_error
def add(user_input):
    user_input = user_input.split()
    global phone_book
    phone_book[user_input[1]] = user_input[2]
    print(phone_book)
    print (f'Adding a new contact with name {user_input[1]} and phone number {user_input[2]}')
    
@input_error
def hello():
    return 'How can i help you?'

@input_error
def change(user_input):
    user_input = user_input.split()
    if user_input[1] in phone_book:
        phone_book[user_input[1]] = user_input[2]
        print(f'New number for contact {user_input[1]} is {user_input[2]}')

@input_error
def phone(user_input):
    user_input = user_input.split()
    print(f'Number for contact {user_input[1]} is {phone_book.get(user_input[1])}')   

@input_error
def show_all():
    if not phone_book:
        print('Phone book is empty')
    else:
        result = "\n".join(f"{name}: {phone}" for name, phone in phone_book.items())
        return result



def main():
    print('I know commands: "hello", "add ", "change ", "phone ", "show all", "good bye", "close", "exit"')
    while True:
        user_input = input('Enter a command: ').lower()
        if user_input == '.' or user_input == 'good bye' or user_input == 'close' or user_input == 'exit':
            print('Good bye!')
            break
        elif user_input == 'hello':
            hello
            print(hello())
            continue
        elif user_input.startswith('add'):
            add(user_input)
        elif user_input.startswith('phone'):
            phone(user_input)
        elif user_input.startswith('change'):
            change(user_input)
        elif user_input.startswith('show'):
            print(show_all())
        # else:
        #     print('Invalid command. Try again')
            

            
    
if __name__ == '__main__':   
    main() 
    
    
    
    
    
   

    