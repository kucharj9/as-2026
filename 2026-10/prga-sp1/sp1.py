# kód žáka: 9
# datum: 12.10.
#

import time
import math

pocet = int(input("pocet: "))

print("\nKulička jede")
for i in range(pocet):
    print(f"{i * ' '}O")
    time.sleep(0.1)

for i in range(pocet+1):
    print(f"{(pocet-i) * ' '}O")
    time.sleep(0.1)

print("\nTabulka")
for i in range(1, pocet+1):
    print(i, i**2, math.sqrt(i))