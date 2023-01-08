WHITE_JOKER = 53
BLACK_JOKER = 54

def position_white_joker(card_deck):
    return card_deck.index(WHITE_JOKER)

def position_black_joker(card_deck):
    return card_deck.index(BLACK_JOKER)

def first_swap(card_deck):
    card_deck[position_white_joker(card_deck)], card_deck[(position_white_joker(card_deck) + 1) % BLACK_JOKER] = card_deck[(position_white_joker(card_deck) + 1) % BLACK_JOKER], card_deck[position_white_joker(card_deck)]
    return card_deck

def second_swap(card_deck):
    card_deck[position_black_joker(card_deck)], card_deck[(position_black_joker(card_deck) + 1) % BLACK_JOKER] = card_deck[(position_black_joker(card_deck) + 1) % BLACK_JOKER], card_deck[position_black_joker(card_deck)]
    card_deck[position_black_joker(card_deck)], card_deck[(position_black_joker(card_deck) + 1) % BLACK_JOKER] = card_deck[(position_black_joker(card_deck) + 1) % BLACK_JOKER], card_deck[position_black_joker(card_deck)]
    return card_deck

def third_swap(card_deck):
    poz_1 = min(position_white_joker(card_deck), position_black_joker(card_deck))
    poz_2 = max(position_white_joker(card_deck), position_black_joker(card_deck))
    return card_deck[poz_2 + 1:] + card_deck[poz_1:poz_2 + 1] + card_deck[0:poz_1]

def split_card_deck(card_deck):
    if card_deck[WHITE_JOKER] == WHITE_JOKER or card_deck[WHITE_JOKER] == BLACK_JOKER:
        return card_deck
    top_card = card_deck[0]
    return card_deck[top_card: WHITE_JOKER] + card_deck[0:top_card] + [card_deck[WHITE_JOKER]]

def solitaire(card_deck):
    while True:
        card_deck = first_swap(card_deck)
        card_deck = second_swap(card_deck)
        card_deck = third_swap(card_deck)
        card_deck = split_card_deck(card_deck)
        if card_deck[0] != WHITE_JOKER and card_deck[0] != BLACK_JOKER:
            break
    
    print("kulcs visszaretitve")
    if card_deck[card_deck[0]] == BLACK_JOKER:
        return WHITE_JOKER
    else:
        return card_deck[card_deck[0]]