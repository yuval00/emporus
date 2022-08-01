import random
import time
from typing import List
from model import Model
from threading import Thread
from functools import wraps
import datetime as dt


def timing(func):
    @wraps(func)
    def time_wrapper(*args, **kwargs):
        start_time = dt.datetime.now()
        result = func(*args, **kwargs)
        end_time = dt.datetime.now()
        total_time = (end_time - start_time)
        print(f"Function {func.__name__} timed at {total_time}")
        return result
    return time_wrapper


class Trader:
    current_gain = 0

    def __init__(self, symbols: List[str]):
        self.symbols = symbols
        self.aggregated = {}
        self.model = Model()

    def calc(self, aggregated_quotes):
        if len(aggregated_quotes) >= 2:
            time.sleep(0.5)
            return {'std': 2542, 'max': 24, 'min': 2}
        else:
            raise Exception('aggregated quotes must have only 10 elements')

    def sell(self, symbol):
        sell_price = random.randint(1, 100)
        self.current_gain += sell_price
        print(f'The symbol: {symbol} was sold')

    def buy(self, symbol):
        buy_price = random.randint(1, 100)
        self.current_gain -= buy_price
        print(f'The symbol: {symbol} was bought')

    def handle_symbol_quote(self, symbol_quote):
        """
        The function receives a quote, and aggregates the data for it in a corresponding dict.
        :param symbol_quote: The newest quote to be added to the symbol
        :return: None
        """
        symbol = symbol_quote['symbol']
        if symbol not in self.aggregated.keys():
            self.aggregated[symbol] = [symbol_quote]
        else:
            self.aggregated[symbol].append(symbol_quote)

    @timing
    def handle_prediction_after_aggregation(self, quotes):
        """
        The Function will be called every 10 seconds, and will run predictions based on the different
        symbols that have been sent quotes about.
        :param quotes: The quotes for a stock.
        :return: Prediction results and in how much time should the stock be sold.
        """
        if len(quotes) >= 2:
            calc_result = self.calc(quotes)
            return self.model.predict(calc_result)
        else:
            return False, -1

    def handle_sell(self, symbol, sell_in):
        time.sleep(sell_in)
        self.sell(symbol)
