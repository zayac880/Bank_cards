import json
from datetime import datetime


bank_file = 'operations.json'


def load_json(bank_file, encoding='utf-8'):
    """
    Чтение JSON файла и возврат его содержимого в виде списка словарей.
    :param bank_file: Путь к JSON файлу.
    :param encoding: Кодировка файла (по умолчанию utf-8).
    :return: Список словарей, содержащих данные из файла.
    """
    try:
        with open(bank_file, 'r', encoding=encoding) as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON file {bank_file}")
        return []
    return data


def hide_account(account):
    """
    Скрывает номер счета или карты.
    :param account: Номер счета или карты.
    """
    return f"{account[:-14]} *** *** {account[-4:]}"


def print_operation(operation):
    """
    Вывод информации о банковской операции.
    :param operation: Словарь, содержащий информацию о банковской операции.
    """
    date = datetime.strptime(operation['date'][:10], '%Y-%m-%d').strftime('%d.%m.%Y')
    description = operation['description']
    from_account = hide_account(operation.get('from', ''))
    to_account = hide_account(operation['to'])
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    print(f"{date} {description}")
    print(f"{from_account} -> {to_account}")
    print(f"{amount} {currency}")
    print()  # пустая строка между операциями


def process_operations(operations):
    """
    Обработка списка банковских операций.
    :param operations: Список словарей, содержащих информацию о банковских операциях.
    """
    for operation in reversed(operations[-5:]):  # выводим только последние 5 операций
        print_operation(operation)


def main(bank_file):
    """
    Основная функция программы.
    :param bank_file: Путь к JSON файлу с данными о банковских операциях.
    """
    data = load_json(bank_file)
    if data:
        process_operations(data)
    else:
        print(f"Empty operations database loaded from {bank_file}")


if __name__ == '__main__':
    main(bank_file)