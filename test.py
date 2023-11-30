import unittest
import game

TEST_STATE = {
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
    "previous_timestamp": -1,  # Timestamp of the previous keypress, -1 if no previous keypress
    "is_complete": False,
}


class TestGame(unittest.TestCase):
    def test_is_game_complete(self):
        _test_state = TEST_STATE.copy()
        # Should be false when cursor index is not at the end of the text
        self.assertFalse(game.is_game_complete(_test_state))

        _test_state["cursor_index"] = len(_test_state["text"])
        # Should be true when cursor index is at the end of the text
        self.assertTrue(game.is_game_complete(_test_state))

    def test_handle_game_complete(self):
        _test_state = TEST_STATE.copy()
        game.handle_game_complete(_test_state)
        # Should set is_complete to True
        self.assertTrue(_test_state["is_complete"])

    def test_handle_backspace(self):
        _test_state = TEST_STATE.copy()

        # Should decrease the cursor index by 1 if the cursor index is not 0
        _test_state["cursor_index"] = 1
        game.handle_backspace(_test_state)
        self.assertEqual(_test_state["cursor_index"], 0)
        self.assertEqual(_test_state["char_states"][0], 0)

        # Should not change the cursor index if the cursor index is 0
        _test_state["cursor_index"] = 0
        game.handle_backspace(_test_state)
        self.assertEqual(_test_state["cursor_index"], 0)
        self.assertEqual(_test_state["char_states"][0], 0)

    def test_is_key_correct(self):
        # Should be true when the key is correct
        self.assertTrue(game.is_key_correct("H", TEST_STATE))
        # Should be false when the key is incorrect
        self.assertFalse(game.is_key_correct("h", TEST_STATE))

    def test_handle_correct_key(self):
        TEST_STATE["cursor_index"] = 0
        # Should update the cursor index
        game.handle_correct_key("H", TEST_STATE)
        self.assertEqual(TEST_STATE["cursor_index"], 1)
        self.assertEqual(TEST_STATE["char_states"][0], 1)

    def test_handle_incorrect_key(self):
        TEST_STATE["cursor_index"] = 0
        # Should update the cursor index
        game.handle_incorrect_key("h", TEST_STATE)
        self.assertEqual(TEST_STATE["cursor_index"], 1)
        self.assertEqual(TEST_STATE["char_states"][0], 2)


if __name__ == "__main__":
    unittest.main()
