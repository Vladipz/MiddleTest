import pytest
from main import count_words
@pytest.mark.parametrize("text, expected", [
    ("Lorem ipsum dolor sit amet", 5),
    ("Lorem;ipsum,dolor:sit,amet", 5),
    ("Lorem   ipsum   dolor   sit    amet", 5),
    ])
def test_count_words_returns_correct_number_of_words_in_one_sentence(text: str, expected: int):
    assert count_words(text) == expected


@pytest.mark.parametrize("text", [
    "",
    " ",
    "  ",
    ": ,;"
    ])
def test_count_words_returns_zero_when_no_words(text: str):
    assert count_words(text) == 0


@pytest.mark.parametrize("text, expected", [
    ("Lorem ipsum dolor sit amet. consectetur adipiscing elit. Donec nec odio.", 11),
    ("Lorem;ipsum,dolor:sit,amet. consectetur adipiscing elit. Donec nec odio.", 11),
    ("Lorem   ipsum   dolor   sit    amet. consectetur adipiscing elit.Donec nec odio.", 11),
    ])
def test_count_words_returns_correct_number_of_words_in_multiple_sentences(text: str, expected: int):
    assert count_words(text) == expected



