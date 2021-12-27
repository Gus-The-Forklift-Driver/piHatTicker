import math
import time
import random

import scrollphathd

from pycoingecko import CoinGeckoAPI


i = 0

while True:
    i += 2
    s = math.sin(i / 50.0) * 2.0 + 6.0

    for x in range(0, 17):
        for y in range(0, 7):
            v = 0.3 + (0.3 * math.sin((x * s) + i / 4.0)
                       * math.cos((y * s) + i / 4.0))

            scrollphathd.pixel(x, y, v)

    time.sleep(0.01)
    scrollphathd.show()
#scrollphathd.write_string(display, brightness=0.2)

# # asdfasdf
# while True:
#     # Show the buffer
#     scrollphathd.show()
#     # Scroll the buffer content
#     scrollphathd.scroll()
#     # Wait for 0.1s
#     time.sleep(0.1)
