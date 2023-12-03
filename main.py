import ui
import input
import game
import load

state = {
    "score": 0,
    "text": "Hello world!",  # TODO: Make this a random string of characters
    "char_states": [
        1,
        1,
        1,
        2,
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

config = {}


def main():
    """Main function when the program is run."""
    global state
    global config

    config = load.load_user_config()

    if not "name" in config:
        config["name"] = input.get_name()
        load.write_user_config(config)

    # Initialize the game state
    state = load.init_game_state()
    window = ui.init_window()

    # Callback function for when a key is pressed

    def key_pressed(key):
        """Callback function for when a key is pressed."""
        global state
        # Update the state based on the key pressed
        state = game.on_key_press(key, state)

        if (state["is_complete"]):
            score = state["score"]
            highscore = config["highscore"] if "highscore" in config else 0
            if score > highscore:
                config["highscore"] = score
                load.write_user_config(config)

        # Redraw the game window
        ui.draw_ui(window, state, config)

    # Bind the keypress event to the window
    input.bind_keypress_event(window, key_pressed)
    input.bind_backspace_event(window, key_pressed)

    # Draw the first game window
    ui.draw_ui(window, state, config)

    window.mainloop()


if __name__ == "__main__":
    main()
