class Student:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__scores = [3, 5, 4, 4, 5, 2, 1, 4, 5, 5]

    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"
    
    @property
    def average(self):
        return sum(self.__scores) / len(self.__scores)

kriszta = Student("Kiss", "Krisztina")
print(kriszta.full_name, kriszta.average)