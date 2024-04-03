from main import read_file
import os
import pytest

@pytest.fixture(autouse=True)
def prepare_text_file(tmp_path):
    target_file = os.path.join(tmp_path, "test.txt")
    with open(target_file, "w") as file:
        lines = ["Lorem ipsum dolor sit amet.\n",
                 "Consectetur adipiscing elit. Donec nec odio."]
        file.writelines(lines)
    return target_file


def test_read_file_returns_text_from_file(prepare_text_file):
    assert read_file(prepare_text_file) == "Lorem ipsum dolor sit amet.\nConsectetur adipiscing elit. Donec nec odio."


def test_read_file_returns_none_when_file_not_found():
    assert read_file("nonexistent_file.txt") is None
