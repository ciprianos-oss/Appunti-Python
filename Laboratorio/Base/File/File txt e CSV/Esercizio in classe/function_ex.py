'''
Scrivere un programma che permetta di inserire
alcuni nomi di studenti e salvarli nel file
stud.txt uno per riga

Il programma deve:
    - Visualizzare tutti i nomi;
    - Contare quanti studenti sono presenti;
    - Chiedere un nome da cercare e dire se è presente oppure no;
    - Visualizzare i nomi in ordine alfabetico
'''

def gestione_file() -> None:
    # Inserimento degli studenti nel file
    with open("stud.txt", "w") as file_studente:
        numero_di_studenti = int(input("Quanti studenti vuoi inserire?: "))
        for _ in range(numero_di_studenti):
            nome = input("Inserisci il nome di uno studente: ")
            file_studente.write(nome + "\n")
    
    # Lettura degli studenti dal file
    with open("stud.txt", "r") as file_studente:
        studenti = file_studente.read().splitlines()
    
    # Visualizzazione di tutti i nomi
    print("\n--- Elenco degli studenti inseriti ---")
    for studente in studenti:
        print(studente)
        
    # Contare quanti studenti sono presenti
    print(f"\nIl numero totale di studenti salvati è: {len(studenti)}")
    
    # Chiedere un nome da cercare e dire se è presente
    nome_da_cercare = input("\nInserisci il nome da cercare: ")
    if nome_da_cercare in studenti:
        print(f"L'alunno '{nome_da_cercare}' è presente in elenco.")
    else:
        print(f"L'alunno '{nome_da_cercare}' NON è presente.")
        
    # Visualizzare i nomi in ordine alfabetico
    print("\n--- Elenco in ordine alfabetico ---")
    studenti_ordinati = sorted(studenti)
    for studente in studenti_ordinati:
        print(studente)