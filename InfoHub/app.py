from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Definiere die Übersetzungs-Pipelines für unterstützte Sprachen
translators = {
    'de': pipeline("translation", model="Helsinki-NLP/opus-mt-en-de"),  # Englisch zu Deutsch
    'en': pipeline("translation", model="Helsinki-NLP/opus-mt-de-en"),  # Deutsch zu Englisch
    'sr': pipeline("translation", model="Helsinki-NLP/opus-mt-en-sr"),  # Englisch zu Serbo-Kroatisch
    'tr': pipeline("translation", model="Helsinki-NLP/opus-mt-en-tr"),  # Englisch zu Türkisch
}

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    texts = data.get('texts')  # Liste von Texten
    target_language = data.get('target_language')

    if target_language not in translators:
        return jsonify({'error': 'Unsupported language'}), 400

    translator = translators[target_language]
    translations = [translator(text)[0]['translation_text'] for text in texts]
    
    return jsonify({'translations': translations})

if __name__ == '__main__':
    app.run(debug=True)