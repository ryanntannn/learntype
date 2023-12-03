def bind_keypress_event(window, callback):
    """Bind a keypress event to the window. The callback function is called when a key is pressed, with the key as the argument."""

    def _callback(_event):
        if not _event.char.isalnum() and _event.char != " " and _event.char != "." and _event.char != ",":
            return
        callback(_event.char)

    window.bind("<Key>", _callback)


def bind_backspace_event(window, callback):
    """Bind a backspace event to the window. The callback function is called when the backspace key is pressed."""

    def _callback(_event):
        callback("Backspace")

    window.bind("<BackSpace>", _callback)
