import time

def on_key_press(key, _state: dict):
	""" Callback function for when a key is pressed. """
	state = _state.copy()

	# TODO: Remove this example, which increments the score by 1 when any key is pressed, and displays the time since the previous keypress
	state["score"] = _state["score"] + 1
	previous_timestamp = _state["previous_timestamp"]
	timestamp = time.time()
	delta_time = timestamp - previous_timestamp
	state["previous_timestamp"] = timestamp
	print(state["score"], delta_time)
	
	# Refer to main.py for the state key schema

	# TODO: Handle edge case when game is complete, i.e. cursor_index == len(text)

	# TODO: Handle edge case when backspace is pressed

	#	TODO: Check if the key pressed is the correct key based on the cursor index and the text

	# TODO: Update the score and char_states based on the key pressed

	return state