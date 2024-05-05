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

    @property
    def playing(self):
        return self.__playing
    
    @playing.setter
    def playing(self, new_playing):
        self.__playing = new_playing

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

    @property
    def hand(self):
        return ", ".join([card.name for card in self.__hand])

    @staticmethod
    def get_random_name():
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def __str__(self):
        return self.__name


class Player(PlayerBASE):
    def _create(self):
        super()._create()  # call to BASE._create() and get random name and credits
        result = input("What is your name? ")  # Get player name
        self._set_name(result)  # call BASE._set_name() to set private __name

    def draw(self, deck):
        print(f"This is your turn {self.__name}!")

        while self._playing:
            print(f"Your hand: {self.hand}")
            print(f"Your hand value: {self.hand_value}")

            response = input("Do you want to draw a card? (y/n)")

            if response.lower() == "y":
                new_card = deck.draw()
                print(f"You new card: {new_card}")
                self._add_card_to_hand(new_card)
                time.sleep(3)
            else:
                self._playing = False

class AIPlayer(PlayerBASE):
    pass


if __name__ == "__main__":
    from cards import Deck

    deck = Deck()

    player = Player()
    ai_player = AIPlayer()

    player.init_hand(deck)
    ai_player.init_hand(deck)