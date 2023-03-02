from Cards import Card, Deck, Hand
import unittest

class TestCard(unittest.TestCase):
    "Test cases specific to the Card class"
    def test_init(self):
        "Test that Card objects are created correctly"
        c = Card(3, 'hearts')
        self.assertEqual(c.value, 3)
        self.assertEqual(c.suit, 'hearts')
        
    def test_repr(self):
        "Test the string representation of a Card object"
        c = Card(3, 'hearts')
        self.assertEqual(str(c), 'Card(3 of hearts)')
        
    def test_lt(self):
        "Test the < operator for Card objects"
        c1 = Card(3, 'hearts')
        c2 = Card(3, 'spades')
        self.assertTrue(c1 < c2)
        c3 = Card(4, 'hearts')
        self.assertTrue(c3 < c2)

class TestDeck(unittest.TestCase):
    "Test cases specific to the Deck class"
    def test_init(self):
        "Test that Deck objects are created correctly"
        d1 = Deck()
        self.assertEqual(len(d1), 52)
        d2 = Deck([2, 1], ['triangles', 'dots'])
        self.assertEqual(len(d2), 4)
        
    def test_repr(self):
        "Test the string representation of a Deck object"
        d = Deck([2, 1], ['triangles', 'dots'])
        self.assertEqual(str(d), 'Deck: [Card(2 of triangles), Card(2 of dots), Card(1 of triangles), Card(1 of dots)]')

class TestHand(unittest.TestCase): 
    """Test cases specific to the Hand class"""
    def test_init(self):
        """Test the initialisation of Hand objects"""

        h1 = Hand([Card(value, 'clubs') for value in range(4, 0, -1)])
        self.assertEqual(str(h1), "Hand: [Card(4 of clubs), Card(3 of clubs), Card(2 of clubs), Card(1 of clubs)]")
    
    'Tests the implimentation of the play function in Hand class'
    def test_play(self):
        h1 = Hand([Card(value, 'clubs') for value in range(5, 0, -1)])

        card = h1.play(Card(3, 'clubs'))
        self.assertEqual(repr(card), "Card(3 of clubs)")
        self.assertEqual(len(h1), 4)
        self.assertEqual(h1.play(Card(1, 'clubs')), Card(1, 'clubs'))

        with self.assertRaises(RuntimeError):
            h1.play(Card(4, 'clubs'))

    def test_repr(self):
        """Test the string representation of a Hand object"""

        hand = Hand([Card(value, 'clubs') for value in range(5, 0, -1)])
        self.assertEqual(repr(hand), 'Hand: [Card(5 of clubs), Card(4 of clubs), Card(3 of clubs), Card(2 of clubs), Card(1 of clubs)]')


unittest.main()

