class Person:
    def __init__(self, name, phone, ballance):
        # instance attributes (public)
        self.name = name

        # protected access level
        self._phone = phone

        # private access level
        self.__ballance = ballance

    def report(self):
        print("-"*50)
        print(f"\tName: {self.name}")
        print(f"\tPhone: {self._phone}")
        print(f"\tBallance: {self.__ballance}")
        print("-"*50)

kriszta = Person("Kriszta", "06 20 123 4567", 1000)
kriszta.report()