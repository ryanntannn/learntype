""" This module contains the UI for the application. """

from tkinter import *

# Window size in pixels
WINDOW_X = 350
WINDOW_Y = 200


def init_window():
    """Initialize the window and return it."""
    window = Tk()
    window.title("LearnType")
    window.geometry(f"{WINDOW_X}x{WINDOW_Y}")
    return window


def clear_window(window):
    """Clear the window of all widgets."""
    for widget in window.winfo_children():
        widget.destroy()


def draw_ui(window, state: dict):
    """Draw a text area with the given the current game state."""
    clear_window(window)
    # TODO: Draw the game screen if the game is not complete, otherwise draw the end screen


def draw_game_ui(window, state: dict):
    """Draw the game screen with the given game state."""

    # TODO: Draw score at the top right corner of the window

    # TODO: Draw current text based on text, char_states, and cursor_index


def draw_end_screen_ui(window, state: dict):
    """Draw the end screen with the given game state."""
