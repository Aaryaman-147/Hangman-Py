import random

HANGMAN_PICS = [
    """
      +---+
          |
          |
          |
         ===
    """,
    """
      +---+
      O   |
          |
          |
         ===
    """,
    """
      +---+
      O   |
      |   |
          |
         ===
    """,
    """
      +---+
      O   |
     /|   |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\  |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\  |
     /    |
         ===
    """,
    """
      +---+
      O   |
     /|\  |
     / \  |
         ===
    """
]

def choose_word(difficulty):
    words = {
        'easy': ['loop', 'array', 'script', 'debug', 'code'],
        'medium': ['python', 'college', 'hangman', 'library', 'science'],
        'hard': ['complication', 'astrophysics', 'interdisciplinary', 'debugging', 'algorithm']
    }
    return random.choice(words[difficulty])

def display(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def get_hint(word, guessed_letters):
    """Reveals one random unrevealed letter from the word."""
    remaining_letters = [letter for letter in word if letter not in guessed_letters]
    return random.choice(remaining_letters) if remaining_letters else None

def hangman():
    print("Welcome to Hangman!")
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    
    while difficulty not in ['easy', 'medium', 'hard']:
        difficulty = input("Invalid choice. Choose difficulty (easy, medium, hard): ").lower()

    word = choose_word(difficulty)
    guessed_letters = set()
    max_attempts = len(HANGMAN_PICS) - 1
    attempts = 0
    hint_used = False

    while attempts < max_attempts:
        print(HANGMAN_PICS[attempts])
        print(f"\nWord: {display(word, guessed_letters)}")
        print(f"Attempts left: {max_attempts - attempts}")

        guess = input("Guess a letter or type 'hint' to reveal a letter: ").lower()

        if guess == "hint":
            if hint_used:
                print("You have already used your hint!")
            else:
                hint_letter = get_hint(word, guessed_letters)
                if hint_letter:
                    guessed_letters.add(hint_letter)
                    print(f"Hint used! Revealed letter: {hint_letter}")
                    hint_used = True
                else:
                    print("No more letters to reveal!")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            attempts += 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(HANGMAN_PICS[-1])
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()