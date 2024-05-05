from game_assets.cards import Deck
from game_assets.players import AIPlayer, Player


class Blackjack:
    def __init__(self):
        # First attributes
        self.__deck = Deck()
        self.__player = Player()
        self.__players = [self.__player, AIPlayer(), AIPlayer(), AIPlayer()]

        # Then method calls
        self.__intro()

    def __intro(self):
        self.__clear_screen()
        print("-"*50, "BLACKJACK", "-"*50)
        print(f"Wellcome {self.__player}. Do you know Blackjack?")
        print("This is a simple card game. Your only goal is to collect cards till your hand's value reaches 21.")

    @staticmethod
    def __clear_screen():
        pass

Blackjack()