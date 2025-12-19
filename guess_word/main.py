import os
import random

# --------------------------------------------------
# Dictionary loading (robust)
# --------------------------------------------------

def load_dictionary(filename="words_alpha.txt"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, filename)
    with open(path, "r", encoding="utf-8") as f:
        return set(word.strip().lower() for word in f)

DICTIONARY = load_dictionary()


def get_candidates(word_length):
    return [w for w in DICTIONARY if len(w) == word_length]


# --------------------------------------------------
# Core logic
# --------------------------------------------------

def count_common_letters(word1, word2):
    chars = list(word1)
    count = 0
    for ch in word2:
        if ch in chars:
            count += 1
            chars.remove(ch)
    return count


# --------------------------------------------------
# MODE 1: Computer is master (Human guesses)
# --------------------------------------------------

def play_human_guesses():
    print("\n🎯 YOU GUESS THE WORD")

    while True:
        try:
            word_length = int(input("Choose word length (3–8): "))
            if 3 <= word_length <= 8:
                break
        except ValueError:
            pass
        print("❌ Enter a valid number between 3 and 8.")

    candidates = get_candidates(word_length)
    secret = random.choice(candidates)
    guesses = []

    print(f"\n🤖 Computer has chosen a {word_length}-letter word.")
    print("Type PASS anytime to give up.")

    while True:
        guess = input(f"\nEnter a {word_length}-letter word: ").lower()

        if guess == "pass":
            print("\n❌ You gave up.")
            print(f"Secret word was: {secret}")
            print(f"Total guesses: {len(guesses)}")
            return

        if len(guess) != word_length or not guess.isalpha():
            print("❌ Invalid input.")
            continue

        if guess not in DICTIONARY:
            print("❌ Not a meaningful word.")
            continue

        guesses.append(guess)

        if guess == secret:
            print("\n🎉 Correct! You guessed the word!")
            print(f"Total guesses: {len(guesses)}")
            return

        print(
            f"🔍 Correct letters (any position): "
            f"{count_common_letters(secret, guess)}"
        )


# --------------------------------------------------
# MODE 2: User is master (Computer guesses)
# --------------------------------------------------

def play_computer_guesses():
    print("\n🤖 COMPUTER GUESSES YOUR WORD")
    print("Think of a secret word in your head.")
    print("Do NOT type it anywhere.\n")

    while True:
        try:
            word_length = int(input("Choose word length (3–8): "))
            if 3 <= word_length <= 8:
                break
        except ValueError:
            pass
        print("❌ Enter a valid number between 3 and 8.")

    candidates = get_candidates(word_length)
    attempt = 0
    letters_known = False

    print("\n🤖 Computer starts guessing.\n")

    while True:
        if not candidates:
            print("⚠️ No possible words left.")
            print("Your feedback may have been inconsistent.")
            return

        guess = random.choice(candidates)
        attempt += 1

        print(f"Guess #{attempt}: {guess}")

        # -----------------------------
        # PHASE 1: Letter discovery
        # -----------------------------
        if not letters_known:
            while True:
                try:
                    feedback = int(
                        input("How many letters match (any position)? ")
                    )
                    if 0 <= feedback <= word_length:
                        break
                except ValueError:
                    pass
                print("❌ Enter a valid number.")

            if feedback == word_length:
                confirm = input(
                    "All letters match. Is this the exact word? (yes/no): "
                ).strip().lower()

                if confirm == "yes":
                    print("\n🎉 Computer guessed your word!")
                    print(f"Attempts taken: {attempt}")
                    return

                # Letters known → switch phase
                letters_known = True

                # Keep only anagrams
                candidates = [
                    w for w in candidates
                    if sorted(w) == sorted(guess)
                ]
            else:
                candidates = [
                    w for w in candidates
                    if count_common_letters(w, guess) == feedback
                ]

        # -----------------------------
        # PHASE 2: Arrangement search
        # -----------------------------
        else:
            confirm = input(
                "Is this the exact word? (yes/no): "
            ).strip().lower()

            if confirm == "yes":
                print("\n🎉 Computer guessed your word!")
                print(f"Attempts taken: {attempt}")
                return

            # Remove wrong permutation
            candidates = [w for w in candidates if w != guess]

def main():
    print("🎮 WORD GUESSING GAME")
    print("-" * 30)
    print("Who is the master (keeps the secret word)?")
    print("1. Computer")
    print("2. You")

    while True:
        choice = input("Enter choice (1 or 2): ").strip()
        if choice == "1":
            play_human_guesses()
            return
        if choice == "2":
            play_computer_guesses()
            return
        print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
