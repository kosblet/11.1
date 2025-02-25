def filter_operations_by_status(operations_list: list, operation_status: str) -> list:
    return [op for op in operations_list if op.get("status") == operation_status]


def reorder_operations_by_date(operations_list: list, descending: bool = True) -> list:
    return sorted(
        operations_list, key=lambda x: x.get("timestamp", ""), reverse=descending
    )


