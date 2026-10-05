#REFACTOR: Refactored logic into logic_utils.py using manual mode.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100

#REFACTOR: Refactored logic into logic_utils.py using manual mode.
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

#FIX: Refactored logic into logic_utils.py using manual mode. While working with Claude,
#I noticed that the return statements where unintuitive (example: "TOO HIGH", "📈 Go HIGHER!"),
#so we fixed that. Also there was a type error so Claude suggested forcing the secret to an INT instead
#of a string.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    secret_int = int(secret)

    if guess == secret_int:
        return "Win", "🎉 Correct!"

    if guess > secret_int:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"

"""FIX: Refactored logic into logic_utils.py using manual mode. Claude noted that there was
an odd parity-based rule where 5 was being added on even attempts and 5 was being subtracted
on odd attempts. I told it to ignore it for now, since I wanted to focus on the first two rows
in the table to fix."""
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
