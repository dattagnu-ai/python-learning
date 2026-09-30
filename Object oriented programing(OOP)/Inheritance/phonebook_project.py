class Contact:

    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number

    def display(self):
        print(f"Name:- {self.name}")
        print(f"No.:- {self.phone}")


contact_1 = Contact("Dattu", "1234567890")
contact_2 = Contact("Shreya", "0987654321")
contact_3 = Contact("Rahul", "9876543210")


class PhoneBook:

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def show_contacts(self):
        for con in self.contacts:
            con.display()

    def search_contacts(self, search_name):
        found = False
        for con in self.contacts:
            if search_name.lower() == con.name.lower():
                con.display()
                found = True
                break
        if not found:
            print("Contact Not Found")

    def delete_contact(self, delete):
        found = False
        for con in self.contacts:
            if delete.lower() == con.name.lower():
                self.contacts.remove(con)
                print("Contact deleted")
                found = True
                break
        if not found:
            print("Contact Not Found")


phone = PhoneBook()
phone.add_contact(contact_1)
phone.add_contact(contact_2)
phone.add_contact(contact_3)
phone.show_contacts()
phone.search_contacts("Shreya")
phone.delete_contact("Shreya")
phone.show_contacts()
