class AuctionRound:
    def __init__(self, players, diamond):
        self.players = players
        self.diamond = diamond
        self.bids = {}   # player_id -> (card, value)

    def play(self, ai_strategy):
        print(f"\n💎 Diamond on auction: {self.diamond.rank}{self.diamond.suit} ({self.diamond.value})")

        # Each player MUST bid exactly one card
        for player in self.players:
            if player.is_ai:
                self.ai_turn(player, ai_strategy)
            else:
                self.human_turn(player)

        bid_values = [bid[1] for bid in self.bids.values()]

        # Show all bids
        print("\n📢 BIDS THIS ROUND:")
        for pid, (card, value) in self.bids.items():
            print(f"  {self.players[pid].name} bid {card} ({value})")

        # Case 1: All bids equal → Diamond discarded
        if len(set(bid_values)) == 1:
            print("⚠️ All bids equal! Diamond discarded.")
            self.discard_all_bid_cards()
            return "DISCARD"

        # Case 2: Winner exists
        return self.resolve_winner()

    def human_turn(self, player):
        print(f"\n{player.name} hand:")
        print(" ".join(str(c) for c in player.hand))

        while True:
            choice = input("Choose a card rank to bid (2–10, J, Q, K, A): ").strip().upper()
            card = next((c for c in player.hand if c.rank == choice), None)
            if card:
                self.bids[player.id] = (card, card.value)
                return
            print("❌ Invalid choice. Choose a rank you still have.")

    def ai_turn(self, player, ai_strategy):
        highest = max((bid[1] for bid in self.bids.values()), default=0)
        card, value = ai_strategy.choose_forced_bid(player, self.diamond, highest)
        self.bids[player.id] = (card, value)

    def discard_all_bid_cards(self):
        for pid, (card, _) in self.bids.items():
            self.players[pid].remove_cards([card])

    def resolve_winner(self):
        winner_id = max(self.bids, key=lambda pid: self.bids[pid][1])

        # Everyone loses their bid card
        self.discard_all_bid_cards()

        winner = self.players[winner_id]
        winner.score += self.diamond.value
        winner.diamonds.append(self.diamond)

        print(f"🏆 {winner.name} wins {self.diamond.rank}{self.diamond.suit}")
        return winner