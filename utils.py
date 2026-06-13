import json

class Utils:
    # Funkcja zapisująca transakcję, do pliku json
    def save_transactions(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f)

    # Funkcja ładująca wszystkie transakcje, z pliku json
    def load_transactions(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            return data
