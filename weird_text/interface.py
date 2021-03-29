from weird_text.decoder import Decoder
from weird_text.encoder import Encoder


class WeirdText:
    def __init__(self) -> None:
        self.encoder = Encoder()
        self.decoder = Decoder()

    def encode(self, text: str) -> str:
        """
        Returns encoded text.

        example:
            input text:

                ‘This is a long looong test sentence,\n’
                ‘with some big (biiiiig) words!’

            output text:

                ‘\n—weird—\n’
                ‘Tihs is a lnog loonog tset sntceene,\n’
                ‘wtih smoe big (biiiiig) wdros!’
                ‘\n—weird—\n’
                ‘long looong sentence some test This with words’

        :param text: Any text
        :returns: Encoded text with sorted list of original words.
        """
        return self.encoder.encode(text)

    def decode(self, text: str) -> str:
        """
        Returns decoded text.

        example:
            input text:
                ‘\n—weird—\n’
                ‘Tihs is a lnog loonog tset sntceene,\n’
                ‘wtih smoe big (biiiiig) wdros!’
                ‘\n—weird—\n’
                ‘long looong sentence some test This with words’

            output text:
                ‘This is a long looong test sentence,\n’
                ‘with some big (biiiiig) words!’

        :param text: Text encoded by method encode from WeirdText.
        :returns: Decode text.
        :raises DecodingException when given text dose not came from method encode from WeirdText.
        """
        return self.decoder.decode(text)
