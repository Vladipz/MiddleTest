import pytest
from main import count_sentences


@pytest.mark.parametrize("text, expected", [
    ("Lorem ipsum.Dolor sit! Amet", 3),
    ("Lorem ipsum.. Dolor!? Sit amet", 3),
    ("Lorem ipsum. Dolor sit?Amet!", 3),
    ("", 0),
    ("This is a test", 1),
    ("One sentence. Second sentence!", 2),
    ("Another test? Yes, indeed.", 2),
    ("A test with... ellipsis.", 2),

    ])
def test_count_sentences_returns_correct_number_of_sentences(text: str, expected: int):
    assert count_sentences(text) == expected


