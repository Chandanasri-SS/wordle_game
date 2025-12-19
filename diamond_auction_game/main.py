from game import DiamondAuctionGame

def main():
    print("🔷 Diamond Auction Game")
    players = input("Enter number of players (2 or 3): ").strip()

    if players not in ('2', '3'):
        players = '2'

    game = DiamondAuctionGame(num_players=int(players))
    game.play()

if __name__ == "__main__":
    main()