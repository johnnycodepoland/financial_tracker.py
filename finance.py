from utils import Utils

class Finance:
    def __init__(self):
        # Zmienna monitorująca aktualne saldo
        self.balance = 0

        # Słownik zapisujący wszystkie transakcje
        self.operations = {}

        # Wywołanie potrzebnych klas
        self.utils = Utils()

        # Tutaj próbujemy wczytać zmienne z pliku
        try:
            data = self.utils.load_transactions("data.json")
            self.balance = data["balance"]
            self.operations = data["operations"]
        except:
            pass

    # Funkcja dodająca transakcje
    def add_transcation(self, amount, date, transcation_type, transaction_category):
        self.operations[len(self.operations) +1] = {"amount": amount, "date": date, "type": transcation_type, "category": transaction_category}
        self.balance += amount
        self.utils.save_transactions({"balance": self.balance, "operations": self.operations}, "data.json")

    # Funkcja wypisująca aktulane saldo
    def show_balance(self):
        print(f"Saldo: {self.balance}")

    # Funkcja wypisująca historię transakcji
    def show_history(self, category=None, date=None):
        for key in self.operations:
            operation = self.operations[key]
            if category is not None and category not in operation["category"]:
                continue
            if date is not None and date not in operation["date"]:
                continue
            transaction_type = "wydatek" if operation['type'] == "expense" else "przychód"
            print(
                f"Numer: {key}, Kwota: {operation['amount']}, Typ: {transaction_type}, Data: {operation['date']}, Kategoria: {operation['category']}")
