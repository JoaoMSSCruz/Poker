from functions.hand_detectors.only_one_ace_per_hand import only_one_ace_per_hand

def detect_straight_flush(suit_division):
    straight_flushes = []

    for suit in suit_division:
        possible_straight_flush = []
        if len(suit) < 5:
            continue
        for card in suit:
            if possible_straight_flush == [] or card.get_value() != possible_straight_flush[-1].get_value() - 1:
                possible_straight_flush = [card]
            else:
                if len(possible_straight_flush) == 4:
                    possible_straight_flush.append(card)
                    if only_one_ace_per_hand(possible_straight_flush):
                        for card_participant in possible_straight_flush:
                            card_participant.set_used()
                        straight_flushes.append(possible_straight_flush)
                    possible_straight_flush = []
                else:
                    possible_straight_flush.append(card)

    return straight_flushes