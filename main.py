#!/usr/bin/env python

import time
import random

import scrollphathd

scrollphathd.write_string(" Hello World!", brightness=0.5)

while True:
    # Show the buffer
    scrollphathd.show()
    # Scroll the buffer content
    scrollphathd.scroll()
    # Wait for 0.1s
    time.sleep(0.1)
