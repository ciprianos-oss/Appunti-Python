try:
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    
    ris = a/b
    print(f"Il risultato è {ris}")
except ZeroDivisionError: # Lancio l'eccezzione se b è 0
    print("[ERROR] Divisione per 0 non possibile")
except ValueError: # Lancio l'eccezione non è coerente l'input rispetto al tipo desiderato
    print("[ERROR] Valore inserito non valido")
else:
    print("Nessun errore")