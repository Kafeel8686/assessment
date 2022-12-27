import re
from collections import Counter

class ParagraphAnalyzer:
    def __init__(self, paragraph):
        self.paragraph = paragraph
        self.words = self.get_words()
        self.characters_with_spaces = len(self.paragraph)
        self.characters_without_spaces = len(re.sub(r'\s', '', self.paragraph))
        self.total_words = len(self.words)

    def get_words(self):
        """Extracts the words from the paragraph and returns them as a list"""
        words = re.findall(r'\b[a-z0-9]+\b', self.paragraph, flags=re.IGNORECASE)
        return words

    def get_word_counts(self):
        """Counts the repetition of each word and returns a dictionary with the counts"""
        word_counts = Counter(self.words)
        return dict(word_counts)

    def get_sorted_word_counts(self):
        """Counts the repetition of each word, sorts the words alphabetically,
        and returns a dictionary with the counts"""
        word_counts = self.get_word_counts()
        sorted_word_counts = {k: v for k, v in sorted(word_counts.items())}
        return sorted_word_counts


if __name__ == "__main__":
    paragraph = "This is a sample paragraph. It has a few words and some numbers 12345."
    analyzer = ParagraphAnalyzer(paragraph)
    word_counts = analyzer.get_word_counts()
    sorted_word_counts = analyzer.get_sorted_word_counts()
    total_words = analyzer.total_words
    characters_with_spaces = analyzer.characters_with_spaces
    characters_without_spaces = analyzer.characters_without_spaces
