# Define a class
class Person:
    # class attributes
    name = None
    address = None
    email = None


# Instance of the Person class
balazs = Person()
tamas = Person()
kriszta = Person()

balazs.name = "Balázs"
balazs.address = "Budapest"
balazs.email = "balazs@email.com"
print(balazs.name, balazs.address, balazs.email)

tamas.name = "Tamás"
tamas.address = "Pécs"
tamas.email = "tamas@email.com"
print(tamas.name, tamas.address, tamas.email)

kriszta.name = "Kriszta"
kriszta.address = "Miskolc"
kriszta.email = "kriszta@email.com"
print(kriszta.name, kriszta.address, kriszta.email)