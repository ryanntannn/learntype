def bind_keypress_event(window, callback):
	""" Bind a keypress event to the window. The callback function is called when a key is pressed, with the key as the argument. """
	def _callback(_event):
		callback(_event.char)

	window.bind("<Key>", _callback)