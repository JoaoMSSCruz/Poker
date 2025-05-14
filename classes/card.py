from global_variables.global_var import aces

class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value
        self.used = False

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit
    
    def get_value(self):
        return self.value

    def get_used(self):
        return self.used

    def set_used(self):
        self.used = True
        if self.is_ace():
            if not aces[self].get_used():
                aces[self].set_used()

    def show_card(self):
        print("Rank:{}, Suit:{}, Value:{};".format(self.rank, self.suit, self.value))

    def is_ace(self):
        if self.get_rank() == "Ace":
            return True
        return False