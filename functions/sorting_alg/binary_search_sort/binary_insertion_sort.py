from functions.sorting_alg.binary_search_sort.binary_search import binary_search
from classes.hand import Hand

def binary_insertion_sort(hand):
    for index in range(1, hand.get_quantity()):
        val = hand.get_card_value(index)
        pos = binary_search(hand, val, 0, index)
        hand = Hand(hand.get_cards(0, pos) + [hand.get_card(index)] + hand.get_cards(pos, index) + hand.get_cards(index+1, hand.get_quantity()))

    return hand