#!/bin/python3

# Import modulo os
import os

# Chiedo il sito. se non inserisco nulla scelgo google.
sito=str(input("Inserisci sito da monitorare. [Default:'www.google.it']: "))
if sito == "":
    sitoc = str("www.google.com")
else:
    sitoc = str(sito)

# Test di ping
print("Test ping di " + sitoc)
cping = str("ping -c10 " + str(sitoc))

# Stampo i risultati
esito = os.system(cping)
if esito == 0:
    print("Esito Test: " + sitoc + " Up")
else:
    print("Esito Test: " + sitoc + " Down")


