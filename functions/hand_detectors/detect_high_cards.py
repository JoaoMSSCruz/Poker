def detect_high_cards(rank_division, quantity):
    high_cards = []
    for rank in reversed(rank_division):
        for card in rank:
            if not card.get_used():
                high_cards.append([card])
                if len(high_cards) == quantity:
                    return high_cards
    return high_cards