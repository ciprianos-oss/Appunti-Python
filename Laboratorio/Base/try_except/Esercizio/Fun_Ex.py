def gestione_errori() -> None:
    colori = ["rosso", "verde", "blu", "giallo", "nero"]

    try:
        pos = int(input("Inserisci la posizione del colore desiderato: "))
        print(colori[pos])
    except ValueError: # Errore di tipo
        print("Devi inserire un numero intero")
    except IndexError: # Errore di indice
        print("Posizione non valida")
    else:
        print("Fine senza errori")