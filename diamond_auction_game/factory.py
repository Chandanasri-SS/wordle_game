from models import Card

RANKS = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
RANK_VALUES = {
    'A':14,'K':13,'Q':12,'J':11,'10':10,
    '9':9,'8':8,'7':7,'6':6,'5':5,
    '4':4,'3':3,'2':2
}

class SuitSetFactory:
    @staticmethod
    def create_suit_set(suit):
        return [
            Card(rank, suit, RANK_VALUES[rank])
            for rank in RANKS
        ]