"""
cards.py
"""

# Suits and faces of a deck of cards
suitchars: list = "♠ ♣ ♥ ♦".split()
suitnames: list = "Clubs Spades Hearts Diamonds".split()
faceschars: list = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

# Card values
cardsvalues: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Card outlines
horizline13: str = "─"*13
horizline11: str = "─"*11
vertline: str = "│"
topright: str = "┌"
topleft: str = "┐"
bottomleft: str = "└"
bottomright: str = "┘"
sideborders = f"{vertline:14}{vertline}"
blankborders = f"{vertline}{vertline}ӀѺѺѺѺѺѺѺѺѺӀ{vertline}{vertline}"
cardtop: str = f"{topright}{horizline13}{topleft}"
cardtop2: str = f"{vertline}{topright}{horizline11}{topleft}{vertline}"
cardbottom: str = f"{bottomleft}{horizline13}{bottomright}"
cardbottom2: str = f"{vertline}{bottomleft}{horizline11}{bottomright}{vertline}"
"""
Print all 52 cards in the standard poker deck
according to their suits
"""
def printcards(suits: list, faces: list, start: int = 0, col: int = 5) -> None:
    for i in range(0, len(suitchars)):
        # print(f"Printing the {suitschars[i]} deck")
        for p in range(start, len(faceschars), col):
            topface = ""
            topsuit = ""
            lowface = ""
            lowsuit = ""
            centersuit = ""
            # Check the number of printable cards at max{col}
            n = len(faceschars[p:p+col])
            print(cardtop*n)
            for x in faceschars[p:p+col]:
                topface += f"{vertline}{x:<2}{vertline:>12}"
                topsuit += f"{vertline}{suitchars[i]:<2}{vertline:>12}"
                centersuit += f"{vertline}{suitchars[i].center(13)}{vertline}"
                lowsuit += f"{vertline:12}{suitchars[i]:>2}{vertline}"
                lowface += f"{vertline:12}{x:>2}{vertline}"
            print(topface)
            print(topsuit)
            for g in range(0, 2):
                print(sideborders*n)
            print(centersuit)
            for g in range(0, 2):
                print(sideborders*n)
            print(lowsuit)
            print(lowface)
            print(cardbottom*n)

def printhands(cards: list, start: int = 0, col: int = 5) -> None:
    for p in range(start, len(cards), col):
        topface = ""
        topsuit = ""
        lowface = ""
        lowsuit = ""
        centersuit = ""
        # Check the number of printable cards at max{col}
        n = len(cards[p:p+col])
        print(cardtop*n)
        for x in cards[p:p+col]:
            # Find the matching suit character
            for idx, val in enumerate(suitnames):
                if x[1] == val:
                    topface += f"{vertline}{x[0]:<2}{vertline:>12}"
                    topsuit += f"{vertline}{suitchars[idx]:<2}{vertline:>12}"
                    lowface += f"{vertline:12}{x[0]:>2}{vertline}"
                    lowsuit += f"{vertline:12}{suitchars[idx]:>2}{vertline}"
                    centersuit += f"{vertline}{suitchars[idx].center(13)}{vertline}"
        print(topface)
        print(topsuit)
        for g in range(0, 2):
            print(sideborders*n)
        print(centersuit)
        for g in range(0, 2):
            print(sideborders*n)
        print(lowsuit)
        print(lowface)
        print(cardbottom*n)

def printsinglecard(card: tuple) -> None:
    if not isinstance(card, tuple):
        return
    topface = ""
    topsuit = ""
    lowface = ""
    lowsuit = ""
    centersuit = ""
    for idx, val in enumerate(suitnames):
        if card[1] == val:
            topface += f"{vertline}{card[0]:<2}{vertline:>12}"
            topsuit += f"{vertline}{suitchars[idx]:<2}{vertline:>12}"
            lowface += f"{vertline:12}{card[0]:>2}{vertline}"
            lowsuit += f"{vertline:12}{suitchars[idx]:>2}{vertline}"
            centersuit += f"{vertline}{suitchars[idx].center(13)}{vertline}"
    print(cardtop)
    print(topface)
    print(topsuit)
    for g in range(0, 2):
        print(sideborders)
    print(centersuit)
    for g in range(0, 2):
        print(sideborders)
    print(lowsuit)
    print(lowface)
    print(cardbottom)

def printholecard() -> None:
    print(cardtop)
    print(cardtop2)
    for g in range(0, 6):
        print(blankborders)
    print(cardbottom2)
    print(cardbottom)

