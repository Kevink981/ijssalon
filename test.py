from algemene_functies import *
from reclame import *

print("-" * 50)
print("argument 2:", mijn_functie_1(2))
print("argument 2:", mijn_functie_1(4))
print("argument 10:", mijn_functie_1(10))
print("argument 12:", mijn_functie_1(12))

print("-" * 50)
print("argument 12, 3:", mijn_functie_2((12, 3)))
print("argument 12, 2:", mijn_functie_2((12, 2)))
print("argument 10, 5:", mijn_functie_2((10, 5)))
print("argument 100, 20:", mijn_functie_2((100, 20)))

print("-" * 50)
print(aanbieding_1("aardbei", 5, 0.2))
print(aanbieding_1("vanille", 4.5, 0.1))
print(aanbieding_1("chocolade", 6, 0.15))

print("-" * 50)
print(inkomsten_totaal([200, 300, 400, 500, 600], 0.21))
print(inkomsten_totaal([150, 250, 350, 450, 550], 0.09))

print("-" * 50)
print(laag_en_hoog([10, 20, 30, 40, 50]))
print(laag_en_hoog([5, 15, 25, 35, 45]))

print("-" * 50)
print(gemiddelde([10, 20, 30, 40, 50]))
print(gemiddelde([5, 15, 25, 35, 45]))

print("-" * 50)
print(meervoudig([10, 20, 30, 40, 50]))
print(meervoudig([5, 15, 25, 35, 45]))

print("-" * 50)