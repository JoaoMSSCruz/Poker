from functions.hand_detectors.only_one_ace_per_hand import only_one_ace_per_hand

def detect_full_house(rank_division):
    full_houses = []
    three_of_a_kinds = []
    pairs = []
    for rank in reversed(rank_division):
        possible_member = []
        if len(rank) < 2:
            continue
        for card in rank:
            if not card.get_used():
                possible_member.append(card)
        if len(possible_member) == 3:
            three_of_a_kinds.append(possible_member)
            pairs.append([possible_member[0], possible_member[1]])
        elif len(possible_member) == 2:
            pairs.append(possible_member)
    for three_of_a_kind in three_of_a_kinds:
        rank = three_of_a_kind[0].get_rank()
        for pair in pairs:
            if only_one_ace_per_hand(three_of_a_kind+pair):
                if pair[0].get_rank() != rank:
                    for card in three_of_a_kind:
                        card.set_used()
                    for card in pair:
                        card.set_used()
                    full_houses.append(three_of_a_kind+pair)
                    three_of_a_kinds.remove(three_of_a_kind)
                    pairs.remove(pair)
                    pairs.remove([three_of_a_kind[0], three_of_a_kind[1]])
                    break

    return full_houses