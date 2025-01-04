import pyautogui as auto
from time import sleep
import sys

x = []

sleep(3)

l = len(x)
p = 0

c = 0

for i in x:
    auto.write(i[:-2])
    auto.press('enter')

    s = str(c) + ":| Line" + str(c + 4) + '\n'
    c = c + 1
    p = c / l * 100
    b = ("Loading.. " + str("%.4f" % p) + '%')
    
    # \r prints a carriage return first, so `b` is printed on top of the previous line.
    sys.stdout.write('\r' + s+b)

    sleep(8)
