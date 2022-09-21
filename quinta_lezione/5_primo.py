#!/bin/python3

# Import modulo random
import random



# Chiedo il numero dei giocatori
giocatori = int(input("** Inserici la modalità gioco: \n 1: 1 Giocatore \n 2: 2 Giocatori \n ** Scelta: "))

if giocatori == 0 or giocatori >= 3 or giocatori == "":
    print("Giocatori consentiti 1/2")
    exit()

if giocatori == "1":
    player = "1"
if giocatori == "2":
    player = "2"

# Debug
# print(giocatori)

if giocatori == 1:
    # Debug
    # print("dentro")

    # Inizializzo la scelta dell'avversario e le variabili
    print()
    scelta = int(input("Fai la tua Scelta \n 1: Carta \n 2: Forbici \n 3: Pietra \n ** Scelta: "))

    if scelta == 0 or scelta >= 4 or scelta == "":
        print("Devi scegliere tra 1/2/3. Stai Attento!")
        exit()

    # Sezione Avversario PC-------------------------------------------------------------------------
    # Creo lista per la scelta del computer e faccio scegliere al computer
    # sceltapc=str(0)
    operandi = [1, 2, 3]
    computer = int(random.choice(operandi))
    comp = str(computer)

    # Valorizzo le scelte
    if computer == 1:
        sceltapc = str("Carta")
        # print("ok")
    if computer == 2:
        sceltapc = str("Forbici")
        # print("ok")
    if computer == 3:
        sceltapc = str("Pietra")
        # print("ok")
    # ----------------------------------------------------------------------------------------------

    # Valorizzo le scelte Umane --------------------------------------------------------------------
    if scelta == 1:
        scelta1 = str("Carta")
        valore = 1
        v = str(valore)
    if scelta == 2:
        scelta1 = str("Forbici")
        valore = 2
        v = str(valore)

    if scelta == 3:
        scelta1 = str("Pietra")
        valore = 3
        v = str(valore)
    # -------------------------------------------------------------------------------------------

    # Elaborazione del vincitore:
    print()
    print("Tua Scelta:" + scelta1, " " + v)
    print("Sua Scelta:" + sceltapc, " " + comp)

    if scelta1 == sceltapc:
        print("Pareggio! Riprovate")

    # Risultati
    # 1:carta 2:Forbici 3:Pietra
    # Carta vs Forbici
    if valore == 1 and computer == 2:
        print("Vince il pc")
        exit()
    if valore == 2 and computer == 1:
        print("Vinci tu!")
        exit()

    # Carta vs Pietra
    if valore == 1 and computer == 3:
        print("Vinci tu!")
        exit()
    if valore == 3 and computer == 1:
        print("Vince il pc")
        exit()

    #  Forbici vs carta
    if valore == 2 and computer == 1:
        print("Vinci tu!")
        exit()
    if valore == 1 and computer == 2:
        print("Vince il pc")
        exit()

    # Forbici vs Pietra
    if valore == 2 and computer == 3:
        print("Vince il pc")
        exit()
    if valore == 3 and computer == 2:
        print("Vinci tu!")
        exit()

    # Pietra vs Carta
    if valore == 3 and computer == 1:
        print("Vince il pc")
        exit()
    if valore == 1 and computer == 3:
        print("Vinci tu!")
        exit()

    # Pietra vs Forbici
    if valore == 3 and computer == 2:
        print("Vinci tu!")
        exit()
    if valore == 2 and computer == 3:
        print("Vince il pc")
        exit()
# ---------------------------------------------------------------------------------------------------
# Se i giocatori sono 2
print()

if giocatori == 2:
    scelta_g1 = int(input("*** Giocatore 1 \n Fai la tua Scelta \n 1: Carta \n 2: Forbici \n 3: Pietra \n ** Scelta: "))
    # print(scelta)

    if scelta_g1 == 0 or scelta_g1 >= 4 or scelta_g1 == "":
        print("Devi scegliere tra 1/2/3. Stai Attento!")
        exit()

    # Elaboro al risposta giocatore 1
    if scelta_g1 == 1:
        g1 = str("Carta")
        g1s = 1
    if scelta_g1 == 2:
        g1 = str("Forbici")
        g1s = 2
    if scelta_g1 == 3:
        g1 = str("Pietra")
        g1s = 3

    scelta_g2 = int(input("*** Giocatore 2 \n Fai la tua Scelta \n 1: Carta \n 2: Forbici \n 3: Pietra \n ** Scelta: "))
    # print(scelta)

    if scelta_g2 == 0 or scelta_g2 >= 4 or scelta_g2 == "":
        print("Devi scegliere tra 1/2/3. Stai Attento!")
        exit()

    # Elaboro al risposta giocatore 2
    if scelta_g2 == 1:
        g2 = str("Carta")
        g2s = 1
    if scelta_g2 == 2:
        g2 = str("Forbici")
        g2s = 2
    if scelta_g2 == 3:
        g2 = str("Pietra")
        g2s = 3

    print()
    print("Scelta Giocatore 1:" + g1)
    print("Scelta Giocatore 2:" + g2)

    # Elaborazione del vincitore
    if g1s == g2s:
        print("Pareggio! Riprovate")

    # Risultati
    # 1:carta 2:Forbici 3:Pietra
    # Carta vs Forbici
    if g1s == 1 and g2s == 2:
        print("Vince Giocatore 2")
        exit()
    if g1s == 2 and g2s == 1:
        vin = str("UMANO")
        print("Vince Giocatore 1")
        exit()

        # Carta vs Pietra
    if g1s == 1 and g2s == 3:
        print("Vince Giocatore 1")
        exit()
    if g1s == 3 and g2s == 1:
        print("Vince Giocatore 2")
        exit()

        #  Forbici vs carta
    if g1s == 2 and g2s == 1:
        print("Vince Giocatore 1")
        exit()
    if g1s == 1 and g2s == 2:
        print("Vince Giocatore 2")
        exit()

        # Forbici vs Pietra
    if g1s == 2 and g2s == 3:
        print("Vince Giocatore 2")
        exit()
    if g1s == 3 and g2s == 2:
        print("Vince Giocatore 1")
        exit()

        # Pietra vs Carta
    if g1s == 3 and g2s == 1:
        print("Vince Giocatore 2")
        exit()
    if g1s == 1 and g2s == 3:
        print("Vince Giocatore 1")
        exit()

        # Pietra vs Forbici
    if g1s == 3 and g2s == 2:
        print("Vince Giocatore 1")
        exit()
    if g1s == 2 and g2s == 3:
        print("Vince Giocatore 2")
        exit()