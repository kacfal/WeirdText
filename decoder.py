import re
from typing import List, Tuple


class DecodeError(Exception):
    pass


class Decoder:
    def decode(self, text: str) -> str:
        encoded_text, original_words = self._split_text(text)

        words = self._get_list_of_words(encoded_text)
        original_words = self._get_list_of_words(original_words)

        for word in words:
            for original_word in original_words:
                if sorted(word) == sorted(original_word):
                    encoded_text = encoded_text.replace(word, original_word)

        return encoded_text

    @staticmethod
    def _split_text(text: str) -> Tuple[str, str]:
        text = text.split('\n—weird—\n')
        if len(text) != 3:
            raise DecodeError(f"Can not decode given text: {text}")
        return text[1], text[2]

    @staticmethod
    def _get_list_of_words(text: str) -> List[str]:
        return re.findall(r"(\w+)", text, re.U)
