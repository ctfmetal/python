#!/bin/python3

# Creo Lista
lista = [1, 2, 3, 4]

# Stampo la lista-----------------------------------
ris1 = str(print("Ecco gli elementi della lista: ", lista))
# print(lista)
# --------------------------------------------------

# Interlinea
print()

# Stampo il secondo elemento della lista-------------
lista = [1, 2, 3, 4]
ris2 = str(print("Ecco il secondo elemento della lista ", lista[1]))
# print(lista[1])
# ----------------------------------------------------

# Interlinea
print()

# Sostituisco il terzo valre della stringa-----------
# Definisco la lista
lista = [1, 2, 3, 4]

# Sostiuisco il valore
terzo = str(lista[2])
lista[2] = "TRE"
sost = str(lista[2])

# lista col valore sostuito
print("Sostituisco il terzo valore: " + terzo + " In: " + sost)
ris3 = str(print("Ecco gli elementi della lista: ", lista))
# print(lista)
# ---------------------------------------------------

# Interlinea
print()

#  Stampo i primi 3 valori della lista------------------------
# primo = str(lista[0])
# secondo = str(lista[1])
# terzo = str(lista[2])

# Definisco la lista
lista = [1, 2, 3, 4]
print("Ecco il primi 3 valori della lista: ", lista[:3])
# print(lista[:3])
# -------------------------------------------------------------

# Interlinea
print()

# Elimino il secondo elemento della lista-------------------------
# Definisco la lista
lista = [1, 2, 3, 4]

# Rimuvo il secondo valore
lista.remove(2)
print("Ecco la liste senza il secondo valore: ", lista)
# print(lista)
# --------------------------------------------------------------------

# Interlinea
print()

# Conto quante volte un elemento è presente nella lista-----------------
# Creo la lista e la stampo
lista = [1, 2, 2, 3]
print("Ecco la lista:",lista)

# Estrggo gli elementi
primo = lista[0]
secondo = lista[1]
terzo = lista[2]
quarto = lista[3]

# DEBUG
# print(primo)

# Conto elementi
conto1 = lista.count(primo)
st1 = str(primo)
print("Il primo elemento della lista è: " + st1, "che è presente ", conto1, " volte nella lista")

conto2 = lista.count(secondo)
st2 = str(secondo)
print("Il secondo elemento della lista è: " + st2, "che è presente ", conto2, " volte nella lista")

conto3 = lista.count(terzo)
st3 = str(terzo)
print("Il terzo elemento della lista è: " + st3, "che è presente ", conto3, " volte nella lista")

conto4 = lista.count(quarto)
st4 = str(quarto)
print("Il quarto elemento della lista è: " + st4, "che è presente ", conto4, " volte nella lista")
# --------------------------------------------------------------------------------------------------
