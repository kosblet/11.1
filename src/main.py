import json
import os
from masks import mask_card_number, mask_account
from utils import search_transactions, categorize_transactions

def load_data(filename):
    full_path = os.path.join(os.path.dirname(__file__), "..", "data", filename)
    with open(full_path, "r", encoding="utf-8") as f:
        return json.load(f)

def filter_by_status(transactions, status):
    return [t for t in transactions if t.get("state", "").upper() == status.upper()]

def sort_by_date(transactions, reverse=False):
    from datetime import datetime
    def parse_date(t):
        return datetime.fromisoformat(t.get("date", ""))
    return sorted(transactions, key=parse_date, reverse=reverse)

def filter_by_currency(transactions, currency):
    return [
        t for t in transactions
        if t.get("operationAmount", {}).get("currency", {}).get("code") == currency
    ]

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("\nПользователь: ").strip()
    if choice != "1":
        print("На данный момент поддерживаются только JSON-файлы.\n")
        return

    try:
        transactions = load_data("transactions.json")
        print("Для обработки выбран JSON-файл.")

        # Фильтрация по статусу
        while True:
            print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
            print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
            status = input("Пользователь: ").strip().upper()
            if status not in ["EXECUTED", "CANCELED", "PENDING"]:
                print(f'Статус операции "{status}" недоступен.')
                continue
            filtered = filter_by_status(transactions, status)
            print(f'Операции отфильтрованы по статусу "{status}"')
            break

        # Сортировка по дате
        sort_choice = input("\nОтсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
        if sort_choice == "да":
            order = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
            filtered = sort_by_date(filtered, reverse="убыв" in order)
            print("Операции отсортированы по дате.")

        # Фильтр по валюте
        rub_filter = input("\nВыводить только рублёвые транзакции? Да/Нет\nПользователь: ").strip().lower()
        if rub_filter == "да":
            filtered = filter_by_currency(filtered, "RUB")
            print("Фильтрация по рублям завершена.")

        # Поиск по описанию
        search_choice = input("\nОтфильтровать список транзакций по слову в описании? Да/Нет\nПользователь: ").strip().lower()
        if search_choice == "да":
            keyword = input("Введите ключевое слово:\nПользователь: ").strip()
            filtered = search_transactions(filtered, keyword)
            print("Фильтрация по ключевому слову завершена.")

        if not filtered:
            print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
            return

        print("\nРаспечатываю итоговый список транзакций...")
        print(f"\nВсего банковских операций в выборке: {len(filtered)}\n")

        for t in filtered:
            description = t["description"]
            amount = t["operationAmount"]["amount"]
            currency = t["operationAmount"]["currency"]["code"]

            from_acc = t.get("from", "Не указан")
            to_acc = t.get("to", "Не указан")

            if "Счет" in from_acc:
                from_acc = mask_account(from_acc)
            else:
                from_acc = mask_card_number(from_acc)

            to_acc = mask_account(to_acc)

            print(f"{description}")
            print(f"{from_acc} -> {to_acc}")
            print(f"Сумма: {amount} {currency}\n")

    except FileNotFoundError:
        print("❌ Файл данных не найден. Проверьте путь.")
    except Exception as e:
        print(f"⚠️ Ошибка при выполнении программы: {e}")

if __name__ == "__main__":
    main()