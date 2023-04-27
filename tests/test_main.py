from main import load_json, hide_account, print_operation


def test_load_json():
    data = load_json('C:/Users/Alex/Desktop/Sky_python/bank_cards/operations.json')
    assert isinstance(data, list)
    assert len(data) == 100


def test_hide_account():
    assert hide_account('Счет 11492155674319392427') == 'Счет ** 2427'
    assert hide_account('11492155674319392427') == ' 1149 21** **** 2427'
    assert hide_account('11492155dfs674319392427') == 'dfs 1149 21** **** 2427'
    assert hide_account('11492155dfs6dfs74319392427') == 'dfsdfs 1149 21** **** 2427'
    assert hide_account('11492155dfs6dfs74319t42427') == 'dfsdfst 1149 21** **** 2427'
    assert hide_account('') == ''


def test_print_operation(capsys):
    # Создаем тестовый словарь с информацией об операции
    operation = {
        'date': '2022-04-25T12:30:00+03:00',
        'description': 'Перевод со счета на счет',
        'from': 'Счет 11492155674319392427',
        'to': 'Maestro 1913883747791351',
        'operationAmount': {'amount': '5000', 'currency': {'name': 'RUB'}}
    }

    # Вызываем функцию для тестовой операции
    print_operation(operation)

    # Получаем значение, выведенное в стандартный вывод
    captured = capsys.readouterr()
    output = captured.out

    # Проверяем, что вывод соответствует ожидаемому формату
    expected_output = '25.04.2022 Перевод со счета на счет\nСчет ** 2427 -> Maestro 1913 88** **** 1351\n5000 RUB\n\n'
    assert output == expected_output