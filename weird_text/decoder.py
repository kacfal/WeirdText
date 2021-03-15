from typing import Tuple

from weird_text.exceptions import DecodeError
from weird_text.parser import get_list_of_words


class Decoder:
    def decode(self, text: str) -> str:
        """
        Returns decoded text.

        Raises DecodeError when given text can not be decoded.
        """
        encoded_text, original_words = self._split_text(text)

        words = get_list_of_words(encoded_text)
        original_words = get_list_of_words(original_words)

        for word in words:
            for original_word in original_words:
                if sorted(word) == sorted(original_word):
                    encoded_text = encoded_text.replace(word, original_word)

        return encoded_text

    @staticmethod
    def _split_text(text: str) -> Tuple[str, str]:
        """ Split given text and returns two strings. """
        text = text.split("\n—weird—\n")
        if len(text) != 3:
            raise DecodeError(f"Can not decode given text: {text}")
        return text[1], text[2]
