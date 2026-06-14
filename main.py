import datetime
from finance import Finance

if __name__ == "__main__":
    finance = Finance()
    while True:
        print("================================")
        print("  WITAJ W PANELU UŻYTKOWNIKA  ")
        print("================================")
        print("Wybierz jedną z poniższych opcji:")
        print("1. Wyświetl saldo")
        print("2. Wyświetl historię")
        print("3. Dodaj transakcję")
        print("4. Zamknij program")

        choose = input("Wybierz akcję do wykonania: ")


        if choose == "1":
            finance.show_balance()
        elif choose == "2":
            while True:
                filter_by_category = input("Czy chcesz filtrować po kategorii (t/n): ")

                if filter_by_category == "t":
                    category = input("Podaj kategorie transakcji: ")
                    break
                elif filter_by_category == "n":
                    category = None
                    break
                else:
                    print("Podano niepoprawną opcję")

            while True:
                filter_by_date = input("Czy chcesz filtrować po dacie (t/n): ")

                if filter_by_date == "t":
                    while True:
                        try:
                            date = str(input("Podaj datę transakcji (YYYY-MM-DD): "))
                            datetime.datetime.strptime(date, "%Y-%m-%d")  # ta funkcja pozwala nam
                            break
                        except:
                            print("Podano niepoprawny format daty")
                    break
                elif filter_by_date == "n":
                    date = None
                    break
                else:
                    print("Podano niepoprawną opcję")
            finance.show_history(category, date)
        elif choose == "3":
            while True:
                transaction_type = input("Podaj typ transakcji (wydatek, przychód): ")

                if transaction_type == "wydatek":
                    transaction_type = "expense"
                    break
                elif transaction_type == "przychód":
                    transaction_type = "income"
                    break
                else:
                    print("Podano niepoprawny typ transakcji")
            try:
                amount = float(input("Podaj kwotę transakcji: "))
            except ValueError:
                print("Podaj niepoprawną kwotę transakcji")
                continue
            if transaction_type == "expense":
                amount = 0 - amount
            category = input("Podaj kategorie transakcji: ")
            finance.add_transcation(amount, str(datetime.date.today()), transaction_type, category)

        elif choose == "4":
            print("Program za chwilę się wyłączy...")
            break
        else:
            print("Nieznana opcja! Wybierz ponownie.")

