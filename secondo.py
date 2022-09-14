#!/bin/python3

#Dichiaro le variabili e creo gli input.

ore = int(input("Ore lavorative: "))
tariffa = int(input("Tariffa oraria: "))

#Eseguo operaziona matematica e cambio il formato della variabile per la concatenazione.
RIS = str((ore * tariffa))

#Stampo a video.
print("Con il tuo lavoro hai guadagnato " +  RIS + " lordi")
