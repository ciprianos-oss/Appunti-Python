import json

def gestione_json() -> None:
    contatore = 0

    # Lettura del file
    with open("libri.json", "r", encoding="utf-8") as mioFile:
        libri = json.load(mioFile)  # lista di dizionari

    # Titolo e autore di tutti i libri + conteggio
    print("Elenco dei libri:")
    for libro in libri:
        print(f"- {libro['titolo']} di {libro['autore']}")
        contatore += 1

    print(f"\nNumero di libri presenti: {contatore}")

    # Anno inserito dall'utente
    while True:
        try:
            anno = int(input("\nInserisci un anno: "))
            break
        except ValueError:
            print("Valore non valido, inserisci un numero intero.")

    # Libri pubblicati dopo l'anno inserito dall'utente
    trovati_dopo = False
    print(f"\nLibri pubblicati dopo il {anno}:")
    for libro in libri:
        if libro["anno"] > anno:
            print(f"- {libro['titolo']} ({libro['anno']})")
            trovati_dopo = True

    if not trovati_dopo:
        print("Nessun libro trovato.")

    # Ricerca di un titolo nel catalogo tramite input dell'utente
    titolo_cercato = input("\nInserisci il titolo di un libro: ").strip()

    presente = False
    for libro in libri:
        if libro["titolo"].lower() == titolo_cercato.lower():
            presente = True
            break

    if presente:
        print(f'Il libro "{titolo_cercato}" è presente nel catalogo.')
    else:
        print(f'Il libro "{titolo_cercato}" non è presente nel catalogo.')