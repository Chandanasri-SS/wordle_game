class AIStrategy:
    def choose_forced_bid(self, player, diamond, highest_bid):
        """
        Improved AI:
        - Preserves high cards for high diamonds
        - Tries to win cheaply
        - Sacrifices low cards when losing is likely
        """

        # Sort hand by value
        hand = sorted(player.hand, key=lambda c: c.value)

        diamond_value = diamond.value

        # ---------- 1. Try cheap winning ----------
        # Find the smallest card that beats highest_bid
        winning_card = next((c for c in hand if c.value > highest_bid), None)

        if winning_card:
            # Decide if this diamond is worth winning
            # Avoid wasting very high cards on low diamonds
            if diamond_value >= winning_card.value - 2:
                return winning_card, winning_card.value

            # If diamond is low value, don't waste mid/high card
            if diamond_value <= 6 and winning_card.value >= 10:
                return hand[0], hand[0].value  # sacrifice lowest

            return winning_card, winning_card.value

        # ---------- 2. Cannot win → strategic sacrifice ----------
        # If cannot beat highest bid, dump the lowest card
        return hand[0], hand[0].value