""" Wordle engine unit tests """

import unittest
import wordle

class TestWordle(unittest.TestCase):
    """ Unit tests for Wordle """

    def test_no_matching_characters(self):
        """
        No matching characters
        Target = “ropes”
        Guess  = “child”
        Result = “00000”
        """

        target = "ropes"
        guess = "child"
        expected_result = "00000"

        sut = wordle.Wordle(target)

        self.assertEqual(sut.guess(guess), expected_result)

    def test_characters_match_in_correct_positions(self):
        """
        Characters match in correct positions
        Target = “alert”
        Guess  = “alarm”
        Result = “22020”
        """

        target = "alert"
        guess = "alarm"
        expected_result = "22020"

        sut = wordle.Wordle(target)

        self.assertEqual(sut.guess(guess), expected_result)

    def test_character_in_wrong_position(self):
        """
        Character in wrong position
        Target = “stair”
        Guess  = “chore”
        Result = “00010”
        """

        target = "stair"
        guess = "chore"
        expected_result = "00010"

        engine = wordle.Wordle(target)

        self.assertEqual(engine.guess(guess), expected_result)

    def test_mix_of_match_and_wrong_position(self):
        """
        Mix of match and wrong position
        Target = “hairy”
        Guess  = “charm”
        Result = “01120”
        """

        target = "hairy"
        guess = "charm"
        expected_result = "01120"

        sut = wordle.Wordle(target)

        self.assertEqual(sut.guess(guess), expected_result)

    def test_multiple_characters_in_wrong_positions(self):
        """
        Multiple characters in wrong positions
        Target = “reads”
        Guess  = “elect”
        Result = “10000”
        """

        target = "reads"
        guess = "elect"
        expected_result = "10000"

        sut = wordle.Wordle(target)

        self.assertEqual(sut.guess(guess), expected_result)

if __name__ == '__main__':
    unittest.main()