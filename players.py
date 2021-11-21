"""
players.py

Players and their cards are stored in the following format:
 1st player
['playername1', 'playername2', ...]

"""
# Players and their cards
playersnames = []
dealer = 'Dealer'

def createplayer(name: str, monies: list,  money: int=100) -> None:
    playersnames.append(name)
    monies.append(money)

def setwagers(wagers: list, insurancewagers: list,
                  splitwagers: list, numplayer: int):
    for _ in range(numplayer):
        wagers.append(0)
        insurancewagers.append(0)
        splitwagers.append(0)
