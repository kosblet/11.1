import os
import pytest
from src.utils import read_csv_transactions, read_json_file, search_transactions_by_description

def test_read_csv_transactions_logs(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text("id;state;date;amount;currency_name;currency_code;from;to;description\n1;EXECUTED;2023-01-01;100;USD;;Visa;Mastercard;Test")
    read_csv_transactions(str(file))
    assert os.path.exists("utils.log")

def test_read_json_file_logs(tmp_path):
    file = tmp_path / "test.json"
    file.write_text('[{"id": 1, "description": "Test"}]')
    read_json_file(str(file))
    assert os.path.exists("utils.log")

def test_search_transactions_logs():
    transactions = [{"id": 1, "description": "Test"}, {"id": 2, "description": "Sample"}]
    search_transactions_by_description(transactions, "test")
    assert os.path.exists("utils.log")