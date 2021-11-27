"""
actions.py

Players' actions
"""

from players import *
from bet import *
from decks import *

def showplayerhandvalue(playername: str, playercards: list) -> None:
    val = playerhandvalue(playercards)
    if val == 21:
        print(f"\n{playername} hand value: {val:2}!")
        if isblackjack(playercards):
            print(f"\n{playername} has Blackjack!")
    elif val > 21:
        print(f"\n{playername} hand value: {val:2} - BUSTED!")
    else:
        print(f"\n{playername} hand value: {val:2}")

def showdealerhandvalue(dealername: str, dealercards: list) -> None:
    val = playerhandvalue(dealercards)
    if val == 21:
        print(f"\n{dealername} hand value: {val:2}!")
        if isblackjack(dealercards):
            print(f"\n{dealername} has Blackjack!")
    elif val > 21:
        print(f"\n{dealername} hand value: {val:2}")
    else:
        print(f"\n{dealername} hand value: {val:2}")

def showdealerhands(dealer: str, dealercards: list) -> None:
    if len(dealercards) > 0:
        print(f"\n{dealer} cards: ")
        printholecard()
        printhands(dealercards, start=1)

def showallhands(name: str, playercards: list):
    print(f"\n{name}'s hands")
    printhands(playercards)

def stand(playername: str) -> None:
    print(f"== {playername} stands.")

def hit(deck: list, playername: str, playercards: list,
            numplayer: int) -> None:
    if len(deck) > 0:
        newcard = deck.pop(0)
        playercards[numplayer].append(newcard)
        print(f"== {playername} hits.")
        print(f"== New card: {newcard[0]} of {newcard[1]}")

def dealerhit(deck: list, dealer: str, dealercards: list) -> None:
    if len(deck) > 0:
        newcard = deck.pop(0)
        dealercards.append(newcard)
        print(f"== {dealer} hits.")
        print(f"== New card: {newcard[0]} of {newcard[1]}")

def isblackjack(playercards: list) -> bool:
    isbj = False
    if len(playercards) == 2:
        if playercards[0][2] == 10 and playercards[1][0] == 'A':
            isbj = True
        if playercards[1][2] == 10 and playercards[0][0] == 'A':
            isbj = True
    return isbj

def playerhandvalue(playercards: list) -> int:
    playerhandvalue = 0
    aceexists = False
    for L in range(0, len(playercards)):
        playerhandvalue += playercards[L][2]
        if playercards[L][0] == 'A':
            aceexists = True
    # Player has two card and one of them is an Ace
    # Add 10 as Ace is 1 by default
    if aceexists and len(playercards) == 2:
        playerhandvalue += 10
    return playerhandvalue

def showhandandvalueafteraction(playername: str,
                                playercards: list) -> None:

    showplayerhandvalue(playername, playercards)
    printhands(playercards)

def dealeraction(deck: list, playername: str, dealercards: list) -> None:
    print(f"\n{playername} turn")
    if playerhandvalue(dealercards) == 21:
        stand(playername)
    elif playerhandvalue(dealercards) == 17:
        stand(playername)
    elif playerhandvalue(dealercards) < 17:
        while playerhandvalue(dealercards) < 17:
            dealerhit(deck, playername, dealercards)
            maxtop = 17 + random.randint(0, 3)
            if (playerhandvalue(dealercards) >= 21 or
                    playerhandvalue(dealercards) >= maxtop):
                stand(playername)
                break
    else:
        pass
    showhandandvalueafteraction(playername, dealercards)

def determinewinner(playersnames: list, dealercards: list, playercards: list,
                         monies: list, wagers: list, numplayer: int) -> None:
    if len(playercards[numplayer]) == 0:
        return
    
    showhandandvalueafteraction(playersnames[numplayer], playercards[numplayer])

    if playerhandvalue(playercards[numplayer]) > 21:
        losebet(playersnames, wagers, numplayer)

    elif (playerhandvalue(playercards[numplayer]) <= 21 and
                                        playerhandvalue(dealercards) <= 21):
        if (playerhandvalue(playercards[numplayer]) <
                    playerhandvalue(dealercards)):
            losebet(playersnames, wagers, numplayer)

        elif (playerhandvalue(playercards[numplayer]) >
                  playerhandvalue(dealercards)):
            winrate = (3 / 2) if isblackjack(playercards[numplayer]) else 1.0
            winbet(playersnames, monies, wagers, numplayer, winrate)

        elif (playerhandvalue(playercards[numplayer]) ==
                  playerhandvalue(dealercards)):
            pushbet(playersnames, monies, wagers, numplayer)

    elif playerhandvalue(playercards[numplayer]) <= 21:
        if playerhandvalue(dealercards) > 21:
            winrate = (3 / 2) if isblackjack(playercards[numplayer]) else 1.0
            winbet(playersnames, monies, wagers, numplayer, winrate)

    else:
        pass
    checkforinsurance(playersnames, monies, insurancewagers,
                          isblackjack(dealercards), numplayer)
