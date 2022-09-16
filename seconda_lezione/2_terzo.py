#!/bin/python3

#Dichiaro le variabili e creo gli input.
name = str(input("Nome: "))
eta = int(input("eta: "))
pwd = str("Password_sicura")

# Controllo l'età
if eta >= 18:
    # Stampo a video.
    print("Ciao, Benvenuto. Sei Maggiorenne")

    #Controllo password
    insert = str(input("Inserisci una Password: "))
    if pwd == insert:
        # Stampo a video.
        print("Benvenuto nome_utente")
    else:
        # Stampo a video
        print("Password non corretta")
else:
    # Stampo a video.
    print("Mi spiace non sei maggiorenne. Chiedi ai tuuoi genitori.")
