class Card():
    """
    A playing card.
    """
    def __init__(self, suit: str, rank: int) -> None:
        if not suit in ["Hearts", "Diamonds", "Clubs", "Spades", "Joker"]:
            raise ValueError("Invalid suit")
        
        if not 0 <= rank <= 13:
            raise ValueError("Invalid rank")
        
        self.__suit = suit
        self.__rank = rank

    def __str__(self) -> str:
        return f"{self.__rank} of {self.__suit}"
    
    # PROPERTIES
    @property
    def suit(self) -> str:
        return self.__suit
    
    @property
    def rank(self) -> int:
        return self.__rank
    
    # SETTERS

    # METHODS
