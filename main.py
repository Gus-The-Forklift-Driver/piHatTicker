import math
import time
import random

import scrollphathd

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

r = cg.get_price(ids='bitcoin', vs_currencies='gbp')
display = f"r{['bitcoin']['gbp']}£ "
scrollphathd.write_string(display, brightness=0.2)

# asdfasdf
while True:
    # Show the buffer
    scrollphathd.show()
    # Scroll the buffer content
    scrollphathd.scroll()
    # Wait for 0.1s
    time.sleep(0.1)
