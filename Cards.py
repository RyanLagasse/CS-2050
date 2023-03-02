import random

class Card:
    'Creates cards with attributes number and suite'

    def __init__(self, value, suit):
        'Initializes the card with base parameters'
        self.value = value
        self.suit = suit

    def __repr__(self):
        "Returns a string representation of the card in the format 'Card(value of suit)'."
        return f'Card({self.value} of {self.suit})'

    def __lt__(self, other):
        'Compares two cards based on value if they have the same suit, otherwise compares the suits.'
        if self.suit == other.suit:
            return self.value < other.value
        else:
            return self.suit < other.suit

class Deck:
    def __init__(self, values=list(range(1, 14)), suits=['clubs', 'diamonds', 'hearts', 'spades']):
        'Initializes the deck with base parameters'
        self.card_list = [Card(value, suit) for value in values for suit in suits]

    def __len__(self):
        'Returns the number of cards in the deck.'
        return len(self.card_list)

    def sort(self):
        'sorts the cards using the sort method'
        self.card_list.sort()

    def __repr__(self):
        ' Returns a string representation of the deck in the format '
        return f'Deck: {self.card_list}'

    def shuffle(self):
        'Shuffles the cards in the deck using the random modules shuffle function.'
        random.shuffle(self.card_list)

    def draw_top(self):
        'Draws the top card from the deck. Raises a RuntimeError if the deck is empty.'
        if len(self.card_list) == 0:
            raise RuntimeError("Can't draw from an empty deck")
        else:
            return self.card_list.pop()

class Hand(Deck):
    def __init__(self, cards):
        'Initializes the hand with base parameters'
        self.cards = cards

    def __repr__(self):
        "Draws the top card from the deck. Raises a 'RuntimeError' if the deck is empty."
        return f'Hand: {self.cards}'

    def play(self, card):
        'lays a card from the hand. Raises a RuntimeError if the card is not in the hand.'
        try:
            return self.card_list.pop(self.card_list.index(card))
        except ValueError:
            raise RuntimeError(f'Attempt to play {repr(card)} that is not in {self.__repr__()}')

    def __len__(self):
        'Returns the number of cards in the hand.'
        return len(self.cards)

'print statements for testing'
'''
d1 = Deck([2, 1], ['triangles', 'dots'])
print(d1.__repr__())

'''
