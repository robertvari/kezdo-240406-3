from game_assets.cards import Deck
from game_assets.players import AIPlayer, Player
import os, time

class Blackjack:
    def __init__(self):
        self.__clear_screen()

        # First attributes
        self.__deck = Deck()
        self.__player = Player()
        self.__players = [self.__player, AIPlayer(), AIPlayer(), AIPlayer()]

        # Then method calls
        self.__intro()

        time.sleep(5)

        self.__start_game()

    def __intro(self):
        self.__clear_screen()
        print("-"*50, "BLACKJACK", "-"*50)
        print(f"Wellcome {self.__player}. Do you know Blackjack?")
        print("This is a simple card game. Your only goal is to collect cards till your hand's value reaches 21.")

    def __start_game(self):
        self.__clear_screen()

        # Init player hands for a new game
        for player in self.__players:
            player.init_hand(self.__deck)

        # Player's rounds
        for player in self.__players:
            player.draw(self.__deck)
        
        # Player's report
        for player in self.__players:
            player.report()

    @staticmethod
    def __clear_screen():
        os.system("cls")

Blackjack()