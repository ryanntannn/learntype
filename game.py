import time


def is_game_complete(state: dict):
    """Return True if the game is complete, False otherwise."""
    return state["cursor_index"] == len(state["text"])


def handle_game_complete(state: dict):  # Mutates the state
    """Handle the game completion."""
    state['is_complete'] = True


def is_backspace(key):
    """Return True if the key is a backspace, False otherwise."""
    return key == "Backspace"


def handle_backspace(state: dict):
    """Handle the backspace key."""
    if state["cursor_index"] != 0:
        state["cursor_index"] -= 1
    else:
        state["cursor_index"] = 0
    state["char_states"][state["cursor_index"]] = 0


def is_key_correct(key, state: dict):
    """Return True if the key is correct, False otherwise."""
    return key == state["text"][state["cursor_index"]]


def handle_correct_key(key, state: dict):  # Mutates the state
    """Handle the correct key."""
    _prev_cursor_index = state['cursor_index']
    state['cursor_index'] += 1
    state['char_states'][_prev_cursor_index] = 1


def handle_incorrect_key(key, state: dict):  # Mutates the state
    """Handle the incorrect key."""
    _prev_cursor_index = state['cursor_index']
    state['cursor_index'] += 1
    state['char_states'][_prev_cursor_index] = 2


def on_key_press(key, _state: dict):
    """ Callback function for when a key is pressed. """
    state = _state.copy()

    if is_game_complete(state):
        handle_game_complete(state)
        return state

    if is_backspace(key):
        handle_backspace(state)
        return state

    if is_key_correct(key, state):
        handle_correct_key(key, state)
    else:
        handle_incorrect_key(key, state)

    length = len(state["char_states"])
    for i in range(length):
        if i == 1:
            state["score"] = state["score"] + i
        else:
            state["score"] = state["score"] + i

    return state
