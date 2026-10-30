# Funzioni per calcolare la media e dire l'esito
def calcola_media(voti):
    somma = 0
    for voto in voti:
        somma += voto

    media = somma / len(voti)
    return media


def esito(media):
    if media >= 6:
        return "Promosso"
    else:
        return "Non promosso"

# Definizione dell'Array di voti
voti = [7, 5, 8, 6, 7]

# Lancio delle funzioni
media = calcola_media(voti)
risultato = esito(media)

# Stampo i vari risultati
print("Voti:", voti)
print("Media:", media)
print("Esito:", risultato)