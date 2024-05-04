class Person:
    # constructor
    def __init__(self, name, address, email):
        print(f"{name} was born!!")
        self.name = name
        self.address = address
        self.email = email


tamas = Person(name="Tamás", address="Budapest", email="tamas@gmail.com")
print(tamas.name, tamas.address, tamas.email)

kriszta = Person(name="Kriszta", address="Pécs", email="kriszta@gmail.com")
print(kriszta.name, kriszta.address, kriszta.email)