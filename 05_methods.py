class Person:
    # constructor (method)
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email

    # my method
    def say_hello(self):
        print(f"Hello! My name is {self.name}.")
    
    # my other method
    def character_sheet(self):
        print("-"*50)
        print(f"\t Name: {self.name}")
        print(f"\t address: {self.address}")
        print(f"\t email: {self.email}")
        print("-"*50)

tamas = Person(name="Tamás", address="Budapest", email="tamas@gmail.com")
tamas.character_sheet()

kriszta = Person(name="Kriszta", address="Pécs", email="kriszta@gmail.com")
kriszta.character_sheet()