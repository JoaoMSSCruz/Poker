from functions.hand_detectors.only_one_ace_per_hand import only_one_ace_per_hand

def detect_two_pairs_and_pairs(rank_division):
    two_pairs = []
    pairs = []

    for rank in reversed(rank_division):
        possible_pairs = []
        if len(rank) < 2:
            continue
        for card in rank:
            if card.get_used():
                possible_pairs = []
                continue
            elif possible_pairs == [] or card.get_rank() != possible_pairs[-1].get_rank():
                possible_pairs = [card] 
            else:
                if len(possible_pairs) == 1:
                    possible_pairs.append(card)
                    for card_participant in possible_pairs:
                        card_participant.set_used()
                        rank.remove(card_participant)
                    pairs.append(possible_pairs)
                    possible_pairs = []
                else:
                    possible_pairs.append(card)
    if len(pairs) > 1:
        for number in range(0, len(pairs) - 1, 2):
            if only_one_ace_per_hand(pairs[number]+pairs[number+1]):
                two_pairs.append(pairs[number]+pairs[number+1])
    for pair in two_pairs:
        pairs.remove([pair[0], pair[1]])
        pairs.remove([pair[2], pair[3]])

    return two_pairs, pairs