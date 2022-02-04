from binance import ThreadedWebsocketManager
from binance.client import Client

API_KEY    = '<BINANCE_API_KEY>'
SECRET_KEY = '<BINANCE_SECRET_KEY>'

def get_client ():
    return Client(API_KEY, SECRET_KEY)

def get_test_client ():
    client = Client(API_KEY, SECRET_KEY)
    client.API_URL = 'https://testnet.binance.vision/api' # for test API
    return client

def get_client_balance (client, symbol):
    return float(client.get_asset_balance(asset=symbol)['free'])

def get_symbol_price (client, symbol_pair):
    return client.get_symbol_ticker(symbol=symbol_pair)

def set_order (client, action, symbol_pair, qty):
    if action == 'BUY':
        client.order_market_buy(symbol=symbol_pair, quantity=qty)
    if action == 'SELL':
        client.order_market_sell(symbol=symbol_pair, quantity=qty)
