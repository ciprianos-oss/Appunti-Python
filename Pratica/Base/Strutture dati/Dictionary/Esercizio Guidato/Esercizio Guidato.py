def gestione_magazzino() -> None:
    # Definizione del dizionario
    magazzino = {
        "mouse": 12,
        "tastiera": 7,
        "monitor": 5,
        "cuffie": 9
    }

    # Chiedo all'utente di inserire un prodotto da visualizzare
    prodotto = input("Inserisci un prodotto da visualizzare: ")

    if prodotto in magazzino:
        quantita = magazzino[prodotto]

        print(f"Sono disponibili {quantita} pezzi")

        # Chiedo all'utente quanti pezzi sono stati venduti
        pezzi_venduti = int(
            input(f"Quanti pezzi del prodotto '{prodotto}' sono stati venduti?: ")
        )

        if pezzi_venduti > quantita:
            print("Non ci sono abbastanza pezzi da vendere!")
        else:
            magazzino[prodotto] -= pezzi_venduti

            print("\nMagazzino aggiornato:")

            for chiave, valore in magazzino.items():
                print(chiave, ":", valore)
    else:
        print("Prodotto non presente!")

def main() -> None:
    gestione_magazzino()

if __name__ == "__main__":
    main()