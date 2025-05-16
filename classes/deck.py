import random
from classes.card import Card

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def get_cards(self):
        return self.cards

    def get_size(self):
        return len(self.get_cards())

    def shuffle_cards(self):
        random.shuffle(self.get_cards())

    def remove_cards(self, cards):
        for card in cards:
            if card.get_value() != 14:
                self.get_cards().remove(card)

    def draw_cards(self, number_of_cards):
        cards_drawn = []
        for card_number in range(number_of_cards):
            card = self.get_cards()[card_number]
            if card.is_ace():
                card1 = Card(card.get_rank(), card.get_suit(), 14)
                cards_drawn.append(card1)
            cards_drawn.append(card)
        return cards_drawn