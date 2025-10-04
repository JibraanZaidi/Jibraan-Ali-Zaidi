New Chat
141 lines

import random
# List of possible words for the game (simple, common words)
words = ["name", "age", "salary", "ali", "ahmad", "movies", "show"]
# Select a random secret word
secret_word = random.choice(words)
# Set to track guessed letters (avoids duplicates)
guessed_letters = set()
# Counter for incorrect guesses
incorrect_guesses = 0
# Maximum allowed incorrect guesses before losing
MAX_INCORRECT = 6
def draw_hangman(num_wrong):
    """
    Draws the hangman figure based on the number of incorrect guesses.
    Uses multiline strings for cleaner ASCII art.
    """
    stages = [
        # Stage 0: Empty gallows
        """
  +---+
      |
      |
      |
      ===
        """,
        # Stage 1: Head
        """
