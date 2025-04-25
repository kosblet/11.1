import sys
import os
from src.processing import filter_operations_by_status, reorder_operations_by_date

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))


def test_filter_operations_executed():
    operations = [
        {"id": 1, "status": "COMPLETED"},
        {"id": 2, "status": "PENDING"},
        {"id": 3, "status": "COMPLETED"},
    ]
    result = filter_operations_by_status(operations, "COMPLETED")
    assert len(result) == 2


def test_filter_operations_pending():
    operations = [
        {"id": 1, "status": "COMPLETED"},
        {"id": 2, "status": "PENDING"},
        {"id": 3, "status": "COMPLETED"},
    ]
    result = filter_operations_by_status(operations, "PENDING")
    assert len(result) == 1


def test_filter_operations_no_match():
    operations = [
        {"id": 1, "status": "COMPLETED"},
        {"id": 2, "status": "PENDING"},
        {"id": 3, "status": "COMPLETED"},
    ]
    result = filter_operations_by_status(operations, "CANCELED")
    assert len(result) == 0


def test_reorder_operations_descending():
    operations = [
        {"id": 1, "timestamp": "2023-01-01"},
        {"id": 2, "timestamp": "2023-01-02"},
        {"id": 3, "timestamp": "2023-01-01"},
    ]
    result = reorder_operations_by_date(operations, descending=True)
    assert result[0]["id"] == 2


def test_reorder_operations_ascending():
    operations = [
        {"id": 1, "timestamp": "2023-01-01"},
        {"id": 2, "timestamp": "2023-01-02"},
        {"id": 3, "timestamp": "2023-01-01"},
    ]
    result = reorder_operations_by_date(operations, descending=False)
    assert result[0]["id"] == 1
