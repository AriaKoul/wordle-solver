from utility_functions import score_guess, generate_best_guesses

def test_score_guess():
    assert score_guess("found", "mound") == 'RGGGG'
    assert score_guess("found", "jkjac") == 'RRRRR'
    assert score_guess("found", "fuonk") == 'GYYGR'
    assert score_guess("found", "munkd") == 'RYYRG'
    # assert test_score_guess("found", "mound") == 'XZZZZ'
    # assert test_score_guess("found", "mound") == 'XZZZZ'
    # assert test_score_guess("found", "mound") == 'XZZZZ'
    # assert test_score_guess("found", "mound") == 'XZZZZ'

def test_generate_best_guesses():
    assert generate_best_guesses(["abcdd", "abcde"]) == ["abcde"]

test_score_guess()
test_generate_best_guesses()
