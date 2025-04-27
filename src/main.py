import logging
from src.utils import (
    read_csv_transactions,
    sort_transactions_by_date,
    filter_transactions_by_date
)

# Настройка логгера
logger = logging.getLogger("main_logger")
logger.setLevel(logging.DEBUG)

# Настройка file_handler
file_handler = logging.FileHandler("main.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Настройка форматтера
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def main():
    # Чтение данных из CSV файла
    csv_file_path = "data/transactions.csv"
    transactions = read_csv_transactions(csv_file_path)

    if not transactions:
        logger.error("Не удалось прочитать данные из CSV файла.")
        return

    # Сортировка транзакций по дате
    sorted_transactions = sort_transactions_by_date(transactions, reverse=True)
    logger.info("Транзакции успешно отсортированы по дате.")

    # Фильтрация транзакций по диапазону дат
    start_date = "2023-01-01T00:00:00Z"
    end_date = "2023-12-31T23:59:59Z"
    filtered_transactions = filter_transactions_by_date(sorted_transactions, start_date, end_date)
    logger.info(f"Транзакции успешно отфильтрованы за период {start_date} - {end_date}.")

    # Вывод результатов
    print("Отсортированные и отфильтрованные транзакции:")
    for transaction in filtered_transactions:
        print(transaction)


if __name__ == "__main__":
    main()