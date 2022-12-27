from app.routes import ParagraphAnalyzer
import pytest

def test_get_words():
    analyzer = ParagraphAnalyzer("This is a sample paragraph.")
    words = analyzer.get_words()
    assert words == ['This', 'is', 'a', 'sample', 'paragraph']

def test_get_word_counts():
    analyzer = ParagraphAnalyzer("This is a sample paragraph with some repeated words.")
    word_counts = analyzer.get_word_counts()
    assert word_counts == {'This': 1, 'is': 1, 'a': 1, 'sample': 1, 'paragraph': 1, 'with': 1, 'some': 1, 'repeated': 1, 'words': 1}

def test_get_sorted_word_counts():
    analyzer = ParagraphAnalyzer("This is a sample paragraph with some repeated words.")
    sorted_word_counts = analyzer.get_sorted_word_counts()
    assert sorted_word_counts == {'a': 1, 'is': 1, 'paragraph': 1, 'repeated': 1, 'sample': 1, 'some': 1, 'This': 1, 'with': 1, 'words': 1}

def test_total_words():
    analyzer = ParagraphAnalyzer("This is a sample paragraph.")
    total_words = analyzer.total_words
    assert total_words == 5

def test_characters_with_spaces():
    analyzer = ParagraphAnalyzer("This is a sample paragraph.")
    characters_with_spaces = analyzer.characters_with_spaces
    assert characters_with_spaces == 29

def test_characters_without_spaces():
    analyzer = ParagraphAnalyzer("This is a sample paragraph.")
    characters_without_spaces = analyzer.characters_without_spaces
    assert characters_without_spaces == 26
