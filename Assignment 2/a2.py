"""
Author: Harmanpreet Singh Phull
Desc: A basic version of the game 'Wordle'
"""

from collections.abc import MutableSet
from random import choice

class WordleWords(MutableSet):
    """
    A class the represents the set of words to be used for the game
    """
    def __init__(self, letters):
        """
        Initializes the class
        Input: int
        Return: N/A
        """
        self._letters = letters
        self._words = set()

    def __contains__(self, word):
        """
        Checks if the specified word is in the set
        Input: string
        Return: bool
        """
        return word in self._words

    def __iter__(self):
        """
        Runs an iterator over the set of words
        Input: N/A
        Return: iter object
        """
        return iter(self._words)

    def __len__(self):
        """
        Returns the number of words in the set
        Input: N/A
        Return: int
        """
        return len(self._words)

    def add(self, word):
        """
        Adds the specified word to the set
        Input: string
        Return: N/A
        """
        try:
            # checks if the word to be added is valid or not
            self.check_word(word)
        except ValueError:
            pass
        else:
            # adds the word if there is no error
            self._words.add(word)

    def discard(self, word):
        """
        Removes the specified word from the
        Input: string
        Return: N/A
        """
        if (self.__contains__(word)):
            # checks whether the word is present in the set
            self._words.discard(word)
        else:
            print(f"{word} is not present in the set")

    def load_file(self, filename):
        """
        Gets all the words from the specified file
        Input: string
        Return: N/A
        """
        with open(filename, 'r') as file:
            word = file.readline().strip()
            while not word == "":
                # loops until the file is empty
                self.add(word)
                word = file.readline().strip()

    def check_word(self, word):
        """
        Checks if the word meets the specified criteria
        Input: string
        Return: N/A
        """
        if (len(word) > self.letters()):
            raise TooLongError
        if (len(word) < self.letters()):
            raise TooShortError
        for letter in word:
            if (ord(letter) > 90 or ord(letter) < 65):
                # checks if every letter of the word is between A and Z
                raise NotLettersError

    def letters(self):
        """
        Returns the number of letters each word has
        Input: N/A
        Return: int
        """
        return self._letters

    def copy(self):
        """
        Makes a copy of this instance of the class
        Input: N/A
        Return: WordleWord instance
        """
        Copy = WordleWords(self.letters())
        for word in self.__iter__():
            # loops over all the words in one instance and adds them to the Copy class
            WordleWords.add(Copy, word)
        return Copy

class TooShortError(ValueError):
    pass

class TooLongError(ValueError):
    pass

class NotLettersError(ValueError):
    pass

class Guess():
    """
    A class that represents the guess made by a user
    """
    def __init__(self, guess, answer):
        """
        Initializes the class
        Input: string, string
        Return: N/A
        """
        self._guess = guess
        self._answer = answer

    def guess(self):
        """
        Returns the guess made
        Input: N/A
        Return: string
        """
        return self._guess

    def correct(self):
        """
        Returns a string that shows all the correct letters in the guess made
        Input: N/A
        Return: string
        """
        Correct = ["_"] * len(self._answer)
        # makes a "blank" list that's as long as the answer
        for index in range(len(self._answer)):
            if (self._guess[index] == self._answer[index]):
                # if the letters at the specified index are the same
                # replaces the _ in Correct with that letter
                Correct[index] = self._answer[index]
        return "".join(Correct)  # joins the list into a string

    def misplaced(self):
        """
        Returns all the correct letter that weren't at the write place
        Input: N/A
        Return: string
        """
        Misplaced = []
        for index in range(len(self._answer)):
            Letter = self._answer[index]
            # the letter at the current index in the answer
            if (Letter in self._guess and self._answer[index] != self._guess[index]):
                # if the letter is in the guess but not at the same position
                # appends it to the Misplaces list
                Misplaced.append(Letter)
        Misplaced.sort()  # sorts the list
        return "".join(Misplaced)

    def wrong(self):
        """
        Returns all the letters that aren't in the answer
        Input: N/A
        Return: string
        """
        Wrong = []
        Answer = list(self._answer)  # makes a list version of the answer string
        for letter in self._guess:
            if (letter in Answer):
                # if the current letter is in the answer removes that letter from the answer so duplicate letters can be detected
                Answer.remove(letter)
            else:
                # if the current letter is not in the answer appends it to the Wrong list
                Wrong.append(letter)
        Wrong.sort()
        return "".join(Wrong)

    def is_win(self):
        """
        Returns if the user won or not
        Input: N/A
        Return: bool
        """
        return self._guess == self._answer

class Wordle():
    """
    A class that represents a game of Wordle
    """
    def __init__(self, words):
        """
        Initializes the class
        Input: WordleWord instance
        Return: N/A
        """
        self._word = choice(list(words._words))  # gets a random word from words
        self._guesses = 0

    def guesses(self):
        """
        Returns the number of guesses the user made
        Input: N/A
        Return: int
        """
        return self._guesses

    def guess(self, guessed):
        """
        Returns a Guess instance that represents the guess the user made
        Input: string
        Return: Guess instance
        """
        self._guesses += 1
        GuessWord = Guess(guessed, self._word)
        return GuessWord

def main():
    #Test Code
    Wordleword = WordleWords(5)
    Wordleword.load_file("words.txt")
    print(Wordleword.__len__())
    WordleCopy = Wordleword.copy()
    print(WordleCopy.__len__())
    Guess1 = Guess("YOYOS", "BONUS")
    print(Guess1.correct())
    print(Guess1.misplaced())
    print(Guess1.wrong())
    print(Wordleword.__iter__())
    WorldeGame = Wordle(Wordleword)

main()