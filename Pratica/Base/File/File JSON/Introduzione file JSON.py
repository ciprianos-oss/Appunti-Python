# Importazione del modulo json
import json

# Creazione dizionario dello studente
stud = {
    "nome": "Giovanni",
    "cognome": "Franco",
    "eta": 18,
    "classe": "5D",
    "media": 4.2
}

# Scrittura del dizionario nel file JSON
with open("studente.json", "w") as myFile:
    json.dump(stud, myFile, indent=4)

# Lettura del file studente.json
with open("studente.json", "r") as MyFile:
    alunno_letto = json.load(MyFile)

print(alunno_letto)