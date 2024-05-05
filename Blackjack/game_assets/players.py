class PlayerBASE:
    def __init__(self, name):
        self.__name = name
        self.__credits = 0
        self.__hand = []
        self.__playing = True

    def say_hello(self):
        print(f"Hello my name is {self.__name}")


class Player(PlayerBASE):
    pass

class AIPlayer(PlayerBASE):
    pass

if __name__ == "__main__":
    player = Player("Robert")
    ai_player = AIPlayer("Csaba")
    
    player.say_hello()
    ai_player.say_hello()