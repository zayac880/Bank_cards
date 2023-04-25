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

