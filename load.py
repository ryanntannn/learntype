DEFAULT_STATE = {
    "score": 0,
    "text": "Hello world!",  # TODO: Make this a random string of characters
    "char_states": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ],  # 0 = untyped, 1 = correct, 2 = incorrect
    "cursor_index": 0,  # Index of the cursor in the text
    "previous_timestamp": -1,  # Timestamp of the previous keypress, -1 if no previous keypress
    "is_complete": False,
}


def init_game_state():
    """Initialize the game state."""
    # TODO: Generate game state based on file input

    # TODO: Remove this line when you are done and return the generated game state instead
    return DEFAULT_STATE.copy()
