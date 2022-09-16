#!/bin/python3


# Dichiaro le variabili e creo gli input.
name = str(input("Nome: "))
eta = int(input("eta: "))


# Controllo l'età
if eta >= 18:
    # Stampo a video.
    print("Ciao, Benvenuto. Sei Maggiorenne")
else:
    # Stampo a video.
    print("Mi spiace non sei maggiorenne. Chiedi ai tuuoi genitori.")
