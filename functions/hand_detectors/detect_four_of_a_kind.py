def detect_four_of_a_kind(rank_division):
    four_of_a_kinds = []

    for rank in rank_division:
        possible_four_of_a_kind = []
        if len(rank) < 4:
            continue
        for card in rank:
            if possible_four_of_a_kind == [] or card.get_rank() != possible_four_of_a_kind[-1].get_rank():
                possible_four_of_a_kind = [card]
            elif card.get_used():
                possible_four_of_a_kind = []
            else:
                if len(possible_four_of_a_kind) == 3:
                    possible_four_of_a_kind.append(card)
                    for card_participant in possible_four_of_a_kind:
                        card_participant.set_used()
                        rank.remove(card_participant)
                    four_of_a_kinds.append(possible_four_of_a_kind)
                    possible_four_of_a_kind = []
                else:
                    possible_four_of_a_kind.append(card)

    return four_of_a_kinds
