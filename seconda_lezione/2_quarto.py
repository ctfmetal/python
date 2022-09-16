#!/bin/python3


# Dichiaro le variabili e creo gli input.

ore = int(input("Quente ore hai lavorato? "))
tar = int("10")

diff = int(ore - 40)

# DEBUG
# print(type(diff))
# print(diff)

# Se le ore sono + di 40
if ore > 40:
    base = int(tar * 40)
    conto1 = int(diff * 1.5 * 10)
    paga = str(conto1 + base)

# Se le ore sono - di 40
else:
    paga = str(ore * tar)

# Stampo a video
print("Paga Totale " + paga)
