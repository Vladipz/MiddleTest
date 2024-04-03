
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("File not found.")
        return None

def count_words(text):
    separators = [' ', ',', ':', ';',".", "!", "?", "..."]  # роздільники слів
    for sep in separators:
        text = text.replace(sep, ' ')  # замінюємо роздільники пробілами
    words = text.split()  # Розділяємо текст на слова за пробілами
    return len(words)

def count_sentences(text):
    separators = ['.', '!', '?', '...']
    for separator in separators:
        text = text.replace(separator, '\n')
    parts = text.split('\n')
    parts = list(filter(lambda s: s != '', parts))
    return len(parts)


def analyze_text(file_path):
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



