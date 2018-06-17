from math import *

def sincos (n):
    a = []
    b = []
    for i in range(len(n)):
        a.append(pi/2 - n[i])
        b.append(cos(n[i]) -  sin(n[i]))

    return a,b