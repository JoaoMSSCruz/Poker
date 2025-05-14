from global_variables.global_var import ranks, suits
from classes.card import Card

def create_total_cards():
    total_cards = []
    for value, rank in enumerate(ranks):
        for suit in suits:
            card = Card(rank, suit, value+1)
            total_cards.append(card)
    return total_cards