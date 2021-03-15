import pytest

from weird_text.encoder import Encoder


@pytest.fixture()
def encoder():
    return Encoder()


@pytest.mark.parametrize("word, expected", [("is", "is"), ("a", "a"), ("Big", "Big")])
def test_whether_shuffle_word_not_shuffled_word_shorter_than_3_letters(
    word, expected, encoder
):
    encoder.shuffle_word(word)

    assert encoder.shuffle_word(word) == expected


@pytest.mark.parametrize(
    "word, expected", [("Long", "Lnog"), ("some", "smoe"), ("test", "tset")]
)
def test_whether_shuffle_word_shuffled_word_with_4_letters(word, expected, encoder):
    encoder.shuffle_word(word)

    assert encoder.shuffle_word(word) == expected


@pytest.mark.parametrize("word", ["sentence", "words", "Looong"])
def test_whether_shuffle_word_shuffled_word_with_more_than_4_letters(word, encoder):
    encoder.shuffle_word(word)

    assert encoder.shuffle_word(word) != word
    assert encoder.shuffle_word(word)[-1:1] == word[-1:1]


@pytest.mark.parametrize(
    "word, expected", [("biiiiig", "biiiiig"), ("Nooooo", "Nooooo")]
)
def test_whether_shuffle_word_not_shuffled_word_with_the_same_letters_in_the_middle(
    word, expected, encoder
):
    encoder.shuffle_word(word)

    assert encoder.shuffle_word(word) == expected


def test_whether_encode_return_correct_template(encoder):
    template = "\n—weird—\n\n—weird—\n"

    assert encoder.encode("") == template


def test_whether_encode_encoding_whole_sentence(encoder):
    input_text = "This is a long test,\na big (biiiiig) test!"

    output = encoder.encode(input_text)

    assert (
        output == "\n—weird—\nTihs is a lnog tset,\n"
        "a big (biiiiig) tset!\n—weird—\n"
        "long test test This"
    )


def test_whether_original_words_return_not_shuffled_and_sorted_words(encoder):
    input_text = "This is a long looong test sentence,\nwith some big (biiiiig) words!"

    print(encoder.encode(input_text))

    assert encoder.original_words == "long looong sentence some test This with words"
