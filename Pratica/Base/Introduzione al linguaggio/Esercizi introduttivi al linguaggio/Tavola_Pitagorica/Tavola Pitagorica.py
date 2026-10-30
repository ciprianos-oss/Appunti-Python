num = int(input("Inserisci il numero in cui stampare la tavola pitagorica: "))

for i in range(1, num + 1):
    for j in range(num + 1):
        prodotto = i * j
        print(f"{prodotto:4}", end="")
    print()