from english_words import english_words_set
import random

def generate_word():
    """
    Generates a random five letter word in the English language.
    This five letter word is the solution to the game. 
    """
    # Make a list of all possible five letter words in the English language
    five_letter_words = []
    for a_word in english_words_set:
        if len(a_word) == 5:
            five_letter_words.append(a_word)
    
    # Check if any word is a proper noun and remove it from the list of possible five letter words
    for word in five_letter_words:
        if word[0].isupper():
            five_letter_words.remove(word)
    
    # Pick a random five letter word to be the solution 
    solution = random.choice(five_letter_words)
    
    return solution

def word_guess():
    """
    Gets user's guess for what the solution could be.
    """
    return

def score_guess(guess, solution):
    """
    Takes the user's guess and scores it based on what the solution is. Below is a key for how
    you can interpret the score:
        X - character is not in the word
        Y - character is in the word but in the wrong spot
        Z - character is in the word and in the right spot
    """
    return

generate_word()