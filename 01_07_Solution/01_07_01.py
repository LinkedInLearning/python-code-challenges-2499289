import math as m
import random as r
verfuegbareZahlen = list(range(1,49))
def ziehung():
    return r.sample(verfuegbareZahlen, 6)
i = 0
while(i < 10):
    print(ziehung())
    i = i + 1
