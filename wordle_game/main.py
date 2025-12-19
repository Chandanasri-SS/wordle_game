import requests
import random

BASE_URL = "https://wordle.we4shakthi.in/game"


# --------------------------------------------------
# API CLIENT (SESSION-BASED)
# --------------------------------------------------

class WordleClient:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        self.player_id = None

    def register(self, name):
        url = f"{BASE_URL}/register"
        payload = {
            "mode": "wordle",
            "name": name
        }

        r = self.session.post(url, json=payload, headers=self.headers)

        if r.status_code not in (200, 201):
            raise RuntimeError(f"Register failed: {r.status_code} {r.text}")

        data = r.json()
        self.player_id = data["id"]
        return data

    def create_game(self):
        url = f"{BASE_URL}/create"
        payload = {
            "id": self.player_id,
            "overwrite": True
        }

        r = self.session.post(url, json=payload, headers=self.headers)

        if r.status_code not in (200, 201):
            raise RuntimeError(f"Create failed: {r.status_code} {r.text}")

        return r.json()

    def guess(self, word):
        url = f"{BASE_URL}/guess"
        payload = {
            "id": self.player_id,
            "guess": word
        }

        r = self.session.post(url, json=payload, headers=self.headers)

        if r.status_code != 200:
            raise RuntimeError(f"Guess failed: {r.status_code} {r.text}")

        return r.json()


def print_feedback(guess, feedback):
    print(f"{guess.upper()}  {feedback}")


# --------------------------------------------------
# GAME LOOP
# --------------------------------------------------

def play_wordle():
    print("🎮 WORDLE — YOU vs COMPUTER")
    print("-" * 35)

    name = input("Enter your name: ").strip()

    client = WordleClient()
    client.register(name)
    print("✅ Registered")
    game = client.create_game()
    print(game["message"])
    print("\n👉 Start guessing (enter 5-letter words)\n")
    print()

    # Simple word pool for computer guesses
    WORD_POOL = [
        "crane", "slate", "trace", "adieu", "roast",
        "grain", "pride", "spear", "alone", "shine"
    ]

    used_words = set()
    turn = 0  # 0 = human, 1 = computer

    while True:
        # ---------------- HUMAN TURN ----------------
        if turn == 0:
            guess = input("👤 Your guess: ").strip().lower()

            if len(guess) != 5 or not guess.isalpha():
                print("❌ Invalid guess")
                continue

            used_words.add(guess)
            response = client.guess(guess)

            print_feedback(guess, response["feedback"])
            print(response["message"])

            if response["feedback"] == "GGGGG":
                print("\n🏆 YOU WIN!")
                break

        # ---------------- COMPUTER TURN ----------------
        else:
            choices = [w for w in WORD_POOL if w not in used_words]
            if not choices:
                print("🤖 Computer has no words left!")
                break

            guess = random.choice(choices)
            used_words.add(guess)

            print(f"\n🤖 Computer guesses: {guess}")
            response = client.guess(guess)

            print_feedback(guess, response["feedback"])
            print(response["message"])

            if response["feedback"] == "GGGGG":
                print("\n🤖 COMPUTER WINS!")
                break

        # Check guesses left
        if "0 guesses" in response["message"]:
            print("\n🤝 DRAW — No guesses left!")
            break

        # Switch turn
        turn = 1 - turn
        print()


# --------------------------------------------------
# ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":
    play_wordle()