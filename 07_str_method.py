class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"Hello! My name is {self.name}"


csaba = Person("Csaba")
kriszta = Person("Kriszta")

print(csaba)
print(kriszta)