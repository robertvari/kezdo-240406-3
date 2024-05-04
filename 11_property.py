class Person:
    def __init__(self, name):
        self.__name = name
        self.__phone = "06 20 123 4567"
        self.__ballance = 1000
        self.__email = "kriszta@gmail.com"

    @property
    def phone(self): 
        return self.__phone
    
    @property
    def ballance(self): 
        return self.__ballance
    
    @ballance.setter
    def ballance(self, new_ballance):
        assert isinstance(new_ballance, int), "Ballance must be of type int"
        self.__ballance = new_ballance
    
    @property
    def name(self): 
        return self.__name
    
    @property
    def email(self):
        return self.__email

    def report(self):
        print("-"*50)
        print(f"\tName: {self.__name}")
        print(f"\tPhone: {self.__phone}")
        print(f"\tBallance: {self.__ballance}")
        print(f"\tEmail: {self.__email}")
        print("-"*50)


kriszta = Person("Kriszta")
kriszta.ballance = 10000
print(kriszta.name, kriszta.phone, kriszta.ballance, kriszta.email)