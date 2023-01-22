import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def test_if_card_is_ace(self):
        ace = Card("Ace",1)
        self.assertEquals(True,CardGame.check_for_ace(self,ace))

    def test_if_card_is_not_ace(self):
        two = Card("Two",2)
        self.assertEquals(False,CardGame.check_for_ace(self,two))
    
    def test_to_see_which_card_is_higher(self):
        two = Card("Two",2)
        ace = Card("Ace",1)
        self.assertEquals(two,CardGame.highest_card(self,two,ace))

    def test_to_see_what_happens_if_cards_are_equal(self):
        ace2 = Card("Ace",1)
        ace1 = Card("Ace",1)
        self.assertEquals("they are the same",CardGame.highest_card(self,ace1,ace2))
    
    def test_to_see_if_total_is_correct(self):
        ace2 = Card("Ace",1)
        ace1 = Card("Ace",1)
        seven = Card("Seven",7)
        cards = [ace1,ace2,seven]
        self.assertEquals("You have a total of 9", CardGame.cards_total(self,cards))


