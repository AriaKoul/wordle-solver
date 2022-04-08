# Wordle Solver

## Background
The online game Wordle has become one of the most popular games on the internet. The link to play this game is below:

[Wordle from the New York Times](https://www.nytimes.com/games/wordle/index.html)

I set out to replicate the game of Wordle myself and create a logical way of solving each 5x5 puzzle when the user is given six tries to guess the Wordle. 

## How to Use
Clone this repository using the following code: 

`$ git clone https://github.com/AriaKoul/wordle-solver`

## Dependencies
To execute this code, you will need Python3, and the following Python modules: random and collections.

To install Python, visit [the Python website] (https://www.python.org/downloads/).

To install these modules, use the following commands:

`$ pip install random collections`

## Descriptions
`utility_functions.py`

This file includes seven different functions which either correspond to creating the actual Wordle game or to solving the game. The functions `generate_list()`, `generate_word()`, and `word_guess()` create the game. The functions `score_guess()`, `count_unique_letters`, `generate_best_guesses`, and `generate_possible_solutions()` solve the game. 

`words.txt`
This text file includes a long list of five letter words from the English language that are used to get a solution for each Wordle game and to check that the user gives an actual English five letter word as input for each of their tries. 

`tests.py`

This file contains all of the necessary tests to check if the code is working as expected.  
