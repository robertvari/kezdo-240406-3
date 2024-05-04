class Person:
    def __init__(self, name, phone, ballance):
        # private access level
        self.__name = name

        # private access level
        self.__phone = phone

        # private access level
        self.__ballance = ballance

        self.__email = None

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        assert isinstance(new_name, str), "Name must be of type string."
        self.__name = new_name

    def get_phone(self):
        return self.__phone

    def get_ballance(self):
        return self.__ballance

    def set_ballance(self, new_ballance):
        # todo validate new_ballance before set self.__ballance!!!
        assert isinstance(new_ballance, int), f"Ballance must be of type int."
        self.__ballance = new_ballance

    def get_email(self):
        return self.__email
    
    def set_email(self, new_email):
        assert isinstance(new_email, str), "Email must be of type string"
        assert "@" in new_email, "Email must contain @ character."

        self.__email = new_email

    def report(self):
        print("-"*50)
        print(f"\tName: {self.__name}")
        print(f"\tPhone: {self.__phone}")
        print(f"\tBallance: {self.__ballance}")
        print(f"\tEmail: {self.__email}")
        print("-"*50)

kriszta = Person("Kriszta", "06 20 123 4567", 1000)
kriszta.set_email("kriszta@gmail.com")
kriszta.report()