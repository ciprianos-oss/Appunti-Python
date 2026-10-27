'''
Scrivre un programma che legga 5 temperature,
le salvi in un file temp.txt una per riga e
successivamente vengono lette le temperature registrate
'''

# Apro il file con l'operatore with, che chiude da solo il file in automatico e rimane aperto fino a quando ci opero all'interno
with open("temp.txt", "w") as mio_file:
    for _ in range(5):
        temp = input("Inserisci una temperatura: ")
        mio_file.write(temp + "\n") # Scrivo le temperature nel file

# Lettura del file appena creato
with open("temp.txt", "r") as mio_file:
    print(mio_file.read())