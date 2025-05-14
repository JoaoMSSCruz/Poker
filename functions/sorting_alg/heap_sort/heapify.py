def heapify(hand, hand_size, i):
    largest = i          # Assume que o maior é a raiz
    left = 2 * i + 1      # Índice do filho à esquerda
    right = 2 * i + 2     # Índice do filho à direita

    # Se o filho da esquerda for maior que a raiz
    if left < hand_size and hand.get_card_value(left) > hand.get_card_value(largest):
        largest = left

    # Se o filho da direita for maior que o maior até agora
    if right < hand_size and hand.get_card_value(right) > hand.get_card_value(largest):
        largest = right

    # Se o maior não for a raiz
    if largest != i:
        hand.switch_cards(i, largest)
        heapify(hand, hand_size, largest)  # Aplica heapify recursivamente