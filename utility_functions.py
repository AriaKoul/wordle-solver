from english_words import english_words_set
import random

def generate_list():
    """
    Plurals are not included in this and we can add the "s" to any four letter word.
    This function creates a list full of all five letter words in the English language.
    """
    five_letter_words = []
    for word in english_words_set:
        # if len(word) == 4 and word[0].islower():
        #     five_letter_words.append(f"{word}s")

        if len(word) == 5 and word[0].islower():
            five_letter_words.append(word)
    
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


def generate_possible_solutions(guess_history):
    """
    Takes the guess history of the user, which is a dictionary that has the following
    strucuture: {"guess": "result"}.
    Based on the result and the guess, this function generates all possible words that 
    do not violate the criterion from the most recent guess and returns all of these possible 
    words as a list.
    """
    
    possible_solutions = generate_list()
    # Iterate over items in guess history to remove invalid words from possible solutions
    return possible_solutions

def generate_best_guesses(word_list):
    """
    This function takes a list of words and returns all the words with the maximum amount of 
    unique letters. This is done in order to generate a list of the best possible guesses that
    could lead the user to eventually getting the solution. 
    """
    best_guesses = []
    # for word in 
    return best_guesses 

  
score_guess(generate_word(), word_guess()) 