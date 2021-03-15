import re
import random

from typing import List


class Encoder:
    def __init__(self):
        self._original_words = []

    @property
    def original_words(self):
        return " ".join(sorted(self._original_words, key=str.lower))

    def encode(self, text: str) -> str:
        template = "\n—weird—\n{}\n—weird—\n{}"
        words = self._get_list_of_words(text)

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
    def _get_list_of_words(text: str) -> List[str]:
        tokenize_re = re.compile(r"(\w+)", re.U)
        return tokenize_re.findall(text)

    @staticmethod
    def _normalized_word_and_check_len(word) -> bool:
        return True if len(set(word[1:-1])) < 2 else False
