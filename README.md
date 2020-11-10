# Interview

1. Your mission is to print model results based on the stock exchange quotes and the calculation you apply on them.
 1.1 First You need to get quotes from stock exchange provider - look at the nasdaq.py(first you need to connect, after that you need to supply
     to the receive_quotes func the delegate where you want the quotes to be going. in order to start receiving quotes, you need
     to call the func start
 1.2 implement handle_quotes_data in trader.py:
     when you receive 10 quotes from each of the provided symbols(AMZN,FB for example)
     you need to call the func calc in order to receive a calculation for the aggregated data.
     currently all the quote symbols are coming one after another but it can happen that you'll receive 10 quotes from AMZN and from FB only 8
     so you need to wait until you receive another two from FB before calling calc.
     After you receive the calculated data you need to call the model(model.py) to make a prediction based on the calc data.
     The results of the model are: which of the symbols to buy(you should buy immediately) and seconds to wait before you sell the symbol.
     buy/sell functions are in trader.py

please notice that most of the functions are implemented but you need to call them.
You should implement func handle_quotes_data in trader.py and the main function in __init__.py
when you test all your implementation, please execute it at least 5 min to see it's stable.
Another important thing is that you should make model prediction as fast as you can, the prediction shouldn't
take more than 0.5 sec after the last received quote
supply your solution by email to michael@emporus.com or if you have any other questions feel free to ask via the email.

2. wrap you logic with rest API - asyncio so it will return the current gain which in trader.py
3. create unit tests with mocks to trader.py
4. create decorator to print the time it took some method to execute
