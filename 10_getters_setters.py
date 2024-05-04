class Person:
    def __init__(self, name, phone, ballance):
        # private access level
        self.__name = name

        # private access level
        self.__phone = phone

        # private access level
        self.__ballance = ballance

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def report(self):
        print("-"*50)
        print(f"\tName: {self.__name}")
        print(f"\tPhone: {self.__phone}")
        print(f"\tBallance: {self.__ballance}")
        print("-"*50)

kriszta = Person("Kriszta", "06 20 123 4567", 1000)
print(kriszta.get_name())