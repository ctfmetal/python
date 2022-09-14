#!/bin/python3


#Dichiaro le variabili e creo gli input.

ore = int(input("Quente ore hai lavorato? "))
tar = int("10")

diff = int(ore - 40)

# DEBUG
# print(type(diff))
# print(diff)

if ore < 40:
    conto = ( diff / 2 * 1,5 )
    print(conto)
else:
    conto=int(ore * tar)
    print(conto)


# Stampo a video.
#print("Mi spiace non sei maggiorenne. Chiedi ai tuuoi genitori.")

