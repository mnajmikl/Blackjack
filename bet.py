"""
bet.py

Blackjack bettings

Common parameters:

Players money and wagers: int
monies = players' money
wagers = players' main wagers

Side wagers: int
insurancewagers = player's insurance wagers
splitwagers = player's split wagers

Cards
maincards = players' main cards
splitcards = players' split cards

Assumptions:
1. Length of all the lists above are the same
2. List has at least one entry
3. numplayer is always positive (default is 0)
4. The index of all the lists correspond with the players

"""

# Wagers and monies
monies: list = []
wagers: list = []
insurancewagers: list = []
splitwagers: list = []


def placebet(bet: int, monies: list, wagers: list, numplayer: int) -> bool:
    if (monies[numplayer] > 0 and bet <= monies[numplayer]):
        wagers[numplayer] += bet
        monies[numplayer] -=  bet
        return True
    else:
        return False

def doublebet(monies: list, wagers: list, numplayer: int) -> bool:
    if (wagers[numplayer] > 0 and monies[numplayer] >= wagers[numplayer]):
        monies[numplayer] -= wagers[numplayer]
        wagers[numplayer] = wagers[numplayer] * 2
        return True
    else:
        return False

def splitbet(monies: list, wagers: list, splitwagers: list,
                 playercards: list, splitcards: list,
                     numplayer: int) -> bool:
    splitsuccess = False
    if len(playercards[numplayer]) == 2:
        splitsuccess = placebet(wagers[numplayer], monies,
                                          splitwagers, numplayer)
        splitcards[numplayer].append(playercards[numplayer].pop(-1))
    return splitsuccess

def insurancebet(bet: int, monies: list,
                     insurancewagers: list, numplayer: int) -> bool:
    if monies == 0:
        return False
    hasinsurance = placebet(bet, monies, insurancewagers, numplayer)
    return hasinsurance

def checkforinsurance(playersnames: list, monies: list, insurancewagers: list,
                          dealerhasbj: bool, numplayer: int) -> None:
    if insurancewagers[numplayer] > 0 and dealerhasbj:
        insurancewin = insurancewagers[numplayer] * 2
        print(f"{playersnames[numplayer]} ", end='')
        print("has win insurance wagers: ${insurancewin}")
        monies[numplayer] += insurancewin
    insurancewagers[numplayer] = 0

def pushbet(playersnames: list, monies: list,
                wagers: list, numplayer: int) -> str:
    print(f"== {playersnames[numplayer]} tied. Player is pushed")
    print(f"== Return ${wagers[numplayer]} to {playersnames[numplayer]} ")
    monies[numplayer] += wagers[numplayer]
    wagers[numplayer] = 0

def winbet(playersnames: list, monies: list, wagers: list,
               numplayer: int, rate: float = 1.0, /) -> None:
    print(f"== {playersnames[numplayer]} wins.")
    win = int((wagers[numplayer] * rate))
    monies[numplayer] += (wagers[numplayer] + win)
    print(f"== {playersnames[numplayer]} has win $ {win}.")
    wagers[numplayer] = 0

def losebet(playersnames: list, wagers: list, numplayer: int) -> None:
    print(f"== {playersnames[numplayer]} busted and lost.")
    print(f"== {playersnames[numplayer]} has lost ${wagers[numplayer]}")
    wagers[numplayer] = 0




