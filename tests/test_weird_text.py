import pytest

from weird_text.weird_text import WeirdText


@pytest.fixture()
def weird_text():
    return WeirdText()


def test_whether_decode_work_correctly(weird_text):
    input_text = (
        "\n—weird—\nTihs is a lnog loonog tset snetnece,"
        "\nwtih smoe big (biiiiig) wdors!\n—weird—\n"
        "long looong sentence some test This with words"
    )

    output = weird_text.decode(input_text)

    assert (
        output == "This is a long looong test sentence,"
        "\nwith some big (biiiiig) words!"
    )


def test_whether_encode_work_correctly(weird_text):
    input_text = "This is a long test,\na big (biiiiig) test!"

    output = weird_text.encode(input_text)

    assert (
        output == "\n—weird—\nTihs is a lnog tset,\n"
        "a big (biiiiig) tset!\n—weird—\n"
        "long test test This"
    )
