"""
game.py
"""

from actions import *
from bet import *
from cards import *
from decks import *
from players import *

deck = []
discardpile = []
dealercards = []
maincards = []
splitcards = []

def startgame(deck: list, playersnames: list, monies: list,
                      wagers: list, insurancewagers: list, splitwagers: list,
                                  numplayer: int, money: int=100) -> None:
    for i in range(numplayer):
        createplayer(f"Player #{i + 1}", monies, wagers,
                         insurancewagers, splitwagers)
    createplaydeck(deck)
    shuffledeck(deck)

def startbets(playersnames: list, monies: list,
                  wagers: list, numplayer: int) -> None:
    for idx, p in enumerate(playersnames):
        while True:
            try:
                print(f"\n== {p} to bet")
                print(f"== {p} have ${monies[idx]}")
                bet = int(input("Enter bet amount : "))
                if placebet(bet, monies, wagers, idx):
                    print(f"== {p} has placed ${bet} bet\n")
                    break
                else:
                    print("Please enter a valid bet value larger than 0).")
            except ValueError:
                print("Please enter integer only.")
                pass

def drawinitalcards(deck: list, playersnames: list,
                        playerscards: list, dealercards: list) -> None:
    playerscards.clear()
    # Create a temporary list of tuples [[], [], ...]
    # with the number of players
    tempcard = [[() for c in range(2)] for i in range(len(playersnames))]

    # clear the elements in the sublists
    for idx, r in enumerate(tempcard):
        r.clear()

    dealercards.clear()
    # Append a card from the deck for each player and dealer
    for n in range(2):
        dealercards.append(deck.pop(0))
        for i, c in enumerate(tempcard):
            c.append(deck.pop(0))
    # Extend the playerscards with a copy of the temporary list
    playerscards.extend(tempcard.copy())

def buildsplitcards(playersnames: list, splitcards: list) -> None:
    splitcards.clear()
    tempcard = [[() for c in range(1)] for i in range(len(playersnames))]
    for idx, r in enumerate(tempcard):
        r.clear()
    splitcards.extend(tempcard.copy())

def askforinsurance(dealercards: list, playersnames: list,
                        monies: list, wagers: list,
                            insurancewagers: list) -> None:
    prompt  = "Enter amount (less or equal than wagers)"
    prompt += "Enter 0 if you do not want insurance"
    if dealercards[1][0] == 'A':
        print("\nDealer has an open card Ace.")
        print("Do you want to have an insurance?\n")
        for idx, p in enumerate(playersnames):
            while True:
                try:
                    print(f"== {p} to put insurance.")
                    print(f"== {p} have: ${monies[idx]}")
                    print(f"== {p}'s current bet: ${wagers[idx]}")
                    print(prompt)
                    bet = int(input("Your insurance bet: "))
                    if bet == 0:
                        print(f"== {p} do not want to have insurance\n")
                        break
                    elif bet > 0 and bet <= wagers[idx]:
                        if monies[idx] > bet:
                            if insurancebet(bet, monies, insurancewagers, idx):
                                print(f"== {p} has placed ${bet} bet\n")
                                break
                        else:
                            print(f"== {p} does not have enough money for insurance\n")
                            break
                    else:
                        print("Please enter a valid bet value.")
                        print("Insurance must be equal or less than current wager")
                        print(f"Current wager is: ${wagers[idx]}")
                except ValueError:
                    print("Please enter integer only.")
                    pass
    else:
        print("Dealer will not ask for insurance.\n")

def askforsplit(playersnames: list, playerscards: list,
                monies: list, wagers: list, splitcards: list,
                splitwagers: list) -> None:

    for idx, p in enumerate(playersnames):
        if (len(playerscards[idx]) == 2 and
            (playerscards[idx][0][0] == playerscards[idx][1][0])
                and wagers[idx] > 0):
            while True:
                print(f"{p} hands:")
                printhands(playerscards[idx])
                showplayerhandvalue(p, playerscards[idx])
                print(f"\n== {p} have two cards with the same face")
                takesplit = input("== Do you want to split? (Y/N): ")
                if takesplit.upper() == 'N':
                    print(f"== {p} do not want split cards")
                    break
                elif takesplit.upper() == 'Y':
                    if monies[idx] >= wagers[idx]:
                        if splitbet(monies, wagers, splitwagers,
                                        playerscards, splitcards, idx):
                            print(f"{p} has split cards with ${wagers[idx]} bet\n")
                            break
                        break
                    else:
                        print(f"Your do not have enough money to split")
                        print(f"You currently have: ${monies[idx]}")
                        print(f"Your current wager: ${wagers[idx]}")
                        break
                else:
                    print("Invalid choice")

def playeractions(deck: list, dealercards: list, playersnames: list,
                    playerscards: list, splitcards: list, monies: list,
                    wagers: list, splitwagers: list) -> None:
    for idx, p in enumerate(playersnames):
        print(f"\nCurrent player {p} hands:")
        showhandandvalueafteraction(p, playerscards[idx])
        if playerhandvalue(playerscards[idx]) < 21:
            while True:
                if playerhandvalue(playerscards[idx]) >= 21:
                    break
                try:
                    print(f"\nCurrent player: {p}")
                    showplayerhandvalue(p, playerscards[idx])
                    action = int(input("Choose: [0 - Stand | 1 - Hit] : "))
                    if action == 0:
                        stand(p)
                        break
                    elif action == 1:
                        hit(deck, p, playerscards, idx)
                    else:
                        print("Please enter a number 0 or 1 only.")

                except ValueError:
                    print("Value entered is not an a number.")
                    print("Please enter a number 0 or 1 only.")
                showhandandvalueafteraction(p, playerscards[idx])

            if len(splitcards[idx]) > 0:
                showhandandvalueafteraction(p, playerscards[idx])
                splitaction(deck, p, splitcards, idx)
        else:
            pass

def splitaction(deck: list, playername: str,
                     splitcards: list, numplayer: int) -> None:
    print(f"\nCurrent player {playername} split hands:")
    printhands(splitcards[numplayer])
    if (len(splitcards[numplayer]) > 0):
        if playerhandvalue(splitcards[numplayer]) < 21:
            while True:
                if playerhandvalue(splitcards[numplayer]) >= 21:
                    break
                try:
                    print(f"\nSplit cards: Current player: {playername}")
                    action = int(input(f"Split: [0 - Stand | 1 - Hit]: "))
                    if action == 0:
                        stand(playername)
                        showplayerhandvalue(playername, splitcards[numplayer])
                        break
                    elif action == 1:
                        hit(deck, playername, splitcards, numplayer)
                        showplayerhandvalue(playername, splitcards[numplayer])
                        printhands(splitcards[numplayer])
                    else:
                        print("Please enter a number 0 or 1 only.")
                except ValueError:
                    print("Value entered is not an a number.")
                    print("Please enter a number 0 or 1 only.")
        print(f"{playername} split hands")
        showhandandvalueafteraction(playername, splitcards[numplayer])
    else:
        pass

def finalizeround(deck: list, discard: list, playerscards: list,
                      splitcards: list, dealercards: list) -> None:

    if len(playerscards) > 0:
        for i in range(len(playerscards)):
            clearcards(discardpile, playerscards[i])
    if len(splitcards) > 0:
        for i in range(len(splitcards)):
            clearcards(discardpile, splitcards[i])
    if len(dealercards) > 0:
        clearcards(discardpile, dealercards)

    if len(deck) <= ((len(playersnames) * 2) + 2):
        recyclecards(deck, discardpile)

    print(f"There are {len(deck)} cards left in the play deck.")
    print(f"{len(discardpile)} cards have been discarded.\n")


def playagain() -> bool:
    while True:
        replay = input("Play again? (Y/N): ")
        if replay.upper() == "N":
            return False
        elif replay.upper() == "Y":
            return True
        else:
            print("Please enter Y for YES or N for NO only")

