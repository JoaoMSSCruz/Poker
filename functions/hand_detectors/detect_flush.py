from functions.hand_detectors.only_one_ace_per_hand import only_one_ace_per_hand

def detect_flush(suit_division):
    flushes = []

    for suit in suit_division:
        possible_flush = []
        if len(suit) < 5:
            continue
        for card in suit:
            if not card.get_used():
                possible_flush.append(card)
                if len(possible_flush) == 5:
                    if only_one_ace_per_hand(possible_flush):
                        for card_participant in possible_flush:
                            card_participant.set_used()
                        flushes.append(possible_flush)
                    possible_flush = []
    
    return flushes