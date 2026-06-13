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
            finance.show_history()
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
            finance.add_transcation(amount, str(datetime.date.today()), transaction_type)

        elif choose == "4":
            print("Program za chwilę się wyłączy...")
            break
        else:
            print("Nieznana opcja! Wybierz ponownie.")

