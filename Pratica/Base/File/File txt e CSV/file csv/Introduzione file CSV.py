import csv

# Scrittura del file csv
with open("stud.csv", "w", newline="") as mioCSV:
    mioScrittore = csv.writer(mioCSV)
    mioScrittore.writerow(["nome", "cognome", "eta", "media"])
    mioScrittore.writerow(["Salvatore", "Cipriano", 18, 6.5])

# Lettura del file csv
with open("stud.csv", "r") as mioCSV:
    mioLettore = csv.reader(mioCSV)

    for riga in mioLettore:
        print(riga)