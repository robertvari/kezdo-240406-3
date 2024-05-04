import os, random

class Game:
    def __init__(self):
        self.__clear_screen()
        self.__intro()

    def __clear_screen(self):
        os.system("cls")  # mac, linux = clear

    def __intro(self):
        print("*"*50, "MAGIC NUMBER GAME", "*"*50)

        print(f"Hello Player Name! You have 0 credits to play.")
        print("If you can guess my number you win 10 credits, otherwise you loose 10 credits")
        print("I you have no more credits the game is over.")
        print(f"I have number between 1 and 10. Can you guess it?")
        print("-"*50)

class Player:
    def __init__(self):
        self.__name = None
        self.__credits = 100
        self.__my_number = "0"
    
    def think_a_number(self):
        self.__my_number = input("What is your guess? ")

    def get_player_name(self):
        self.__name = input("What is your name?")

    def report(self):
        print(f"Name: {self.__name}")
        print(f"Credits: {self.__credits}")

    @property
    def my_number(self):
        return self.__my_number

    def __str__(self):
        return self.__name

class Computer:
    def __init__(self):
        self.__min_number = 0
        self.__max_number = 10
        self.__my_number = "0"

    @property
    def my_number(self):
        return self.__my_number

    def think_a_number(self):
        self.__my_number = str(random.randint(self.__min_number, self.__max_number))


# Game()

player = Player()
player.get_player_name()
player.report()