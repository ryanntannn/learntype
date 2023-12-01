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
    # Timestamp of the previous keypress, -1 if no previous keypress
    "previous_timestamp": -1,
    "is_complete": False,
}


def temp_init_game_state():
    """Initialize the game state."""
    text = "Do not pity the dead, Harry. Pity the living, and, above all those who live without love."

    return {
        "score": 0,
        "text": text,
        "char_states": [0] * len(text),
        "cursor_index": 0,
        "previous_timestamp": -1,
        "is_complete": False,
    }


def init_game_state():
    """Initialize the game state."""
    # TODO: Generate game state based on file input

    # TODO: Remove this line when you are done and return the generated game state instead
    return temp_init_game_state()
