import os, random

class Game:
    def __init__(self):
        self.__clear_screen()

    def __clear_screen(self):
        os.system("cls")  # mac, linux = clear

    def __intro(self):
        print("*"*50, "MAGIC NUMBER GAME", "*"*50)

        print(f"Hello {self.player}! You have {self.player.credits} credits to play.")
        print("If you can guess my number you win 10 credits, otherwise you loose 10 credits")
        print("I you have no more credits the game is over.")
        print(f"I have number between 1 and {self.computer.max_number}. Can you guess it?")
        print("-"*50)

class Player:
    pass

class Computer:
    pass


Game()