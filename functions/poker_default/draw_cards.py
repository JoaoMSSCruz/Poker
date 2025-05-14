def draw_cards(deck):
    while True:
        number_of_cards_to_be_drawn = int(input("How many cards would you like to draw? "))
        if 3 <= number_of_cards_to_be_drawn <= 15:
            return deck.draw_cards(number_of_cards_to_be_drawn)
        else:
            print("Please choose a number between 3 and 15.")