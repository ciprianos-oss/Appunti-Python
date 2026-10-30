'''
1. DEFINIZIONE DEGLI ARRAY
'''
giorni      = ["Lunedi", "Martedi", "Mercoledi", "Giovedi", "Venerdi", "Sabato", "Domenica"]
temperature = []

'''
2. INSERIMENTO DEI DATI
'''
for i in giorni:
    temperatura_letta = float(input(f"Inserisci la temperatura di {i}: "))
    temperature.append(temperatura_letta)

'''
3. STAMPA DEI VALORI INSERITI DALL'UTENTE
'''
for i in range(len(giorni)):
    print(f"La temperatura di {giorni[i]} è di: {temperature[i]} gradi")

'''
4. STATISTICHE
'''
temperatura_minima = min(temperature)
temperatura_massima = max(temperature)
temperatura_media = sum(temperature)/len(temperature)

# Ricerca del giorno piu caldo della settimana
giorno_piu_caldo = giorni[temperature.index(temperatura_massima)]

# Ricerca dei giorni piu caldi della media
giorni_piu_caldi = []
for i in range(len(giorni)):
    if temperature[i] > temperatura_media:
        giorni_piu_caldi.append(giorni[i])

print(f"La temperatura minima registrata è di {temperatura_minima} gradi")
print(f"La temperatura massima registrata è di {temperatura_massima} gradi")
print(f"La media settimanale è di {temperatura_media}")
print(f"Il giorno più caldo è: {giorno_piu_caldo}")
print(f"Giorni sopra la media: {', '.join(giorni_piu_caldi)} ({len(giorni_piu_caldi)})")