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

Status: 
insurancestats = players' insurance status [True, False]
TODO Check whether this list is required?
splithandstats = players' split play status ['Win', 'Lost', 'Push']
TODO Check whether this list is required?
mainhandstats = players' main play status ['Win', 'Lost', 'Push']

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

# status ['', 'Win', 'Lost', 'Push']
mainhandstats: list = []
splithandstats: list = []

# False = not insured, True = insured
insurancestats: list = []

 
def placebet(bet: int, monies: list, wagers: list, 
                numplayer: int = 0, /) -> bool:
    if (monies[numplayer] > 0 and bet <= monies[numplayer]):
        wagers[numplayer] += bet
        monies[numplayer] -=  bet
        return True
    else:
        return False
    
def doublebet(monies: list, wagers: list,
                numplayer: int = 0, /) -> bool:
    if (wagers[numplayer] > 0 and monies[numplayer] >= wagers[numplayer]):
        monies[numplayer] -= wagers[numplayer]
        wagers[numplayer] = wagers[numplayer] * 2
        return True
    else:
        return False
    
def splitbet(monies: list, wagers: list, splitwagers: list, 
                 playercards: list, splitcards: list, splithandstats: list,
                     numplayer: int = 0, /) -> bool:
    splitsuccess = False
    if len(playercards[numplayer]) == 2:
        splitsuccess: bool = placebet(wagers[numplayer], monies,
                                          splitwagers, numplayer)
        splitcards[numplayer].append(playercards[numplayer].pop(-1))
        splithandstats[numplayer] = splitsuccess
    return splitsuccess

def insurancebet(bet: int, monies: list, insurancewagers: list,
              insurancestats: list, numplayer: int = 0, /) -> bool:
    if monies == 0:
        return False
    insured: bool = placebet(bet, monies, insurancewagers, numplayer)
    insurancestats[numplayer] = insured
    return insured

def insured(monies: list, insurancewagers: list,
              insurancestats: list, dealerhasbj: bool,
                    numplayer: int = 0, /) -> bool:
    insured = False
    if insurancestats[numplayer] and dealerhasbj:
        monies[numplayer] += (insurancewagers[numplayer] * 2)
        insurancewagers[numplayer] = 0
        insured = True
    else:
        insurancewagers[numplayer] = 0
        insured = False
    return insured
    
def pushbet(monies: list, wagers: list,
                numplayer: int = 0, /) -> str:
    monies[numplayer] += wagers[numplayer]
    wagers[numplayer] = 0
    
def winbet(monies: list, wagers: list,
                rate: float = 2.0, numplayer: int = 0, /) -> str:
    monies[numplayer] += int((wagers[numplayer] * rate))
    wagers[numplayer] = 0

def losebet(wagers: list, numplayer: int = 0, /) -> str:
    wagers[numplayer] = 0




