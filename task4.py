
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == "show_phone" and args[0]:
                return "Enter only ONE argument for the command"
            return "Enter the argument for the command"
        except KeyError:
            return "Contact doesn't exist."
        except KeyboardInterrupt:
            return "Enter command correct way"
        except ValueError:
            return "Enter command correct way"

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    # перевіряємо чи контакт існує якщо ТАК тоді нічого не змінюємо
    if name in contacts.keys():
        return "Contact alredy exist."
    contacts[name] = phone
    return "Contact added."

@input_error    
def change_contact(args, contacts):
    name, phone = args
    # перевіряємо чи контакт має цей самий номер
    if contacts[name] != phone:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact alredy have this number."

@input_error   
def show_phone(args, contacts):
    name, = args
    # перевіряємо чи контакт існує в списку і повертаємо одразу значення
    return contacts.get(name)
    
@input_error   
def show_all(args, contacts):
    # тут я вирішив зробити перевірку якщо до команди додано будь-які аргументи то вона не працює коректно
    if not args:
        return contacts
    else:
        return "Command don't recive any arguments. Example: 'all'"





def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()