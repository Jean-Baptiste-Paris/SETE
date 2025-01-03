from .card import Card
from .player import Player
from .deck import Deck
from .rule_manager import RuleManager

class Game():
    """
    The rule manager for the game.
    """
    def __init__(self, players: list["Player"], deck: Deck, rules: RuleManager) -> None:
        self.__players = players
        self.__deck = deck
        self.__rules = rules
        self.__round_winners = set()
        self.__played_cards = list()

    def __str__(self) -> str:
        return f"{len(self.__players)} players, round {len(self.__round_winners) + 1}"
    
    
    # PROPERTIES
    @property
    def players(self) -> set:
        return self.__players
    
    @property
    def deck(self) -> Deck:
        return self.__deck
    
    @property
    def rules(self) -> RuleManager:
        return self.__rules
    
    @property
    def round_winners(self) -> list:
        return self.__round_winners
    
    @property
    def played_cards(self) -> list:
        return self.__played_cards
    
    # SETTERS

    # METHODS
    def start_round(self) -> None:
        """
        Start a round of the game.
        """
        self.__deck.resetAndShuffle()   # Initialize the deck

        for player in self.__players:   # Draw 7 cards for each player
            player.draw(self.__deck, 7)

        card = self.__deck.draw()       # Put the first card into play
        self.played_cards.append(card)
        
        
    def end_round(self, winner: Player) -> None:
        """
        End the current round.
        """
        pass

    def top_card(self) -> Card:
        """
        Return the top card in play.
        """
        return self.__played_cards[-1]
