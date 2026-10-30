#Creazione del dizionario
studente = {
    "Nome": "Salvatore",
    "Cognome": "Cipriano",
    "Eta": 19,
    "Classe": "5D",
    "Media": 9.5
}

#Mando a video un elemento del dizionario
print(studente["Nome"])
studente["promosso"] = True #Aggiunta di un campo al dizionario

#Iterazione tramite ciclo
for chiave, valore in studente.items():
    print(chiave, ": ", valore) # Separo la chiave dal contenuto