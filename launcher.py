import client
import utils
import indicateurs

trader = client.get_test_client() # test /!\
trader_btc_balance  = client.get_client_balance(trader, 'BTC')
trader_usdt_balance = client.get_client_balance(trader, 'USDT')

symbol_pair = utils.get_symbol_pair('BTC', 'USDT')
sma_9       = indicateurs.get_sma_9 (symbol_pair, '1d')
sma_20      = indicateurs.get_sma_20 (symbol_pair, '1d')
sma_market_state = utils.get_sma_status(sma_9, sma_20)

# RECUPERATION ordre du marché dans le fichier
with open("market_state.txt", "r") as reader:
    old_market_state = reader.read()
    if old_market_state == sma_market_state: # dernier ordre == ordre actuel du marché ?
        pass # si oui, on fait rien
    else: # si non, on inverse + passage d'ordre
        if sma_market_state == 'BUY' and trader_usdt_balance > 0: # si le marché est en achat et que j'ai de la fiat, j'achete
            # set_order (client, 'BUY', symbol_pair, qty)
            print ('BUY')
        if sma_market_state == 'SELL' and trader_btc_balance > 0: # si le marché est en vente et que j'ai de la crypto, je vends
            # set_order (client, 'SELL', symbol_pair, qty)
            print ('SELL')

# MAJ ordre du marché dans le fichier
file_market_state = open("market_state.txt", "w")
file_market_state.write(sma_market_state)
file_market_state.close()


