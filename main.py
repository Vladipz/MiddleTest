def read_file(file_path: str) -> str:
    """
    Read the contents of a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str or None: The contents of the text file if it exists, None otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("File not found.")
        return None

def count_words(text: str) -> int:
    """
    Count the number of words in the given text.

    Args:
        text (str): The input text.

    Returns:
        int: The number of words in the text.
    """
    separators = [' ', ',', ':', ';', '.', '!', '?', '...']  # word separators
    for sep in separators:
        text = text.replace(sep, ' ')  # replace separators with spaces
    words = text.split()  # Split the text into words by spaces
    return len(words)

def count_sentences(text: str) -> int:
    """
    Count the number of sentences in the given text.

    Args:
        text (str): The input text.

    Returns:
        int: The number of sentences in the text.
    """
    separators = ['.', '!', '?', '...']
    for separator in separators:
        text = text.replace(separator, '\n')  # Replace sentence separators with newlines
    parts = text.split('\n')
    parts = list(filter(lambda s: s != '', parts))  # Filter out empty parts
    return len(parts)

def analyze_text(file_path: str) -> tuple[int, int]:
    """
    Analyze a text file and count the number of words and sentences.

    Args:
        file_path (str): The path to the text file.

    Returns:
        tuple: A tuple containing the number of words and sentences in the text file.
               
    """
    text = read_file(file_path)
    if text:
        num_words = count_words(text)
        num_sentences = count_sentences(text)
        return num_words, num_sentences
    else:
        return None, None


# Приклад використання:
if __name__ == "__main__":
    file_path = "test.txt"  # Вкажіть шлях до свого файлу
    num_words, num_sentences = analyze_text(file_path)
    if num_words is not None and num_sentences is not None:
        print("Кількість слів у тексті:", num_words)
        print("Кількість речень у тексті:", num_sentences)



