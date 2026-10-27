#Importo la libreria per il sorteggio del numero
import random

def sorteggio() -> None:
    num_segreto = random.randrange(1, 10)
    trovato = False
    conteggio_tentativi = 0
    conteggio_totale = []

    #Ciclo per verificare se il numero e stato indovinato
    while not trovato and conteggio_tentativi < 5:
        num_utente = int(input("Inserisci un numero: "))

        conteggio_tentativi += 1
        if num_utente == num_segreto:
            if conteggio_tentativi == 0:
                print("Hai indovinato il numero ed hai indovinato al primo tentativo!!")
                trovato = True
            else:
                print(f"Hai indovinato il numero in {conteggio_tentativi} tentativi!")
                trovato = True
        elif num_utente > num_segreto:
            print("Troppo alto!")
            conteggio_totale.append(conteggio_tentativi)
        else:
            print("Troppo basso!")
            conteggio_totale.append(conteggio_tentativi)
        
        if conteggio_tentativi == 5:
            print("Hai perso!")