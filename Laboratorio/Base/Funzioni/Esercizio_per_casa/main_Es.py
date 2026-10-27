import Fun_Es

def main() -> None:
    n1 = float(input("Inserisci il primo operando: "))
    n2 = float(input("Inserisci il secondo operando: "))
    op = input("Inserisci l'operazione (+, -, *, /): ")

    res, errore = Fun_Es.calcola_numeri(n1, n2, op)

    if errore:
        print("Errore: operazione non valida o divisione per zero.")
    else:
        print(f"Risultato: {res}")

if __name__ == "__main__":
    main()