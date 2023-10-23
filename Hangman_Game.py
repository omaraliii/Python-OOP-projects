import random

HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\\',
    '|       |',
    '|      / \\'
]

WORDS = [
    'CASA', 'CARRO', 'MONO', 'ESTERNOCLEIDOMASTOIDEO', 'PYTHON', 'DJANGO',
    'MILTON', 'LENIS', 'SWAPPS', 'LOGIA', 'UNITTESTING'
]


class Hangman:

    def __init__(self, word_to_guess):
        self.word_to_guess = word_to_guess
        self.failed_attempts = 0
        self.game_progress = ['_'] * len(self.word_to_guess)
        self.guessed_letters = []

    def find_index(self, letter):
        indexes = []
        for i in range(len(self.word_to_guess)):
            if self.word_to_guess[i] == letter:
                indexes.append(i)
        return indexes

    def is_valid_letter(self, input_):
        return input_.isalpha() and len(input_) == 1

    def print_game_status(self):
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print('\n')
        print(' '.join(self.game_progress))
        print('Guessed Letters: ' + ', '.join(self.guessed_letters))

    def update_progress(self, letter, indexes):
        for index in indexes:
            self.game_progress[index] = letter

    def get_user_input(self):
        while True:
            user_input = input('\nPlease type a letter: ')
            if self.is_valid_letter(user_input) and user_input not in self.guessed_letters:
                return user_input
            else:
                if user_input in self.guessed_letters:
                    print('You already guessed that letter.')
                else:
                    print('Invalid input. Please enter a single letter.')

    def play(self):
        while self.failed_attempts < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()
            self.guessed_letters.append(user_input)

            if user_input in self.word_to_guess:
                indexes = self.find_index(user_input)
                self.update_progress(user_input, indexes)

                if self.game_progress.count('_') == 0:
                    print('\n¡Yay! You win!')
                    print('The word is: {0}'.format(self.word_to_guess))
                    return

            else:
                self.failed_attempts += 1

        print("\n¡OMG! You lost!")
        print('The word was: {0}'.format(self.word_to_guess))


if __name__ == '__main__':
    word_to_guess = random.choice(WORDS)
    hangman = Hangman(word_to_guess)
    hangman.play()
