from classes.hand import Hand

def merge(left_half, right_half):

    result = []
    i = j = 0
    
    # Junta de forma ordenada
    while i < left_half.get_quantity() and j < right_half.get_quantity():
        if left_half.get_card_value(i) <= right_half.get_card_value(j):
            result.append(left_half.get_card(i))
            i += 1
        else:
            result.append(right_half.get_card(j))
            j += 1

    # Adiciona os restantes elementos
    result.extend(left_half.get_cards(i, left_half.get_quantity()))
    result.extend(right_half.get_cards(j, right_half.get_quantity()))

    return Hand(result)