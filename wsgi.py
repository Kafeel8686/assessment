from flask import Flask, request, jsonify, render_template
from app.routes import ParagraphAnalyzer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # data = request.get_json()
    paragraph = request.form['paragraph']
    analyzer = ParagraphAnalyzer(paragraph)
    word_counts = analyzer.get_word_counts()
    sorted_word_counts = analyzer.get_sorted_word_counts()
    total_words = analyzer.total_words
    characters_with_spaces = analyzer.characters_with_spaces
    characters_without_spaces = analyzer.characters_without_spaces

    response = {
        'word_counts': word_counts,
        'sorted_word_counts': sorted_word_counts,
        'total_words': total_words,
        'characters_with_spaces': characters_with_spaces,
        'characters_without_spaces': characters_without_spaces
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0")