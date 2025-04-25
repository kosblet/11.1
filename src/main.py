from src.utils import (
    read_csv_transactions,
    read_excel_transactions,
    read_json_file,
    search_transactions_by_description,
    count_operations_by_categories,
)

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите источник данных:")
    print("1. JSON-файл")
    print("2. CSV-файл")
    print("3. XLSX-файл")

    choice = input("Введите номер пункта меню: ")
    if choice == "1":
        transactions = read_json_file("data/operations.txt")
    elif choice == "2":
        transactions = read_csv_transactions("data/transactions.csv")
    elif choice == "3":
        transactions = read_excel_transactions("data/transactions_excel.xlsx")
    else:
        print("Неверный выбор. Попробуйте снова.")
        return

    # Фильтрация по статусу
    while True:
        status = input("Введите статус (EXECUTED, CANCELED, PENDING): ").upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        print("Статус операции недоступен. Попробуйте снова.")

    filtered_transactions = [t for t in transactions if t.get("state", "").upper() == status]

    # Дополнительные фильтры
    sort_by_date = input("Отсортировать операции по дате? (да/нет): ").lower() == "да"
    if sort_by_date:
        order = input("По возрастанию или по убыванию? (возрастание/убывание): ").lower()
        reverse = order == "убывание"
        filtered_transactions.sort(key=lambda x: x.get("date", ""), reverse=reverse)

    rub_only = input("Выводить только рублевые транзакции? (да/нет): ").lower() == "да"
    if rub_only:
        filtered_transactions = [
            t for t in filtered_transactions
            if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]

    search_description = input("Отфильтровать список транзакций по слову в описании? (да/нет): ").lower() == "да"
    if search_description:
        search_string = input("Введите слово для поиска: ")
        filtered_transactions = search_transactions_by_description(filtered_transactions, search_string)

    # Вывод результата
    if filtered_transactions:
        print("Распечатываю итоговый список транзакций...")
        for t in filtered_transactions:
            print(t)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")