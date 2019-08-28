# from math import radians,sin
#
#
#
# rad90=radians(90)
# # radians=radians(90)
# # print(radians)
#
# rad45=radians(180)
# print(rad45)


import time
from datetime import datetime

# def display_time(time=datetime.now()):

def display_time(time=None):
    if time is None:
        time=datetime.now()
    print(time.strftime("%B %d,%Y %H:%M:%S"))

display_time()
time.sleep(1)

display_time()
time.sleep(1)
display_time()
time.sleep(1)

from html import escape as h_escape
from glob import escape as m_escape

print(help(h_escape))

import html
import glob

print(html.escape)
print(glob.escape)