#!/bin/python3


#Dichiaro e creo l'input
N1 = int(input("Primo Numero: "))
N2 = int(input("Secondo Numero: "))

#Converto da Int a Str
N1S =  str(N1)
N2S = str(N2)


#Eseguo il calcolo
SOMMA = str((N1 + N2))
PROD = str((N1 * N2))



#debug
#print(type(N1))
#print(type(N2))

#Stampo a video il risultato
print("La Somma di  " +  N1S + " e " + N2S + " e' uguale a " + SOMMA + ".")
print("Il prodotto di  " +  N1S + " e " + N2S + " e' uguale a " + PROD + ".")
