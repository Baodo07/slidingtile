import math
import numpy as np
from numpy import random

i = int(input())
a = "(define (problem hard1) \n"+"  (:domain strips-sliding-tile) \n" +"  (:objects"
b = 1
while b < i**2:
    a += " t" + str(b)
    b+=1
b = 1
while b <= i:
    a += " x" + str(b)
    b+= 1
b = 1
while b <= i:
    a += " y" + str(b)
    b+= 1
a += ") \n"
a += "  (:init \n   "
b = 1
while b < i**2:
    a += "(tile t" + str(b) +") "
    b+=1
a+= "\n   "
b = 1
while b <= i:
    a += "(position x" + str(b) +") "
    b+= 1
a+= "\n   "
b = 1
while b <= i:
    a += "(position y" + str(b) +") "
    b+= 1
a+= "\n   "
b = 1
while b < i:
    a += "(inc x" + str(b) + " x"+ str(b+1) +") "
    b+= 1
b = i
while b > 1:
    a += "(dec x" + str(b) + " x"+ str(b-1) +") "
    b-= 1
a+= "\n   "
b = 1
while b < i:
    a += "(inc y" + str(b) + " y"+ str(b+1) +") "
    b+= 1
b = i
while b > 1:
    a += "(dec y" + str(b) + " y"+ str(b-1) +") "
    b-= 1
a+= "\n   "
from numpy import random
import numpy as np
size = i
arr1 = list(range(1, size * size))
arr2 = []
for x in range(1, size * size):
	value = random.choice(arr1)
	arr1.remove(value)
	arr2.append("at t"+str(value))
arr2.append("blank")
for n in range(i):
    for m in range(i):
        a += "(" +str(arr2[n*i+m]) + " x"+str(m+1) +" y" + str(n+1)+ ") "
a += ")\n"
a += "  (:goal \n"
a += "   (and "
for n in range(i):
    for m in range(i):
        if n*i+m+1 == i*i:
            break
        a += "(at t" + str(n*i+m+1) + " x"+str(m+1) +" y" + str(n+1)+ ") "
a += ")) \n"
a+= ")"
print(a)
