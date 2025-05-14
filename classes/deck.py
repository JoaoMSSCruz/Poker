import random
from classes.card import Card
from global_variables.global_var import aces

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def draw_cards(self, number_of_cards):
        cards_drawn = []
        for card_number in range(number_of_cards):
            card = self.cards[card_number]
            if card.is_ace():
                card1 = Card(card.get_rank(), card.get_suit(), 14)
                cards_drawn.append(card1)
                aces[card] = card1
                aces[card1] = card
            cards_drawn.append(card)
        return cards_drawn