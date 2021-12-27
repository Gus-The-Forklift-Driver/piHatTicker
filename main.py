#!/usr/bin/env python

import time
import random

import scrollphathd

from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
from secret import coinMarketCapApiKey
cmc = CoinMarketCapAPI(coinMarketCapApiKey)

r = cmc.cryptocurrency_quotes_latest(symbol='BTC')

display = f"BTC  24h change = {r.data['volume_change_24h']}, current price = {r.data['price']}"

scrollphathd.write_string(" Hello World!", brightness=0.5)

while True:
    # Show the buffer
    scrollphathd.show()
    # Scroll the buffer content
    scrollphathd.scroll()
    # Wait for 0.1s
    time.sleep(0.1)
