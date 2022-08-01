import pytest
from trader import Trader


@pytest.fixture
def trade():
    return Trader(["FB", "AMZN"])


def test_buy(trade):
    start_value = trade.current_gain
    trade.buy("FB")
    assert trade.current_gain < start_value


def test_sell(trade):
    start_value = trade.current_gain
    trade.sell("FB")
    assert trade.current_gain > start_value


def test_delayed_sell(trade):
    start_value = trade.current_gain
    trade.handle_sell("FB", 2)
    assert trade.current_gain > start_value


def test_calc(trade):
    calc_result = trade.calc(['stub', 'list'])
    assert calc_result['std'] == 2542 and calc_result['max'] == 24 and calc_result['min'] == 2


def test_handle_symbol_quote(trade):
    trade.handle_symbol_quote({'symbol': 'FB'})
    assert len(trade.aggregated['FB']) == 1
