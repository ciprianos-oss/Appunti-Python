#Definisco la funzione per la tavola pitagorica
def tavola_pitagorica(dimensione: int) -> None:
    for i in range(1, dimensione + 1):
        for j in range(1, dimensione + 1):
            prodotto = i * j
            print(f"{prodotto:4}", end="")
            
        print() #Vado a capo per stampare una nuova riga