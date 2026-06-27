import sys
from finance import Finance
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QPushButton, QHBoxLayout, QLabel, QTableWidget, QHeaderView, QTableWidgetItem
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        # Inicjalizacja klasy nadrzędnej, bez której program nie będzie poprawnie działał
        super().__init__()

        # Inicjalizujemy klasę finance
        self.finance = Finance()

        # Ustawiamy tytuł okna aplikacji
        self.setWindowTitle("Financial tracker")

        # Ustawiamy rozmiar okna
        self.setGeometry(100, 200, 1500, 800)

        # Pusty pojemnik na zawartość okna
        central_widget = QWidget()

        # Informacja dla okna o tym, że pojemnik, który przed chwilą utworzyliśmy jest jego wnętrzem
        self.setCentralWidget(central_widget)

        # Informacja dla pojemnika o tym, że ma wszystko układać pionowo
        self.layout = QVBoxLayout(central_widget)

        # Dodajemy nawigacje
        self.create_navigation()

        # Dodajemy dashboard
        self.create_dashboard()

    def create_navigation(self):
        # Tworzymy widget na zakładki
        tab_widget = QWidget()

        # Tworzymy layout dla widgetu na zakładki
        tab_layout = QHBoxLayout(tab_widget)

        # Dodajemy przycisk "Dodaj transakcje"
        transactions_button = QPushButton("Dodaj transakcje")

        # Dodajemy przycisk "Dodaj transakcje" do layoutu na zakładki
        tab_layout.addWidget(transactions_button)

        # Przesuwamy przyciski na prawą stronę
        tab_layout.addStretch()

        # Dodajemy przycisk "Dashboard"
        dashboard_button = QPushButton("Dashboard")

        # Dodajemy dashboard_button do layoutu na zakładki
        tab_layout.addWidget(dashboard_button)

        # Dodajemy przycisk "Transakcje"
        transactions_button = QPushButton("Transakcje")

        # Dodajemy dashboard_button do layoutu na zakładki
        tab_layout.addWidget(transactions_button)

        # Dodajemy przycisk "Cykliczne"
        cyclical_button = QPushButton("Cykliczne")

        # Dodajemy cyclical_button do layoutu na zakładki
        tab_layout.addWidget(cyclical_button)

        # Dodajemy przycisk "Raporty"
        report_button = QPushButton("Raporty")

        # Dodajemy report_button do layoutu na zakładki
        tab_layout.addWidget(report_button)

        # Ustawiamy maksymalną wielkość dla widgetu, tab_widget
        tab_widget.setMaximumHeight(50)

        # Dodajemy tab_widget do głównego layoutu
        self.layout.addWidget(tab_widget)

    # Główny dashboard
    def create_dashboard(self):
        # Tworzymy widget na treść
        content_widget = QWidget()

        # Tworzymy layout dla widgetu na treść
        self.content_layout = QVBoxLayout(content_widget)

        # Dodajemy widget na treść do głównego layoutu
        self.layout.addWidget(content_widget)

        # Wywołujemy widgety na górną i dolną treść
        self.create_top_section()

        self.create_bottom_section()

    # Górna część dashboardu
    def create_top_section(self):
        # Tworzymy widget na górną część treści
        top_widget = QWidget()

        # Tworzymy layout dla widgetu na górną część treści
        top_layout = QHBoxLayout(top_widget)

        # Dodajemy widget na górną część treści do layoutu na treść
        self.content_layout.addWidget(top_widget)

        # Dodajemy widget na balans
        balance_label = QLabel(f"Saldo: {self.finance.return_balance()}zł")

        # Ustawiamy styl widgetu na balans
        balance_label.setStyleSheet("background-color: white; border-radius: 10px; padding: 10px;")

        # Ustawiamy wielkość widgetu na balans
        balance_label.setFixedSize(600, 120)

        # Ustawiamy czcionkę i jej rozmiar
        balance_label.setFont(QFont("Arial", 70))

        # Dodajemy widget na wpłaty do górnego widgetu na treść
        top_layout.addWidget(balance_label)

        # Dodajemy widget na wpłaty
        income_label = QLabel(f"Wpłaty: {self.finance.return_income()}zł")

        # Ustawiamy styl widgetu na wpłaty
        income_label.setStyleSheet("background-color: white; border-radius: 10px; padding: 10px;")

        # Ustawiamy wielkość widgetu na wpłaty
        income_label.setFixedSize(400, 120)

        # Ustawiamy czcionkę i jej rozmiar
        income_label.setFont(QFont("Arial", 40))

        # Dodajemy widget na wpłaty do górnego widgetu na treść
        top_layout.addWidget(income_label)

        # Dodajemy widget na wydatki
        expense_label = QLabel(f"Wydatki: {self.finance.return_expense()}zł")

        # Ustawiamy styl widgetu na wydatki
        expense_label.setStyleSheet("background-color: white; border-radius: 10px; padding: 10px;")

        # Ustawiamy wielkość widgetu na wydatki
        expense_label.setFixedSize(400, 120)

        # Ustawiamy czcionkę i jej rozmiar
        expense_label.setFont(QFont("Arial", 40))

        # Dodajemy widget na wydatki do górnego widgetu na treść
        top_layout.addWidget(expense_label)

        # Wypychamy widget na saldo na maksa w lewo
        top_layout.addStretch()

    # Dolna część dashboardu
    def create_bottom_section(self):
        # Tworzymy widget na dolną część treści
        bottom_widget = QWidget()

        # Tworzymy layout dla widgetu na dolną część treści
        bottom_layout = QHBoxLayout(bottom_widget)

        # Dodajemy widget na dolną część treści do layoutu na treść
        self.content_layout.addWidget(bottom_widget)

        # Tworzymy "kontener" na historię transakcji, aby uniknąć błędu ze stylem widgetu na transakcje, który jest w formie tabeli
        table_container = QWidget()

        # Ustawiamy layout dla "kontenera" na historię transakcji
        table_layout = QVBoxLayout(table_container)

        # Ustawiamy wielkość "kontenera" na historię na transakcji
        table_container.setFixedSize(600, 480)

        # Dodajemy nazwę obiektu, dla table_container, aby uniknąć przekazywania stylu na "dzieci" table_container
        table_container.setObjectName("table_container")

        # Ustawiamy styl, tylko dla table_container bez przekazywania na jego "dzieci"
        table_container.setStyleSheet("#table_container {background-color: white; border-radius: 10px; padding: 10px;}")

        # Dodajemy widget na historię transakcji
        history_table = QTableWidget(0, 4)

        # Importujemy wszystkie transakcje, korzystając z funkcji show_history()
        transactions = self.finance.show_history()

        # Iterujemy przez wszystkie transakcje, aby dodać je do tabeli z ostatnimi transakcjami
        for transaction in transactions:
            row = history_table.rowCount()
            history_table.insertRow(row)
            amount = abs(transaction[1])
            history_table.setItem(row, 0, QTableWidgetItem(str(amount)))
            history_table.setItem(row, 1, QTableWidgetItem(str(transaction[2])))
            type = "wydatek" if transaction[3] == "expense" else "przychód"
            history_table.setItem(row, 2, QTableWidgetItem(type))
            history_table.setItem(row, 3, QTableWidgetItem(str(transaction[4])))

        # Ustawiamy automatyczne wypełnianie całej dostępnej przestrzeni przez kolumny
        history_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Dodajemy widget na historię transakcji do layoutu "kontenera" na transakcje
        table_layout.addWidget(history_table)

        # Ustawiamy nagłówki / nazwy kolumn dla tabeli history_table
        history_table.setHorizontalHeaderLabels(["Kwota", "Data", "Typ", "Kategoria"])

        # Dodajemy "kontener" na transakcje, do dolnego layoutu
        bottom_layout.addWidget(table_container)

        # Wypychamy dolną część treści na maksa w lewo
        bottom_layout.addStretch()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

