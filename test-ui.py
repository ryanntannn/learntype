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
    "previous_timestamp": -1,  # Timestamp of the previous keypress, -1 if no previous keypress
    "is_complete": False,
}


def main():
    """Main function when the program is run."""
    global state
    window = ui.init_window()
    ui.draw_ui(window, state)
    window.mainloop()


if __name__ == "__main__":
    main()
