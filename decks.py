"""
decks.py
"""
from cards import *
import random

"""
Cards in deck are stored in the following format:                  
[(face, suit, value),     -> 1st card
    (face, suit, value),  -> 2nd card
        ... ]             -> nth card 
"""

def createdeck() -> list:
    deck = [(faceschars[i], s, cardsvalues[i]) for s in suitnames
                for i in range(len(cardsvalues))]
    return deck

def createplaydeck(deck: list, numdecks: int = 4) -> None:
    for i in range(0, numdecks):
        deck.extend(createdeck())
    
def shuffledeck(deck: list, numshuffle: int = 5) -> None:
    for i in range(0, numshuffle):
        random.shuffle(deck)

def clearcards(discardpile: list, playerscards: list) -> None:
    for i in range(len(playerscards)):
        discardpile.append(playerscards.pop(0))
        
def recyclecards(deck: list, discardpile: list) -> None:
    shuffledeck(discardpile)
    for i in range(len(discardpile)):
        deck.append(discardpile.pop(0))



