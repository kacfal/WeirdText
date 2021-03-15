import random

from weird_text.parser import get_list_of_words


class Encoder:
    def __init__(self):
        self._original_words = []

    @property
    def original_words(self) -> str:
        return " ".join(sorted(self._original_words, key=str.lower))

    def encode(self, text: str) -> str:
        """ Returns encoded text. """
        template = "\n—weird—\n{}\n—weird—\n{}"
        words = get_list_of_words(text)

        for word in words:
            shuffled_word = self.shuffle_word(word)
            text = text.replace(word, shuffled_word)

        return template.format(text, self.original_words)

    def shuffle_word(self, word: str) -> str:
        """ Gets single word and shuffled it if it possible. """
        if self._normalized_word_and_check_len(word):
            return word

        middle_word = list(word[1:-1])
        random.shuffle(middle_word)
        shuffled_word = word.replace(word[1:-1], "".join(middle_word))

        if shuffled_word == word:
            return self.shuffle_word(word)

        self._original_words.append(word)
        return shuffled_word

    @staticmethod
    def _normalized_word_and_check_len(word) -> bool:
        return True if len(set(word[1:-1])) < 2 else False
