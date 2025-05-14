def partition(hand, low, high):
    pivot = hand.get_card_value(high)
    i = low - 1
    for j in range(low, high):
        if hand.get_card_value(j) <= pivot:
            i += 1
            hand.switch_cards(i, j)
    hand.switch_cards(i + 1, high)
    return i + 1