def binary_search(hand, val, start, end):
    while start < end:
        mid = (start + end) // 2
        if hand.get_card_value(mid) < val:
            start = mid + 1
        else:
            end = mid
    return start