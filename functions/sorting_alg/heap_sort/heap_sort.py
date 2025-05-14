from functions.sorting_alg.heap_sort.heapify import heapify

def heap_sort(hand):
    hand_size = hand.get_quantity()
        
    # 1. Constrói o max-heap (reorganiza a lista)
    for index in range(hand_size // 2 - 1, -1, -1):
        heapify(hand, hand_size, index)

    # 2. Extrai elementos um a um
    for size in range(hand_size - 1, 0, -1):
        hand.switch_cards(0, size)
        heapify(hand, size, 0)  # Reorganiza o heap com os restantes

    return hand