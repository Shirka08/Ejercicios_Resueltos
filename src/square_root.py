import math
import random

def square_root(number):
    assert x >= 0
    y = math.sqrt(number)
    assert y * y == number
    return y
for i in range(1, 1000):
    r = random.random() * 1000
    try:
        z = square_root(r)
    except:
        print r, r - math.sqrt(r) * math.sqrt(r)
        breaks

  print "Done"