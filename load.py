import ui
import random
from tkinter import *
from tkinter import filedialog
import time
import sys

# Window size in pixels
WINDOW_X = 350
WINDOW_Y = 200

IS_MAC = sys.platform == "darwin"

FONT = "Menlo" if IS_MAC else "Consolas"
BACKGROUND_COLOR = "#323437"  # HEX format

DEFAULT_STATE = {
    "score": 0,
    "text": "Hello world!",  # TODO: Make this a random string of characters
    "char_states": [
        0,
        0,
        0,
        0,
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

'''def temp_init_game_state():
    """Initialize the game state."""
    text = "Do not pity the dead, Harry. Pity the living, and, above all those who live without love."

    return {
        "score": 0,
        "text": text,
        "char_states": [0] * len(text),
        "cursor_index": 0,
        "previous_timestamp": -1,
        "is_complete": False,
    }'''

def init_game_state():
	""" Initialize the game state. """
	file_name=filedialog.askopenfilename(initialdir='/', title='Select a text file', filetypes=(('Text files', '*.txt*'),('all files', '*.*')))
	
	# Making new state dictionary
	new_state=DEFAULT_STATE.copy()
	
    # Opening users file
	input_file=open(file_name, 'r')
	
    # Reading file and making a list of paragraphs
	new_text_list=input_file.read().split('\n\n')
	
    # Choosing a random paragraph
	new_text=new_text_list[random.randint(0, len(new_text_list)-1)]
	
	# Assigning new paragraph to the new_state dictionary
	new_state["text"]=new_text
	
    # Assigning new character state to the new_state dictionary
	new_state["char_states"]=[0]*len(new_text)
	
	return new_state
