from english_words import english_words_set
import random

def generate_word():
    """
    Generates a random five letter word in the English language.
    This five letter word is the solution to the game. 
    """
    # Make a list of all possible five letter words in the English language
    global five_letter_words
    five_letter_words = []
    for word in english_words_set:
        if len(word) == 5 and word[0].islower():
            five_letter_words.append(word)
    
    # Pick a random five letter word to be the solution 
    solution = random.choice(five_letter_words)
    print(solution)
    
    return solution

def word_guess(five_letter_words):
    """
    Gets user's guess for what the solution could be.
    Asks for another input if the user's guess doesn't satisfy the following two conditions:
        1) Length of the word is five letters
        2) Word is in the list five_letter_words (is real and isn't a proper noun)
    """
    # Gets user input
    guess = input('Enter your five-letter word guess here: ')

    # Checks that user's input satisfies all requirements and if not, asks for another guess
    while len(guess) != 5 or guess not in five_letter_words:
        guess = guess.lower()
        if len(guess) < 5 or len(guess) > 5 or guess not in five_letter_words:
            guess = input('Make sure your guess is five letters long, not a proper noun, and is real. Guess another word: ')

    return guess

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
word_guess(five_letter_words)