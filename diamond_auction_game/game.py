import random
from models import Player
from factory import SuitSetFactory
from ai import AIStrategy
from round import AuctionRound


import random
from models import Player
from factory import SuitSetFactory
from ai import AIStrategy
from round import AuctionRound


class DiamondAuctionGame:
    def __init__(self, num_players=2):
        self.players = []
        self.ai = AIStrategy()

        # Fixed suit order (Diamonds always auction)
        suits = ['♠', '♥', '♣']
        random.shuffle(suits)

        # Create suit-based sets
        suit_sets = {
            suit: SuitSetFactory.create_suit_set(suit)
            for suit in ['♠', '♥', '♣', '♦']
        }

        if num_players == 2:
            self.players = [
                Player(0, "You", suit_sets[suits[0]], is_ai=False),
                Player(1, "Computer", suit_sets[suits[1]], is_ai=True),
            ]
            self.diamond_deck = suit_sets['♦']   # auction
            # one suit in suits[] is unused

        else:
            self.players = [
                Player(0, "You", suit_sets[suits[0]], is_ai=False),
                Player(1, "Computer 1", suit_sets[suits[1]], is_ai=True),
                Player(2, "Computer 2", suit_sets[suits[2]], is_ai=True),
            ]
            self.diamond_deck = suit_sets['♦']

        random.shuffle(self.diamond_deck)

    def play(self):
        print("\n🎴 Diamond Auction Game Started!")
        print(f"Players: {', '.join(p.name for p in self.players)}")
        print("-" * 40)

        round_no = 1

        for diamond in self.diamond_deck:
            print(f"\n========== ROUND {round_no} ==========")

            auction_round = AuctionRound(self.players, diamond)
            result = auction_round.play(self.ai)

            # Show scores after each round
            print("\n📊 SCORES AFTER THIS ROUND:")
            for p in self.players:
                print(
                    f"  {p.name}: {p.score} pts | "
                    f"Diamonds: {len(p.diamonds)} | "
                    f"Cards left: {len(p.hand)}"
                )

            round_no += 1

        self.end_game()

    def end_game(self):
        print("\n=== FINAL SCORES ===")
        ranked = sorted(
            self.players,
            key=lambda p: (-p.score, -len(p.diamonds), len(p.hand))
        )

        for p in ranked:
            print(
                f"{p.name}: "
                f"{p.score} points | "
                f"Diamonds won: {len(p.diamonds)} | "
                f"Cards remaining: {len(p.hand)}"
            )

        print("\n🎉 Game Over!")