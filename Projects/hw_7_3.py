import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(punct, ' ')
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        found_positions = {}
        for name, words in self.get_all_words().items():
            if word in words:
                found_positions[name] = words.index(word) + 1
            else:
                found_positions[name] = None
        return found_positions

    def count(self, word):
        word = word.lower()
        word_counts = {}
        for name, words in self.get_all_words().items():
            word_counts[name] = words.count(word)
        return word_counts
