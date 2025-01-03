from .deck import Deck
from .game import Game

class Player():
    """
    A player in the game.
    """
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__hand = []
    
    def __str__(self) -> str:
        return f"{self.__name} has {len(self.__hand)} cards"
    
    # PROPERTIES
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def hand(self) -> list:
        return self.__hand
    
    # SETTERS
    
    # METHODS
    def draw(self, deck: Deck, quantity: int = 1) -> None:
        """
        Draw a card from the deck and add it to hand.
        """
        for _ in range(quantity):
            card = deck.draw()
            self.__hand.append(card)

    def score(self, game: Game) -> int:
        """
        Count the number of rounds won.
        """
        return game.round_winners.count(self)
        