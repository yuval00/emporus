from trader import Trader
from nasdaq import StockExchangeProvider
import datetime as dt
from threading import Thread
from fastapi import FastAPI
import uvicorn


trading = Trader(["AMZN", "FB"])
exchanger = StockExchangeProvider()
stop_flag = False


app = FastAPI()


@app.get("/api/gain")
async def get_gain():
    return trading.current_gain


def exchange_thread():
    while not stop_flag:
        try:
            exchanger.configure_quotes_stream(trading.symbols, trading.handle_symbol_quote)
            exchanger.connect('ploni', 'Aa123456')
            exchanger.start()
        except Exception as e:
            pass


def main_stock_aggregator():
    global stop_flag
    start_time = dt.datetime.now()
    current_time = dt.datetime.now()
    th = Thread(target=exchange_thread)
    th.start()
    while (current_time - start_time).total_seconds() < 300:
        if (current_time - start_time).total_seconds() >= 10:
            if current_time.second % 10 == 0:
                agg = trading.aggregated
                trading.aggregated = {}
                for stock in agg.keys():
                    should_buy, sell_in = trading.handle_prediction_after_aggregation(stock)
                    if should_buy:
                        trading.buy(stock)
                        Thread(target=trading.handle_sell, args=(stock, sell_in)).start()
        current_time = dt.datetime.now()
    stop_flag = True


if __name__ == '__main__':
    t = Thread(target=main_stock_aggregator)
    t.start()
    uvicorn.run(app, host="0.0.0.0", port=8000)
