
from datetime import datetime, timedelta
from collections import defaultdict, UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)
        
class Phone(Field):
    def __init__(self, phone):
        
        if len(phone) == 10:
            super().__init__(phone)
        else: 
            raise ValueError("Enter 10 characters.") 

class Birthday (Field):
    def __init__(self, birthday):
        birthday_date = datetime.strptime(birthday, "%d.%m.%Y")
        super().__init__(birthday_date)
    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone (self, phone):
        phone = Phone (phone)
        self.phones.append (phone)

    def remove_phone (self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove (p)
                return self.phones
        
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
        return self.phones

    def find_phone (self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return "The phone doesn't exist."
    
    def add_birthday (self, birthday):
        self.birthday = Birthday (birthday)

    def __str__(self):
        birthday_str = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "None"  # Format birthday
        phones_str = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name.value.capitalize ()}, phones: {phones_str}, birthday: {birthday_str}"

class AddressBook(UserDict):

    def add_record (self, record):
        self.data.update ({record.name.value: record})

    def find (self, name):
        if name in self.data:
            return self.data [name]
        else: 
            return "Error"

    def delete (self, name):
        del self.data [name]
        print (f"{name} is deleted.")
        for name, r in self.data.items ():
            print (f"{r} exists.")

    def get_birthdays_per_week (self):
        birthdays_per_week = defaultdict (list)
    
        today = datetime.today().date()

        for record in self.data.values ():
            name = record.name.value
            birthday = record.birthday.value
            birthday_this_year = birthday.replace (year = today.year)
            if birthday_this_year.date () < today:
                birthday_this_year = birthday_this_year.replace (year = today.year + 1)

            delta_days = (birthday_this_year.date () - today).days

            birthday_weekday = birthday_this_year.strftime ("%A")
                
            if birthday_this_year.weekday () in [5, 6]:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
                birthday_weekday = "Monday"
        
            if delta_days < 7:
                birthdays_per_week [birthday_weekday].append(name)
        
        result = ""
        for weekday, names in birthdays_per_week.items():
            formatted_names = ', '.join(name.capitalize() for name in names)
            result += f"{weekday}: {formatted_names}\n"

        return result
            #print(f"{weekday}: {', '.join(names.capitalize)}")
        #return result

           

# Створення нової адресної книги
#book = AddressBook()

    # Створення запису для John
#john_record = Record("John")
#john_record.add_phone("1234567890")
#john_record.add_phone("5555555555")
#john_record.add_birthday("09.03.1991")
    # Додавання запису John до адресної книги
#book.add_record(john_record)

    # Створення та додавання нового запису для Jane
#jane_record = Record("Jane")
#jane_record.add_phone("9876543210")
#jane_record.add_birthday("11.03.2003")
#book.add_record(jane_record)

#julia_record = Record("Julia")
#julia_record.add_phone("6666677777")
#julia_record.add_birthday ("10.09.1991")
#book.add_record(julia_record)

#mary_record = Record("Mary")
#mary_record.add_phone("4444445555")
#mary_record.add_birthday ("12.03.2005")
#book.add_record(mary_record)
    # Виведення всіх записів у книзі
#for name, record in book.data.items():
    #print(record)

#book.get_birthdays_per_week ()
    # Знаходження та редагування телефону для John
#john = book.find("John")
#john.edit_phone("1234567890", "1112223333")
#john.remove_phone ("5555555555")

#print(john)  # Виведення: Contact name: John, phones: 1112223333

    # Пошук конкретного телефону у записі John
#found_phone = john.find_phone("5555555555")
#print(f"{john.name}: {found_phone}")  # Виведення: The phone doesn't exist.
#jane = book.find ("Jane")
#found_phone = jane.find_phone ("9876543210")
#print(f"{jane.name}: {found_phone}")
    # Видалення запису Jane
#book.delete("Jane") # Виведення:  Jane is deleted.
#book.delete ("Julia") # Виведення:  Julia is deleted.
    # Виведення записів у книзі після видалення
#for name, record in book.data.items():
    #print(record)

