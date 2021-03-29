import re
from typing import Tuple, Dict

from weird_text.exceptions import DecodingException
from weird_text.parser import get_list_of_words


class Decoder:
    def decode(self, text: str) -> str:
        """
        Returns decoded text.

        Raises DecodingException when given text can not be decoded.
        """
        encoded_text, original_words = self._split_text(text)

        words = self._build_dict_of_words(encoded_text, original_words)

        re_replace = re.compile(r'\b({})\b'.format('|'.join(re.escape(word) for word in words.keys())))
        return re_replace.sub(lambda x: words[x.group(1)], encoded_text)

    @staticmethod
    def _build_dict_of_words(encoded_text: str, original_words: str) -> Dict[str, str]:
        words = get_list_of_words(encoded_text)
        original_words = get_list_of_words(original_words)
        words_ = {}

        for word in words:
            if len(word) > 3:
                for original_word in original_words:
                    if word[0] == original_word[0] and word[-1] == original_word[-1]:
                        if len(word) == len(original_word):
                            words_[word] = original_word
        return words_

    @staticmethod
    def _split_text(text: str) -> Tuple[str, str]:
        """ Split given text and returns two strings. """
        text = text.split("\n—weird—\n")
        if len(text) != 3:
            raise DecodingException(f"Can not decode given text: {text}")
        return text[1], text[2]
