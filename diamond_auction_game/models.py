class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.rank}{self.suit}"


class Player:
    def __init__(self, pid, name, hand, is_ai=False):
        self.id = pid
        self.name = name
        self.hand = hand[:]     # exactly 13 cards
        self.score = 0
        self.diamonds = []
        self.is_ai = is_ai
        self.passed = False

    def remove_cards(self, cards):
        for c in cards:
            self.hand.remove(c)

    def remaining_power(self):
        return sum(c.value for c in self.hand)