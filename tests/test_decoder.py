import pytest

from weird_text.decoder import Decoder
from weird_text.exceptions import DecodingException


@pytest.fixture()
def decoder():
    return Decoder()


def test_whether_decoder_decoding_text(decoder):
    input_text = (
        "\n—weird—\n"
        "Tihs is a lnog loonog tset snetnece,"
        "\nwtih smoe big (biiiiig) wdors!"
        "\n—weird—\n"
        "long looong sentence some test This with words"
    )

    output = decoder.decode(input_text)

    assert (
        output == "This is a long looong test sentence,"
        "\nwith some big (biiiiig) words!"
    )


def test_whether_decoder_raise_exception_with_msg(decoder):
    input_text = (
        "Tihs is a lnog loonog tset snetnece,"
        "\nwtih smoe big (biiiiig) wdors!"
        "long looong sentence some test This with words"
    )

    with pytest.raises(DecodingException) as e:
        decoder.decode(input_text)
        assert e == f"Can not decode given text: {input_text}"
