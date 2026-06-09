import random

# ─── Hangman ASCII art stages ───────────────────────────────────────────────
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]

WORDS = ["python", "hangman", "programming", "developer", "internship"]


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("\n" + "=" * 40)
    print("       Welcome to HANGMAN!")
    print("=" * 40)

    while incorrect_guesses < max_incorrect:
        print(HANGMAN_STAGES[incorrect_guesses])
        print(f"\n  Word: {display_word(word, guessed_letters)}")
        print(f"  Wrong guesses left: {max_incorrect - incorrect_guesses}")
        print(f"  Guessed letters   : {', '.join(sorted(guessed_letters)) or 'None'}")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\n  🎉 You won! The word was: '{word}'")
            break

        guess = input("\n  Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠  Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("  ⚠  You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"  ✅ '{guess}' is in the word!")
        else:
            incorrect_guesses += 1
            print(f"  ❌ '{guess}' is NOT in the word.")
    else:
        print(HANGMAN_STAGES[max_incorrect])
        print(f"\n  💀 Game over! The word was: '{word}'")

    print("\n" + "=" * 40)
    play_again = input("  Play again? (yes/no): ").lower().strip()
    if play_again in ("yes", "y"):
        hangman()
    else:
        print("  Thanks for playing! Goodbye 👋")


if __name__ == "__main__":
    hangman()
