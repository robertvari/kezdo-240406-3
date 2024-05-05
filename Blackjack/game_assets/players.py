import random, time

class PlayerBASE:
    def __init__(self):
        # First attributes
        self.__name = None
        self.__credits = 0
        self.__hand = []
        self.__playing = True

        # Then method calls
        self._create()

    def _create(self):
        self.__credits = random.randint(10, 100)
        self.__name = self.get_random_name()

    def _set_name(self, new_name):
        self.__name = new_name

    def init_hand(self, deck):
        self.__hand.clear()
        self.__playing = True

        self.__hand.append(deck.draw())
        self.__hand.append(deck.draw())

    def draw(self, deck):
        # Player must draw if hand value < 16 hand value > 21
        while self.__playing:
            if self.hand_value < 19:
                print(f"{self.__name} draws a card...")
                time.sleep(2)
                self.__hand.append(deck.draw())
            else:
                print(f"{self.__name} finishes.")
                self.__playing = False

    def report(self):
        print(f"{self.__name}, Hand: {self.__hand} Hand Value: {self.hand_value}")

    @property
    def hand_value(self):
        return sum([i.value for i in self.__hand])

    @staticmethod
    def get_random_name():
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"


class Player(PlayerBASE):
    def _create(self):
        super()._create()  # call to BASE._create() and get random name and credits
        # result = input("What is your name? ")  # Get player name
        self._set_name("Robert")  # call BASE._set_name() to set private __name

class AIPlayer(PlayerBASE):
    pass


if __name__ == "__main__":
    from cards import Deck

    deck = Deck()

    player = Player()
    ai_player = AIPlayer()

    player.init_hand(deck)
    ai_player.init_hand(deck)

    player.draw(deck)
    ai_player.draw(deck)

    print(player.report())
    print(ai_player.report())