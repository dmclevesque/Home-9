contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return "No such contact"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter user name"
    return inner

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} added"

@input_error
def find_contact(name):
    phone = contacts[name]
    return phone

@input_error
def update_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} updated"

@input_error
def show_all_contacts():
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result

def main():
    while True:
        command = input("Enter command: ").lower()
        if command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command.startswith("add "):
            data = command.split()
            name = data[1]
            phone = data[2]
            result = add_contact(name, phone)
            print(result)
        elif command.startswith("change "):
            data = command.split()
            name = data[1]
            phone = data[2]
            result = update_contact(name, phone)
            print(result)
        elif command.startswith("phone "):
            name = command.split()[1]
            result = find_contact(name)
            print(result)
        elif command == "show all":
            result = show_all_contacts()
            print(result)

if __name__ == "__main__":
    main()