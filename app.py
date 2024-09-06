from flask import Flask, request, jsonify
from transformers import pipeline
import logging

app = Flask(__name__)

# Logging konfigurieren
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Definiere die Übersetzungs-Pipelines für unterstützte Sprachen
translators = {
    'de': pipeline("translation_en_to_de"),
    'en': pipeline("translation_de_to_en"),
    'sr': pipeline("translation_en_to_sr"),
    'tr': pipeline("translation_en_to_tr"),
    # Weitere Sprachen und Modelle hier hinzufügen
}

@app.route('/translate', methods=['POST'])
def translate():
    logger.debug("Anfrage an /translate empfangen")
    
    data = request.json
    logger.debug("Empfangene Daten: %s", data)
    
    texts = data.get('texts')  # Liste von Texten
    target_language = data.get('target_language')
    
    if target_language not in translators:
        logger.error("Unsupported language: %s", target_language)
        return jsonify({'error': 'Unsupported language'}), 400

    translator = translators[target_language]
    
    try:
        translations = [translator(text)[0]['translation_text'] for text in texts]
        logger.debug("Übersetzungen: %s", translations)
        return jsonify({'translations': translations})
    except Exception as e:
        logger.error("Fehler bei der Übersetzung: %s", e)
        return jsonify({'error': 'Translation error'}), 500

if __name__ == '__main__':
    app.run(debug=True)