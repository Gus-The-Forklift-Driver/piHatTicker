#!/usr/bin/env python

import time
import random

import scrollphathd

from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
from secret import coinMarketCapApiKey
cmc = CoinMarketCapAPI(coinMarketCapApiKey)

try:
    r = cmc.cryptocurrency_quotes_latest(symbol='BTC')
except:
    display = " failed to fetch data"
else:
    display = f" BTC  24h change = {r.data['BTC']['volume_change_24h']}, current price = {r.data['BTC']['price']}"

scrollphathd.write_string(display, brightness=0.2)

while True:
    # Show the buffer
    scrollphathd.show()
    # Scroll the buffer content
    scrollphathd.scroll()
    # Wait for 0.1s
    time.sleep(0.1)
