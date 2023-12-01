import time


def is_game_complete(state: dict):
    """Return True if the game is complete, False otherwise."""
    return state["cursor_index"] == len(state["text"])  # TODO: Implement this function
    # return False  # TODO: Implement this function


def handle_game_complete(state: dict):  # Mutates the state
    """Handle the game completion."""
    result=is_game_complete(state)
    if result == True:
        state['is_complete'] = True
    else:
        state['is_complete'] = False
        
    # TODO: Set the is_complete key in the state to True


def is_backspace(key):
    """Return True if the key is a backspace, False otherwise."""
    return key == "<BackSpace>"  # TODO: Implement this function


def handle_backspace(state: dict):
    """Handle the backspace key."""
    


    # TODO: Should decrease the cursor index by 1 if the cursor index is not 0
    if cursor_index != 0:
        cursor_index -= 1
    # TODO: Should not change the cursor index if the cursor index is 0
    # TODO: Should update the char_states based on the cursor index
    char_states = is_key_correct(state)


def is_key_correct(key, state: dict):
    """Return True if the key is correct, False otherwise."""
    return key == state['text']
    # TODO: Implement this function


def handle_correct_key(key, state: dict):  # Mutates the state
    """Handle the correct key."""
    # TODO: Should update the cursor index
    cursor_index += 1
    # TODO: Update char_states based on the cursor index
    char_states = 1
    # TODO: Update score based on the cursor index


def handle_incorrect_key(key, state: dict):  # Mutates the state
    """Handle the incorrect key."""
    # TODO: Should update the cursor index
    cursor_index += 1
    # TODO: Update char_states based on the cursor index
    char_states = 2


def on_key_press(key, _state: dict):
    """Callback function for when a key is pressed."""
    state = _state.copy()

    # TODO: Remove this example, which increments the score by 1 when any key is pressed, and displays the time since the previous keypress
    state["score"] = _state["score"] + 1
    previous_timestamp = _state["previous_timestamp"]
    timestamp = time.time()
    delta_time = timestamp - previous_timestamp
    print(state["score"], delta_time, key)

    # Refer to main.py for the state key schema

if cursor_index == len(text):
    # TODO: Handle edge case when game is complete, i.e. cursor_index == len(text)


    # TODO: Handle edge case when backspace is pressed
if is_backspace(key_pressed):

    # TODO: Check if the key pressed is the correct key based on the cursor index and the text, and handle it accordingly

    # Last step: Update the previous_timestamp key in the state
    state["previous_timestamp"] = timestamp
    return state
