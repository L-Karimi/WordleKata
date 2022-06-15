""" Wordle Engine module """

class Wordle:
    """ A Wordle-style game engine. """

    def __init__(self, target):
        """ Standard initialiser. """
        self.target = list(target)

    def guess(self, guess):
        """ Guess at the target word. """

        result = ["0", "0", "0", "0", "0"]

        for index, character in enumerate(list(guess)):
            guess_list = list(guess)
            character_count = guess_list[:index].count(character)

            if character == self.target[index]:
                result[index] = "2"
            elif self.target.count(character) > character_count:
                result[index] = "1"

        return ''.join(result)

if __name__ == '__main__':
    wordle = Wordle('hello')
    RESULT = wordle.guess('hello')
    print(RESULT)