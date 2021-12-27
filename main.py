import math
import time
import random
import utils
import scrollphathd
from scrollphathd.fonts import font3x5

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

# turns the screen white
scrollphathd.fill(0)
scrollphathd.show()

r = cg.get_price(ids='bitcoin', vs_currencies='gbp')
display = f"{utils.human_format(r['bitcoin']['gbp'])} "
scrollphathd.write_string(display, font=font3x5, brightness=0.2)

# asdfasdf
while True:
    # Show the buffer
    scrollphathd.show()
    # Scroll the buffer content
    scrollphathd.scroll()
    # Wait for 0.1s
    time.sleep(0.1)
