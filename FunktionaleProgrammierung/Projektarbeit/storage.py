import json
import os

# Change current working directory to the directory of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def save_result(result):
    """Speichert das Spielergebnis in einer JSON-Datei."""
    results = load_results()
    results.append(result)
    with open('results.json', 'w') as file:
        json.dump(results, file)

def load_results():
    """Lädt die bisherigen Spielergebnisse aus einer JSON-Datei."""
    if os.path.exists('results.json'):
        with open('results.json', 'r') as file:
            return json.load(file)
    return []
