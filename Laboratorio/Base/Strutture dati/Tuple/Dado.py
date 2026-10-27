import random

def lancio_dado() -> None:
    facce = (1, 2, 3, 4, 5, 6)
    risultati = []

    #Lancio il dado e memorizzo il valore che esce
    n = int(input("Quanti lanci vuoi fare?: "))
    for _ in range(n): #Si mette l'underscore(_) quando NON si usa il contatore
        lancio = random.choice(facce)
        risultati.append(lancio)
    
    print(risultati)

    #Tolgo degli elementi dal set
    ris_set = set(risultati)
    da_togliere = {2, 3}
    tolti = ris_set - da_togliere
    print(tolti)