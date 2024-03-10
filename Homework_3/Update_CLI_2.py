from Function import AddressBook, Phone, Record, Birthday

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter a valid date in the format DD.MM.YYYY!"
        except KeyError:
            return "Contact doesn`t exist."
        except IndexError:
            return "No contacts found."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name].add_phone(phone)  # додавання нового номера до існуючого контакту
        return "Phone added successfully!"
    else:
        try:
            phone_obj = Phone(phone)  # перевірка телефону
            record = Record(name)
            record.add_phone(phone_obj.value)  # додаємо перевірений номер до запису
            contacts.add_record(record)
            return "Contact added successfully!"
        except ValueError as e:
            return str(e)
    

@input_error
def change_contact(args, contacts):
    name, old_phone, new_phone = args
    if name in contacts:
        contacts[name].edit_phone(old_phone, new_phone)
        return "Contact changed successfully!"
    else:
        raise ValueError #("Enter Name old-number new-number!")
 
    
@input_error 
def show_phone (args, contacts):
    name = args[0]
    record = contacts.find(name) # пошук по імені
    if record != "Error":
        phones = [phone.value for phone in record.phones]
        if phones:
            return ', '.join(phones)
        else:
            return "No phone number found for the contact!"
    else:
        raise KeyError #("Contact doesn't exist!")

    
@input_error  
def show_all_contacts (contacts):
    result = ""
    if contacts:
        for name, record in contacts.items():
            result += str(record) + "\n"
    else:
        raise IndexError #("No contacts found!")
    return result
    

@input_error
def add_birthday(args, contacts):
    name, birthday = args
    birthday_o = Birthday(birthday)  # перевірка формату дати
    if name in contacts:
        contacts[name].add_birthday(birthday)  # додаємо дату
        return "Birthday added successfully!"
    else:
        raise KeyError #("Contact doesn't exist!")
    
@input_error 
def show_birthday (args, contacts):
    name = args[0]
    record = contacts.find(name) #пошук по імені
    if record:
        return record.birthday.value.strftime("%d.%m.%Y")
    else:
        raise KeyError #("Contact doesn't exist.")

def main():
    contacts = AddressBook ()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input.lower ())

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact (args, contacts))
        elif command == "phone":
            print (show_phone (args, contacts))
        elif command == "all":
            print (show_all_contacts (contacts))
        elif command == "add-birthday":
            print (add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays": 
            print(contacts.get_birthdays_per_week())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

