from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_guess_above_secret_is_too_high_not_too_low():
    # FIX: before the fix, secret was cast to str on even attempts causing
    # lexicographic comparison — check_guess(9, 10) returned "Too High"
    # because "9" > "10" in string ordering.
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"
