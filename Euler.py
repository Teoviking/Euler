import numpy as np
import matplotlib.pyplot as plt

def func( x, y ):
    return (2*x - y)
     
def euler( x0, y, h, x ):
    temp = -0
 
    while x0 < x:
        temp = y
        y = y + h * func(x0, y)
        x0 = x0 + h
 
    print("Approximate solution at x = ", x, " is ", "%.6f"% y)
     
x0 = 1
y0 = 2
h = 0.001
 
x = 2
 
euler(x0, y0, h, x)