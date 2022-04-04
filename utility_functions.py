from english_words import english_words_set
import random
from collections import Counter
import hashlib


def generate_list():
    """
    Plurals are not included in this and we can add the "s" to any four letter word.
    This function creates a list full of all five letter words in the English language.
    """
    five_letter_words = []
    all_words = open('words.txt', 'r')
    for word in all_words:
        if "'" not in word:
            five_letter_words.append(word[0:5])

    all_words.close()
    return five_letter_words

def generate_word():
    """
    Generates and returns a random five letter word in the English language.
    This five letter word is the solution to the game. 
    """

    # Pick a random five letter word to be the solution 
    solution = random.choice(generate_list())
    print(solution)
    return solution

def word_guess():
    """
    Gets user's guess for what the solution could be and returns it.
    Asks for another input if the user's guess doesn't satisfy the following two conditions:
        1) Length of the word is five letters
        2) Word is in the list five_letter_words (is real and isn't a proper noun)
    """
    # Gets user input
    guess = input('Enter your five-letter word guess here: ').lower()
    # Checks that user's input satisfies all requirements and if not, asks for another guess
    while len(guess) != 5 or guess not in generate_list():
        guess = input('Make sure your guess is five letters long, not a proper noun, and is real. Guess another word: ')

    return guess

def score_guess(solution, guess):
    """
    Takes the user's guess and scores it based on what the solution is. Below is a key for how
    you can interpret the score:
        R - character is not in the word
        Y - character is in the word but in the wrong spot
        G - character is in the word and in the right spot
    Returns the result in string form.
    """
    result = ''
    for i in range(len(solution)):
        if solution[i] == guess[i]:
            result += 'G'
        elif guess[i] in solution:
            result += 'Y'
        else:
            result += 'R'
    print(result)
    return result

def count_unique_letters(word):
    unique_letters = len(list(Counter(word).keys()))
    return unique_letters

def generate_best_guesses(word_list):
    """
    This function takes a list of words and returns all the words with the maximum amount of 
    unique letters. This is done in order to generate a list of the best possible guesses that
    could lead the user to eventually getting the solution. 
    """
    best_guesses = []
    unique_letter_dict = dict()

    for word in word_list:
        unique_letter_dict[word] = count_unique_letters(word)
    max_unique_letters = max(list(unique_letter_dict.values()))

    for key in unique_letter_dict:
        if unique_letter_dict[key] == max_unique_letters:
            best_guesses.append(key)

    return best_guesses 

def generate_possible_solutions(guess_history):
    """
    Takes the guess history of the user, which is a dictionary that has the following
    structure: {"guess": "result"}.
    Based on the result and the guess, this function generates all possible words that 
    do not violate the criterion from the most recent guess and returns all of these possible 
    words as a list.
    """
    
    possible_solutions = set()
    # all_words_1 = generate_list()
    # all_words_2 = all_words_1

    all_words_1 = ['found', 'mound', 'emcee']
    all_words_2 = all_words_1

    print(len(possible_solutions))
    # Iterate over items in guess history to remove invalid words from possible solutions
    for guess in guess_history:
        for i in range(len(guess)):
            
            if guess_history[guess][i] == 'R':
                for word in all_words_1:
                    if guess[i] not in word:
                        possible_solutions.add(word)

            if guess_history[guess][i] == 'G':
                for word in all_words_1:
                    remove = False
                    if guess[i] != word[i]:
                        remove = True
                        try:
                            all_words_1.remove(word)
                        except ValueError:
                            pass
                    print(f"This is the guess: {guess[i]}")
                    print(f"This is the word: {word[i]}")
                    if remove:
                        print(f"Removed {word}")
                    else:
                        print(f"Did not remove {word}")

    possible_solutions.update(all_words_1)
    print(len(possible_solutions))
    print(possible_solutions)
    return possible_solutions 

# For this logic, there are some unexpected words in the output

# generate_possible_solutions({"white": "RRRRR", "found": "RGGGG", "phone": "RRYGR"})
generate_possible_solutions({"found": "GGGGG"})