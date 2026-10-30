import random

facce = (1, 2, 3, 4, 5, 6)
risultati = []

#Lancio il dado e memorizzo il valore che esce
n = int(input("Quanti lanci vuoi fare?: "))
for _ in range(n):
    lancio = random.choice(facce)
    risultati.append(lancio)

# Trova i numeri che non sono presenti nei risultati
non_usciti = [f for f in facce if f not in risultati]

print(risultati)
print(f"Il numero massimo che e uscito è: {max(risultati)}")
print(f"Il numero minimo che e uscito è: {min(risultati)}")
print(f"Il numero 6 è uscito {risultati.count(6)} volte")

if non_usciti:
    print(f"I numeri che NON sono mai usciti sono: {non_usciti}")
else:
    print("In questi lanci sono usciti tutti i numeri da 1 a 6 almeno una volta!")