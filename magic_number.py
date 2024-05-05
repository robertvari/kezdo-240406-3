import os, random, time

class Game:
    def __init__(self):
        # First attributes
        self.__player = Player()
        self.__computer = Computer()
        self.__try_counter = 3

        # Then method calls
        self.__clear_screen()
        self.__intro()

        # todo ask for start the game
        if self.__player.ask_for_start_game(new_game=True):
            self.__start_game()
        else:
            self.__exit_game()

    def __start_game(self):
        self.__clear_screen()

        self.__try_counter = 3

        self.__computer.think_a_number()
        self.__player.think_a_number()

        while self.__player.my_number != self.__computer.my_number:
            self.__try_counter -= 1

            if self.__try_counter == 0:
                break

            print(f"Wrong guess! You have {self.__try_counter} tries left. Try again.")
            self.__player.think_a_number()
        
        # End game conditions
        if self.__player.my_number == self.__computer.my_number:
            print(f"You win! {self.__computer.my_number} was my number :)")
            # CREDITS += 10
            self.__player.give_credits(10)
            print(f"{self.__player} has {self.__player.credits} credits.")
        else:
            print(f"You lost the game :( My number was {self.__computer.my_number}")
            # CREDITS -= 10
            self.__player.take_credits(10)
            print(f"{self.__player} has {self.__player.credits} credits.")

            if self.__player.credits <= 0:
                print(f"I'm sorry {self.__player}. You lost all your credits. Game Over:(")
                time.sleep(5)
                self.__exit_game()

        # Ask for start the game
        if self.__player.ask_for_start_game(new_game=False):
            self.__start_game()
        else:
            self.__exit_game()

    def __exit_game(self):
        self.__clear_screen()
        print(f"Maybe next time {self.__player}. Have a nice day!")
        exit()

    def __clear_screen(self):
        os.system("cls")  # mac, linux = clear

    def __intro(self):
        print("*"*50, "MAGIC NUMBER GAME", "*"*50)
        
        self.__player.get_player_name()
        
        print(f"Hello {self.__player}! You have {self.__player.credits} credits to play.")
        print("If you can guess my number you win 10 credits, otherwise you loose 10 credits")
        print("I you have no more credits the game is over.")
        print(f"I have number between {self.__computer.min_number} and {self.__computer.max_number}. Can you guess it?")
        print("-"*50)

class Player:
    def __init__(self):
        self.__name = None
        self.__credits = 10
        self.__my_number = "0"
    
    @property
    def credits(self):
        return self.__credits

    @property
    def my_number(self):
        return self.__my_number

    def give_credits(self, credits):
        self.__credits += credits

    def take_credits(self, credits):
        self.__credits -= credits

    def think_a_number(self):
        self.__my_number = input("What is your guess? ")

    def get_player_name(self):
        self.__name = input("What is your name?")

    def report(self):
        print(f"Name: {self.__name}")
        print(f"Credits: {self.__credits}")

    def ask_for_start_game(self, new_game=False):
        if new_game:
            question = "Do you want to start the game?"
        else:
            question = "Do you want to play again?"

        user_input = input(f"{question} (y/n) ")
        return user_input.lower() == "y"

    def __str__(self):
        return self.__name

class Computer:
    def __init__(self):
        self.__min_number = 1
        self.__max_number = 10
        self.__my_number = "0"

    @property
    def my_number(self):
        return self.__my_number

    @property
    def min_number(self):
        return self.__min_number
    
    @property
    def max_number(self):
        return self.__max_number

    def think_a_number(self):
        self.__my_number = str(random.randint(self.__min_number, self.__max_number))


Game()