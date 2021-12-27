import math
import time
import random
import utils

import sched
import time

import scrollphathd
from scrollphathd.fonts import font3x5, font5x7smoothed


from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

# turns the screen white
scrollphathd.fill(0)
scrollphathd.show()

s = sched.scheduler(time.time, time.sleep)


def update_price(sc):
    print("fetching data")
    r = cg.get_price(ids='bitcoin', vs_currencies='gbp')
    display = f"{utils.human_format(r['bitcoin']['gbp'])} "
    scrollphathd.write_string(display, brightness=0.2)
    s.enter(60, 1, update_price, (sc,))


def scroll(sc):
    # Show the buffer
    scrollphathd.show()
    # Scroll the buffer content
    scrollphathd.scroll()
    s.enter(0.2, 1, scroll, (sc,))


s.enter(60, 1, update_price, (s,))
s.enter(0.2, 1, scroll, (s,))
s.run()
