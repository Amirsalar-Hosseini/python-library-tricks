import math
from turtle import *

def first(x):
    return 15 * math.sin(x) ** 3

def second(x):
    return 12 * math.cos(x) - 5 * math.cos(2 * x) - 2 * math.cos(3 * x) - math.cos(4 * x)

speed(2000)
bgcolor("black")
for i in range(360):
    x = first(math.radians(i)) * 10
    y = second(math.radians(i)) * 10
    goto(x, y)
    color("#F52375")
    goto(0, 0)

done()
