""" This module contains the UI for the application. """

from tkinter import *
import msvcrt

# Window size in pixels
WINDOW_X = 350
WINDOW_Y = 200

FONT = "Consolas"
BACKGROUND_COLOR = "#323437"  #HEX format


def window_size(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    #Get in mmillimeters (mm)
    screen_heightmm = window.winfo_screenmmheight()
    screen_widthmm = window.winfo_screenmmwidth()
    return (screen_width, screen_height, screen_heightmm, screen_widthmm)



def init_window():
    """Initialize the window and return it."""
    global WINDOW_X, WINDOW_Y
    window = Tk()
    window.resizable(False,False)
    window.title("LearnType")
    _window_size = window_size(window)
    window.configure(bg=BACKGROUND_COLOR)
    WINDOW_X = _window_size[0]
    WINDOW_Y = _window_size[1]


    window.geometry(f"{_window_size[0]}x{_window_size[1]}")
    return window


def clear_window(window):
    """Clear the window of all widgets."""
    for widget in window.winfo_children():
        widget.destroy()



def draw_ui(window, state: dict):
    """Draw a text area with the given the current game state."""
    clear_window(window)
    # stringify the game state and display it in the window
    text = str(state)
    #score = str(state['score'])
    #print(score)
    print(text)
    text_area = Label(window, text=text)
    #text_area.pack()
    
    text_area.configure(font=(FONT, 12))

    # TODO: Draw the game screen if the game is not complete, otherwise draw the end screen
    if state['is_complete']:
        #End Screen
        draw_end_screen_ui(window, state)
    else:
        #Normal Screen
        draw_game_ui(window, state)
        


def draw_game_ui(window, state: dict):
    """Draw the game screen with the given game state."""
    global BACKGROUND_COLOR

    # TODO: Draw score at the top right corner of the window
    score = str(state['score'])
    #canvas = Canvas(window, width = 1000, height = 750, bg = "SpringGreen2")
    #canvas.create_text(300, 50, text="HELLO WORLD", fill="black", font=('Helvetica 15 bold'))
    #canvas.pack()
    #canva.grid(row=0, column=0)

    box_width = WINDOW_X/2
    
    # TODO: Draw current text based on text, char_states, and cursor_index
    text_data = state['text']
    
    cursor = state['cursor_index']
    print(text_data[cursor])


    #Set colors
    _text = Text(window, wrap=WORD, font=(FONT,18))
    _text.tag_configure("red", background="red", foreground="black")
    _text.tag_configure("green", foreground="white")
    _text.tag_configure("grey", foreground="grey")

    for i in range(len(state['char_states'])):
        #print(state['char_states'][i])
        #print(text_data[i])

        if state['char_states'][i] == 1:
            #Red
            _text.insert(END, text_data[i], "red")
        elif state['char_states'][i] == 2:
            #Green
            _text.insert(END, text_data[i], "green")
        else:
            #Grey
            _text.insert(END, text_data[i], "grey")

    
    _text.place(x=10, y=10, width=box_width)
    #_text.bind("<Button-1>", leftClick(_text))
    _text.config(highlightthickness=0, borderwidth=0, background=BACKGROUND_COLOR)
    
    _text.pack()

    
    

def draw_end_screen_ui(window, state: dict):
    """Draw the end screen with the given game state."""
    print("end")
    pass
