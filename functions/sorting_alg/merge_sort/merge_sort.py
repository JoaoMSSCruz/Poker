from classes.hand import Hand
from functions.sorting_alg.merge_sort.merge import merge

def merge_sort(hand):

    if hand.get_quantity() <= 1:
        return hand

    # Divide
    mid = hand.get_quantity() // 2
    left_half = merge_sort(Hand(hand.get_cards(0, mid)))
    right_half = merge_sort(Hand(hand.get_cards(mid, hand.get_quantity())))

    # Conquista (fusão)
    return merge(left_half, right_half)