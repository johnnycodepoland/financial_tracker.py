from PyQt6.QtWidgets import QDialog, QWidget, QVBoxLayout, QLineEdit


class AddTransactionDialog(QDialog):
    def __init__(self):

        # Inicjalizacja klasy nadrzędnej, bez której program nie będzie poprawnie działał
        super().__init__()

        # Ustawiamy tytuł okna formularza
        self.setWindowTitle("Add transaction")

        # Dodajemy layout
        central_layout = QVBoxLayout(self)

        # Tworzymy obiekt QLineEdit, który pozwoli nam wprowadzać tekst
        amount_input = QLineEdit()

        # Ustawiamy nazwę dla placeholderu, do przyjmowania kwoty transakcji
        amount_input.setPlaceholderText("Kwota")

        # Dodajemy widget do wprowadzania kwoty
        central_layout.addWidget(amount_input)