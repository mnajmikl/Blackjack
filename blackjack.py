"""
blackjack.py
"""

from time import sleep
from game import *

def main():
    # 1. Initialize the game elements
    startgame(playersnames, monies, 4)
    setwagers(wagers, insurancewagers, splitwagers, 4)
    setcards(deck)
    while True:
        # 2. Start betting
        startbets(playersnames, monies, wagers, len(playersnames) - 1)
        # 3. Draw two cards for all players and dealer
        # 3a. Build split cards list
        drawinitalcards(deck, playersnames, maincards, dealercards)
        buildsplitcards(playersnames, splitcards)
        # 4. Show dealer's hand with a hole card
        showdealerhands(dealer, dealercards)
        # 4a. Ask for insurance bet if face card is Ace
        askforinsurance(dealercards, playersnames, monies,
                        wagers, insurancewagers)
        sleep(2)
        # Split rig code
        # maincards[0][0] = ('8', 'Clubs', 8)
        # maincards[0][1] = ('8', 'Spades', 8)
        # 5. Ask to split if any player has twin cards
        askforsplit(playersnames, maincards, monies, wagers,
                        splitcards, splitwagers)
        # 5a. Player actions: hit or stand
        playeractions(deck, dealercards, playersnames, 
                        maincards, splitcards)
        # 6. Dealer's action
        sleep(2)
        dealeraction(deck, dealer, dealercards)
        sleep(2)
        # 7. Determine winner and pay/collect bets
        for idx in range(len(playersnames)):
            determinewinner(playersnames, dealercards, maincards,
                                     monies, wagers, idx)
        # 8. finalizeround()
        finalizeround(deck, discardpile, maincards, splitcards, dealercards)
        # 9. Ask for new round
        if not playagain():
            break

if __name__ == "__main__":
    main()
