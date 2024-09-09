# termin.py
from flask import Flask, jsonify, send_file
import WebUntis_Crawler
import json

app = Flask(__name__)

@app.route('/run-crawler', methods=['GET'])
def run_crawler():
    try:
        # Führe den Crawler aus und sammle Lehrerinformationen
        lehrer_liste = WebUntis_Crawler.start_crawler()
        
        # Debug-Ausgabe in der Konsole
        print("Lehrer gefunden:", lehrer_liste)
        
        if not lehrer_liste:
            return jsonify({'success': False, 'message': 'Keine Lehrer gefunden'})
        
        # Speichern der Lehrerliste in einer JSON-Datei
        with open('teachers.json', 'w') as f:
            json.dump({'teachers': lehrer_liste}, f)
        
        # Sende die JSON-Daten zurück
        return jsonify({'success': True, 'teachers': lehrer_liste})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)