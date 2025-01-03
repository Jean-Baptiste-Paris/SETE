from .card import Card
import random

class Deck():
    """
    A deck of playing cards.
    """
    def __init__(self) -> None:
        self.__cards = []

    def __str__(self) -> str:
        return f"{len(self.__cards)} cards in the deck"
    
    # PROPERTIES
    @property
    def cards(self) -> list:
        return self.__cards
    
    # SETTERS

    # METHODS
    def shuffle(self) -> None:
        """
        Shuffle the deck.
        """
        random.shuffle(self.__cards)

    def draw(self) -> Card:
        """
        Draw a card from the deck.
        """
        return self.__cards.pop(0)
    
    def resetAndShuffle(self) -> None:
        """
        Reset the deck.
        """
        self.__cards = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for rank in range(1, 14):
                self.__cards.append(Card(suit, rank))
        for _ in range(2):
            self.__cards.append(Card("Joker", 0))
        self.shuffle()