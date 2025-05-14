def only_one_ace_per_hand(poker_hand):
    card_record = []
    for card in poker_hand:
        card_rep = (card.get_rank(), card.get_suit())
        if card_rep in card_record:
            return False
        card_record.append(card_rep)
    return True