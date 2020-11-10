import random
import time
from typing import List


class Trader:
    current_gain = 0

    def __init__(self, symbols: List[str]):
        self.symbols = symbols

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
        Receive quote from stock exchange, aggregate 10 seconds of quotes from provided symbols.
        If we have more than 2 quotes and exactly 10 seconds of the symbol we can call 'calc'
        to get the calculated data for model prediction -> call predict -> print if the symbol should be bought.
        You receive quote each millisecond.
        quote is made of : time, symbol, price
       return:"""
