""" This module contains the UI for the application. """

from tkinter import *
import sys
from tkinter.font import BOLD

# Window size in pixels
WINDOW_X = 350
WINDOW_Y = 200

IS_MAC = sys.platform == "darwin"

FONT = "Menlo" if IS_MAC else "Consolas"
BACKGROUND_COLOR = "#323437"  # HEX format

print(sys.platform)


def window_size(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Get in millimeters (mm)
    screen_heightmm = window.winfo_screenmmheight()
    screen_widthmm = window.winfo_screenmmwidth()
    return (screen_width, screen_height, screen_heightmm, screen_widthmm)


def init_window():
    """Initialize the window and return it."""
    global WINDOW_X, WINDOW_Y
    window = Tk()
    window.resizable(False, False)
    window.title("LearnType")
    _window_size = window_size(window)
    window.configure(bg=BACKGROUND_COLOR, cursor="dotbox")
    WINDOW_X = _window_size[0] - 10 if IS_MAC else _window_size[0]
    WINDOW_Y = _window_size[1] - 70 if IS_MAC else _window_size[1]

    window.geometry(f"{WINDOW_X}x{WINDOW_Y}")
    return window


def clear_window(window):
    """Clear the window of all widgets."""
    for widget in window.winfo_children():
        widget.destroy()


def draw_ui(window, state: dict):
    """Draw a text area with the given the current game state."""
    clear_window(window)

    # Draw the game screen if the game is not complete, otherwise draw the end screen
    if state['is_complete']:
        # End Screen
        txt = Label(window, text="Game Over!", background=BACKGROUND_COLOR
                      ,font=(FONT, 60), foreground="#323535", bg="#e2b714")
        txt.pack(side="top", fill=X, expand=False)
        draw_end_screen_ui(window, state)
    else:
        # Normal Screen
        txt = Label(window, text="Game On!", background=BACKGROUND_COLOR
                      ,font=(FONT, 60), foreground="#323535", bg="#e2b714")
        txt.pack(side="top", fill=X, expand=False)
        draw_game_ui(window, state)


def draw_game_ui(window, state: dict):
    """Draw the game screen with the given game state."""
    global BACKGROUND_COLOR
    box_width = WINDOW_X/2

    # TODO: Draw score at the top right corner of the window

    #Score
    score = str(state['score'])
    canvas = Canvas(window, width = 150, height = 40, bg = BACKGROUND_COLOR)
    canvas.create_text(75, 10, text=("Score:", score), fill="white", font=(FONT,14), anchor="n")
    canvas.config(highlightthickness=0, borderwidth=0)
    canvas.pack(side=TOP, anchor="ne")


    #Title
    title = Canvas(window, bg=BACKGROUND_COLOR, width=150, height=40)
    title.create_text(75, 20, text="LearnType", fill="white", font=(FONT, 16, BOLD))
    title.place(width=box_width)
    title.pack(side=TOP, anchor="center")
    

    # TODO: Draw current text based on text, char_states, and cursor_index
    text_data = state['text']
    cursor = state['cursor_index']
    
    _text = Text(window, wrap=WORD, font=(FONT, 18), autoseparators=TRUE)

    # Set colors
    _text.tag_configure("wrong", background="red", foreground="black")
    _text.tag_configure("correct", foreground="white")
    _text.tag_configure("untyped", foreground="grey")

    _text.tag_configure("location", underline=TRUE, foreground="grey")

    for i in range(len(state['char_states'])):

        if state['char_states'][i] == 1:
            # Red
            _text.insert(END, text_data[i], "correct")
        elif state['char_states'][i] == 2:
            # Green
            _text.insert(END, text_data[i], "wrong")
        elif state["char_states"][i] == 0:
            # Grey
            # Show cursor in current location
            if cursor == i:
                _text.insert(END, text_data[i], "location")
            else:
                _text.insert(END, text_data[i], "untyped")

    _text.place(x=10, y=10, width=box_width)
    _text.config(highlightthickness=0, borderwidth=0,
                 background=BACKGROUND_COLOR, state="disabled", cursor="dotbox")
    _text.pack(side=TOP, expand=TRUE)


def draw_end_screen_ui(window, state: dict):
    """Draw the end screen with the given game state."""
    print("end")
    pass
