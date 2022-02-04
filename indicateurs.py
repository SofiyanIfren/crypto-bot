import requests
import json
import pandas as pd
import ta
from datetime import datetime, timedelta

URL = 'https://api.binance.com/api/v3/klines'

def get_sma_9 (symbol_pair, interval):
    my_date = datetime.now() - timedelta(30)
    date_start = int(my_date.timestamp()*1000)
    date_end   = int(datetime.now().timestamp()*1000)
    parameters = {'symbol' : symbol_pair, 'interval' : interval, 'startTime' : date_start, 'endTime' : date_end}
    res = json.loads(requests.get(URL, params=parameters).text)
    data = pd.DataFrame(res)
    data.columns = ['datetime', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'qav', 'num_trades', 'taker_base_vol', 'taker_quote_vol', 'ignore']
    data['SMA9'] = ta.trend.sma_indicator(data['close'], 9)
    return data['SMA9'].iloc[-1]

def get_sma_20 (symbol_pair, interval):
    my_date = datetime.now() - timedelta(30)
    date_start = int(my_date.timestamp()*1000)
    date_end   = int(datetime.now().timestamp()*1000)
    parameters = {'symbol' : symbol_pair, 'interval' : interval, 'startTime' : date_start, 'endTime' : date_end}
    res = json.loads(requests.get(URL, params=parameters).text)
    data = pd.DataFrame(res)
    data.columns = ['datetime', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'qav', 'num_trades', 'taker_base_vol', 'taker_quote_vol', 'ignore']
    data['SMA20'] = ta.trend.sma_indicator(data['close'], 20)
    return data['SMA20'].iloc[-1]
