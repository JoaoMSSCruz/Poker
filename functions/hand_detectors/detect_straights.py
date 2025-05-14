def detect_straights(rank_division):
    straights = []
    capable_cards = []

    for rank in reversed(rank_division):
        not_used_cards = []
        for card in rank:
            if card.get_value():
                not_used_cards.append(card)
                
        capable_cards.append(not_used_cards)
        
    if len(capable_cards) > 4:
        number = 0
        while number <= len(capable_cards) - 5:
            group = capable_cards[number]
            for card in group:
                try:
                    # Garante que todos os grupos têm pelo menos uma carta
                    if not all(len(capable_cards[number + i]) > 0 for i in range(5)):
                        continue
                    if not all(len(capable_cards[number + i]) > 0 and not capable_cards[number + i][0].get_used() for i in range(5)):
                        continue
                    card1 = capable_cards[number+1][0]
                    card2 = capable_cards[number+2][0]
                    card3 = capable_cards[number+3][0]
                    card4 = capable_cards[number+4][0]

                    value = card.get_value()
                    if value == card1.get_value() + 1 == card2.get_value() + 2 == card3.get_value() + 3 == card4.get_value() + 4:
                        straights.append([card, card1, card2, card3, card4])
                        card.set_used()
                        card1.set_used()
                        card2.set_used()
                        card3.set_used()
                        card4.set_used()

                        capable_cards[number+1].remove(card1)
                        capable_cards[number+2].remove(card2)
                        capable_cards[number+3].remove(card3)
                        capable_cards[number+4].remove(card4)
                        capable_cards[number].remove(card)

                        # Limpa listas vazias
                        capable_cards = [group for group in capable_cards if group]
                        
                        # Recomeça do início
                        number = -1
                        break
                except IndexError:
                    pass
            number += 1
    
    return straights