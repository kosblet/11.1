# src/main.py

import json
import os

from masks import get_mask_account, get_mask_card_number


def load_data(filename):
    full_path = os.path.join(os.path.dirname(__file__), "..", "data", filename)
    with open(full_path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    try:
        transactions = load_data("transactions.json")
        print("✅ Данные загружены:", len(transactions), "транзакций\n")

        for t in transactions:
            # Получаем поля безопасно через .get()
            desc = t.get("description", "Не указано")

            operation_amount = t.get("operationAmount", {})
            amount = operation_amount.get("amount", "Не указана")
            currency_info = operation_amount.get("currency", {})
            currency = currency_info.get("code", "Не указана")

            from_acc = t.get("from", "Не указан")
            to_acc = t.get("to", "Не указан")

            # Маскируем "from"
            if from_acc != "Не указан":
                if "Счет" in from_acc:
                    from_acc = get_mask_account(from_acc)
                else:
                    from_acc = get_mask_card_number(from_acc)
            else:
                from_acc = "Не указан"

            # Маскируем "to" (всегда счет)
            to_acc = get_mask_account(to_acc)

            # Выводим информацию
            print(f"{desc}")
            print(f"Сумма: {amount} {currency}")
            print(f"Откуда: {from_acc}")
            print(f"Куда: {to_acc}\n")

    except FileNotFoundError:
        print("Файл данных не найден. Проверьте путь.")
    except Exception as e:
        print(f"Ошибка при выполнении программы: {e}")


if __name__ == "__main__":
    main()
