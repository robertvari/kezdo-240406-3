class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"Hello! My name is {self.name}"
    
    def __repr__(self) -> str:
        return self.name


csaba = Person("Csaba")
kriszta = Person("Kriszta")

my_friends = [csaba, kriszta]
print(my_friends)
print(csaba)