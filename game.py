import time


def is_game_complete(state: dict):
    """Return True if the game is complete, False otherwise."""
    if state["cursor_index"] == len(state["text"]):
        return True
    else:
        return False
    # return state["cursor_index"] == len(state["text"])  # TODO: Implement this function
    # return False  # TODO: Implement this function


def handle_game_complete(state: dict):  # Mutates the state
    """Handle the game completion."""
    result = is_game_complete(state)
    state['is_complete'] = result

    # TODO: Set the is_complete key in the state to True


def is_backspace(key):
    """Return True if the key is a backspace, False otherwise."""
    return key == "Backspace"  # TODO: Implement this function


def handle_backspace(state: dict):
    """Handle the backspace key."""
    result = is_backspace('key')

    # TODO: Should decrease the cursor index by 1 if the cursor index is not 0
    if state["cursor_index"] != 0:
        state["cursor_index"] -= 1
    else:
        state["cursor_index"] = 0
    # TODO: Should not change the cursor index if the cursor index is 0
    # TODO: Should update the char_states based on the cursor index


def is_key_correct(key, state: dict):
    """Return True if the key is correct, False otherwise."""
    return key == state['text']
    # TODO: Implement this function


def handle_correct_key(key, state: dict):  # Mutates the state
    """Handle the correct key."""
    # if result of is_key_correct is true
    if is_key_correct('key', state) == True:
        # TODO: Should update the cursor index
        state['cursor_index'] += 1
    # TODO: Update char_states based on the cursor index
        state['char_states'] = 1


def handle_incorrect_key(key, state: dict):  # Mutates the state
    """Handle the incorrect key."""
    # if result of is_key_correct is incorrect
    if is_key_correct == False:
        # TODO: Should update the cursor index
        state['cursor_index'] += 1
    # TODO: Update char_states based on the cursor index
        state['char_states'] = 2


def on_key_press(key, _state: dict):
    # Callback function for when a key is pressed.
    state = _state.copy()
    """
    # TODO: Remove this example, which increments the score by 1 when any key is pressed, and displays the time since the previous keypress
    state["score"] = state["score"] + 1
    previous_timestamp = state["previous_timestamp"]
    timestamp = time.time()
    delta_time = timestamp - previous_timestamp
    print(state["score"], delta_time)
    """
    # Refer to main.py for the state key schema
    # timestamp = time.time()
    # state["score"] = state["score"] + 1

    if state["cursor_index"] == len(state["text"]):
        # TODO: Handle edge case when game is complete, i.e. cursor_index == len(text)
        return state['score']
    if is_backspace(key):
        handle_backspace(state["text"])
        # TODO: Handle edge case when backspace is pressed
    if is_key_correct("text", state):
        handle_correct_key("text")
        # state["previous_timestamp"] = timestamp
        # TODO: Check if the key pressed is the correct key based on the cursor index and the text, and handle it accordingly
        # Last step: Update the previous_timestamp key in the state
        # state["previous_timestamp"] = timestamp
        # return state
    length = len(state["char_states"])
    for i in range(length):
        if i == 1:
            state["score"] = state["score"] + i
        else:
            state["score"] = state["score"] + i
    return state["score"]
