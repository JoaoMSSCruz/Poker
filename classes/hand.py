class Hand:
    def __init__(self, hand):
        self.hand = hand
        self.quantity = len(hand)

    def get_quantity(self):
        return self.quantity
    
    def get_hand(self):
        return self.hand

    def get_card_value(self, card_index):
        return self.get_card(card_index).get_value()

    def show_hand(self):
        for card in self.hand:
            card.show_card()

    def switch_cards(self, index_card1, index_card2):
        self.hand[index_card1], self.hand[index_card2] = self.hand[index_card2], self.hand[index_card1]  

    def get_cards(self, index_card1, index_card2):
        cards = []
        for i in range(index_card1, index_card2):
            cards.append(self.get_card(i))
        return cards
    
    def get_card(self, index):
        return self.get_hand()[index]
    