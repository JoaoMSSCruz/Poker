def detect_three_of_a_kind(rank_division):
    three_of_a_kinds = []

    for rank in rank_division:
        possible_three_of_a_kind = []
        if len(rank) < 3:
            continue
        for card in rank:
            if possible_three_of_a_kind == [] or card.get_rank() != possible_three_of_a_kind[-1].get_rank():
                possible_three_of_a_kind = [card]
            elif card.get_used():
                possible_three_of_a_kind = []
            else:
                if len(possible_three_of_a_kind) == 2:
                    possible_three_of_a_kind.append(card)
                    for card_participant in possible_three_of_a_kind:
                        card_participant.set_used()
                        rank.remove(card_participant)
                    three_of_a_kinds.append(possible_three_of_a_kind)
                    possible_three_of_a_kind = []
                else:
                    possible_three_of_a_kind.append(card)

    return three_of_a_kinds