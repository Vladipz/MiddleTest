import pytest
from main import analyze_text

# Fixture to provide sample text file
@pytest.fixture
def text_file(tmp_path):
    file_content = "This is a sample text file.\nIt contains multiple lines.\nAnd sentences too!"
    file_path = tmp_path / "sample.txt"
    with open(file_path, "w") as file:
        file.write(file_content)
    return str(file_path)

def test_analyze_text_with_valid_file(text_file):
    num_words, num_sentences = analyze_text(text_file)
    assert num_words == 13  # Expected number of words in the sample text
    assert num_sentences == 3  # Expected number of sentences in the sample text

def test_analyze_text_with_invalid_file():
    num_words, num_sentences = analyze_text("non_existent_file.txt")
    assert num_words is None
    assert num_sentences is None
