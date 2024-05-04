class Person:
    # class attribute
    race = "human"

    def __init__(self, name):
        # Instance attribute
        self.name = name

csaba = Person("Csaba")
kriszta = Person("Kriszta")

print(csaba.name, csaba.race)
print(kriszta.name, kriszta.race)