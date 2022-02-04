def get_symbol_pair(symbol_origin, symbol_destination):
    return symbol_origin + symbol_destination

def get_sma_status (sma_9, sma_20):
    market_status = ''
    if sma_20 > sma_9 :
        market_status = 'SELL'
    if sma_20 < sma_9 :
        market_status = 'BUY'
    return market_status
