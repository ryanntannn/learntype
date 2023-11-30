import ui
import input
import game
import load

state = {
    "score": 0,
    "text": "Hello world!",  # TODO: Make this a random string of characters
    "char_states": [0 for _ in range(12)],  # 0 = untyped, 1 = correct, 2 = incorrect
    "cursor_index": 0,  # Index of the cursor in the text
    "previous_timestamp": -1,  # Timestamp of the previous keypress, -1 if no previous keypress
    "is_complete": False,
}


def main():
    """Main function when the program is run."""
    global state
    window = ui.init_window()

    # Callback function for when a key is pressed
    def key_pressed(key):
        """Callback function for when a key is pressed."""
        global state
        _new_state = state.copy()
        if state["cursor_index"] >= len(state["text"]):
            _new_state["is_complete"] = True
        else:
            _new_state["score"] = state["score"] + 1
            _new_state["char_states"][_new_state["cursor_index"]] = (
                state["cursor_index"] % 2 + 1
            )
            _new_state["cursor_index"] = (_new_state["cursor_index"] + 1) % len(
                _new_state["text"]
            )
        state = _new_state

        # Redraw the game window
        ui.draw_ui(window, state)

    # Bind the keypress event to the window
    input.bind_keypress_event(window, key_pressed)
    ui.draw_ui(window, state)
    window.mainloop()


if __name__ == "__main__":
    main()
