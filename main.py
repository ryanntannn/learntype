import ui
import input
import game
import load

state = {
	"score": 0, 
	"text": "Hello world!", # TODO: Make this a random string of characters
	"char_states": [1,1,1,2,0,0,0,0,0,0], # 0 = untyped, 1 = correct, 2 = incorrect
	"cursor_index": 0, # Index of the cursor in the text
	"previous_timestamp": -1, # Timestamp of the previous keypress, -1 if no previous keypress
	"is_complete": False
}

def key_pressed(key):
	""" Callback function for when a key is pressed. """
	# Update the state based on the key pressed
	state = game.on_key_press(key, state)

	# Redraw the game window
	ui.draw_game_window(window, state)

def main(): 
	""" Main function when the program is run. """
	window = ui.init_window()

	input.bind_keypress_event(window, key_pressed)

	state = load.init_game_state()

	ui.draw_game_window(window, state)

	window.mainloop()

if __name__ == '__main__':
	main()
