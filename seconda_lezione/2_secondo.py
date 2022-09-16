#!/bin/python3


# Dichiaro le variabili e creo gli input.
pwd = str("Password_sicura")
insert = str(input("Inserisci una Password: "))


# Controllo opassword
if pwd == insert:
    # Stampo a video.
    print("Benvenuto nome_utente")
else:
    # Stampo a video
    print("Password non corretta")
