from classes.hand import Hand
from functions.hand_detectors.detect_poker_hands import detect_poker_hands
from global_variables.global_var import poker_hands_names
from functions.sorting_alg.choose_sorting_algorithm import choose_sorting_algorithm
import copy
from global_variables.global_var import aces
from global_variables.global_var import total_poker_hands

class Player:
    def __init__(self, cards, player_num):
        self.cards = cards
        self.combinations = copy.deepcopy(total_poker_hands)
        self.hand = []
        self.aces = {}
        self.total_value = 0
        self.player_num = player_num
        self.hand_size = 2
        self.hand_strenght = ""
        self.player_state = ""

    def get_player_num(self):
        return self.player_num

    def get_cards(self):
        return self.cards    

    def get_hand(self):
        return self.hand

    def get_total_value(self):
        return self.total_value

    def get_combinations(self):
        return self.combinations

    def get_number_of_cards(self):
        return len(self.get_cards())

    def get_hand_size(self):
        return self.hand_size
    
    def get_player_state(self):
        return self.player_state

    def get_hand_strenght(self):
        return self.hand_strenght
    
    def set_hand_strenght(self, strength):
        self.hand_strenght = strength

    def set_total_value(self, value):
        self.total_value = value

    def add_card_hand_size(self):
        self.hand_size += 1

    def set_player_state(self, state):
        self.player_state = state

    def reset_combinations(self):
        self.combinations = copy.deepcopy(total_poker_hands)

    def show_combinations(self):
        combinations = {}
        for key in self.get_combinations().keys():
            if self.get_combinations()[key] != 0:
                combinations[key] = self.get_combinations()[key]
        print(combinations)

    def show_hand(self):
        self.get_hand().show_hand()

    def add_cards(self, cards):
        for card in cards:
            self.get_cards().append(card)
            if card.get_value() != 14:
                self.add_card_hand_size()

        hand = choose_sorting_algorithm(Hand(self.get_cards()))
        self.hand = copy.deepcopy(hand)
        for card in self.get_hand().get_cards(0, self.get_hand().get_quantity()):
            if card.is_ace():
                suit, value = card.get_suit(), card.get_value()
                for card1 in self.get_hand().get_cards(0, self.get_hand().get_quantity()):
                    if card1.is_ace() and card1.get_suit() == suit and card1.get_value() != value:
                        aces[card] = card1
                        aces[card1] = card

    def calculate_total_value(self, poker_hands):
        total_value = 0
        counter = 900
        for poker_hand in poker_hands:
            if len(poker_hand) > 0:
                for combination in poker_hand:
                    for card in combination:
                        total_value += card.get_value()
                total_value += counter
            counter -= 100
        self.total_value = total_value

    def update_poker_hands(self):
        combinations = self.get_combinations()
        poker_hands = detect_poker_hands(self.get_hand())
        self.calculate_total_value(poker_hands)
        if self.get_hand_size() == 7:
            for index, poker_hand in enumerate(poker_hands):
                combinations[poker_hands_names[index]] += len(poker_hand)