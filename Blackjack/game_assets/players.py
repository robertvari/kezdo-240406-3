import random

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

    @staticmethod
    def get_random_name():
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"


class Player(PlayerBASE):
    def _create(self):
        super()._create()  # call to BASE._create() and get random name and credits
        result = input("What is your name? ")  # Get player name
        self._set_name(result)  # call BASE._set_name() to set private __name

class AIPlayer(PlayerBASE):
    pass


if __name__ == "__main__":
    player = Player()
    ai_player = AIPlayer()

    pass